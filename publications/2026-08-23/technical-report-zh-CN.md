# SPM-Polaris：面向长时程 AI Agent 的证据治理记忆与上下文管理

**技术报告：** Version 1.0<br>
**发布日期：** 2026-08-23<br>
**证据截止：** 2026-08-23<br>
**作者与发布者：** Veridical Tech, Inc.<br>
**联系邮箱：** contact@spmos.ai<br>
**状态：** 第一方技术报告；未经同行评审或第三方独立评估

> 本报告描述 SPM-Polaris V3.0.0 的公开行为与证据边界。它不是 SLA、合规认证、法律意见、融资材料或普遍性能保证。

## 摘要

长上下文与长期记忆解决的是不同问题。上下文窗口是一次模型请求可使用的输入空间；长期记忆是一个跨请求生命周期，涉及选择性写入、候选检索、证据准入、上下文编译、Provider 状态保护、删除与审计。

SPM-Polaris 是当前 SPM 产品：一个面向 AI Agent、带治理长期记忆的 Provider Proxy。它将候选检索与证据准入分开，在上下文压缩过程中保护 Provider 原生状态，在证据不足时拒绝注入，并记录逐请求的证据与 token 边界。Hosted Provider Proxy、Local Proxy 与 MCP 都使用托管 SPM memory plane，但它们在凭证保管、模型流量、调用方式、receipt 和操作责任上不同。

本文说明系统架构、当前有限的第一方观测、局限与后续评测计划。当前 claim ledger 已撤回、且尚未满足重新发布门槛的历史准确率和对比效率数字，不进入本报告的对外宣传结果。

## 1. 长上下文不等于长期记忆

更长的上下文很有价值，但它不能自动回答以下系统问题：

- 哪些历史内容应该成为长期记忆？
- 召回内容是用户陈述、外部观察，还是 assistant 提议？
- 它是否仍然有效，或者已经被更新、取代或删除？
- 删除旧历史时，是否会破坏 system/developer 指令、tool linkage、reasoning state、多模态对象或 Provider 管理的会话 lineage？
- 开发者能否解释本次请求使用了什么记忆、删除了什么历史？

研究也已经表明：相关信息在长上下文中的位置会影响模型使用效果；hard negative 可能降低长上下文 RAG 的最终质量；即便检索条件较好，输入长度本身仍可能造成任务性能下降。

两者的实际区别是：

```text
上下文窗口 = 一次模型请求可以使用的输入空间
长期记忆 = 跨请求、跨时间维护的受治理状态
```

## 2. 系统范围

SPM 是 StellarPath Memory Operating System，由 Veridical Tech, Inc. 开发的产品家族。SPM-Polaris V3.0.0 是当前生产产品。

SPM-Polaris 不是：

- 基础模型；
- 模型转售平台；
- 完整 Agent runtime 或工作流编排器；
- 每个请求都能减少 token 的通用压缩器；
- 完全自托管或 air-gapped 的 memory plane；
- 已完成合规认证或正式生产 SLA 的平台。

它的职责是围绕 Provider 工作流，治理记忆如何写入、召回、准入、编译进入模型上下文、审计与删除。

## 3. 请求与记忆生命周期

公开架构可以概括为：

```text
Eligible source content
  -> 提取与索引
  -> lexical/vector candidates
  -> tenant/namespace/generation/ACL/source-state/provenance 检查
  -> evidence admission 或明确 refusal
  -> 受保护的上下文编译
  -> Provider 原生转发或 MCP tool response
  -> receipt、生命周期维护与删除控制
```

### 3.1 写入路径

记忆可以通过显式 MCP `remember`、Console/source 操作，以及 Provider Proxy 或 Local Proxy 交换中符合条件的可见文本进入。

Observer 使用独立 capture copy。可见用户文本和符合条件的可见 assistant 文本可以被捕获；reasoning summary、thinking/redacted-thinking block、tool/function argument、signature 与 partial JSON 保持为 Provider 协议状态，不进入 memory capture。

### 3.2 候选检索与证据准入

SPM-Polaris 不把向量相似度直接当作事实权威。当前存储优先级为：

```text
user statement > externally observed source > assistant proposal
```

该顺序并不意味着用户陈述客观正确，而是防止较低权威的 assistant 提议静默覆盖用户明确表达的内容。

Recall 结合 lexical 和 vector candidates，考虑来源多样性，并执行最终 evidence gate。没有证据符合条件时，系统返回 `UNKNOWN` 等明确空结果或 refusal，不注入记忆。

### 3.3 Best evidence 与 provenance

公开 recall contract 将简短的 best-evidence `answer` 与有限的 `evidence_refs` 分开。Agent 在需要多个前提或精确来源时，可以通过 read token 读取 backing source 或选定 span。

Memory path 不增加生成式 answer model；最终推理由用户配置的上游 Provider 完成。

## 4. 受保护的上下文编译

上下文压缩被视为状态完整性操作，而不是简单截断。

受保护内容包括 system/developer 指令、最新用户任务、tool call/result linkage、OpenAI Responses reasoning 与 lineage、Anthropic thinking state、多模态对象，以及无法安全重建的未知 Provider 字段。

最近两个符合条件的 exchange 保持受保护。只有当 admitted evidence 绑定到精确 removal set 中的来源时，较旧完整 exchange 才可以被移除。空、降级、不相关或被拒绝的 recall 都会触发 passthrough。

因此，对于短请求、单轮请求、opaque/stateful 请求或没有安全可移除历史的请求，0% reduction 可能是正确结果。

## 5. 接入与凭证边界

| 路径 | Provider 凭证 | 模型流量 | Memory 调用 | Hosted receipt |
|---|---|---|---|---|
| Hosted Provider Proxy | 受保护的 SPM 托管保管 | Client -> SPM -> Provider | 请求链自动执行 | 有 |
| Local Proxy | 权限受限的本地配置 | Client -> Local Proxy -> Provider | Memory mode 开启时自动执行 | 无 |
| MCP | Application 保管 | Application -> Provider | 显式 memory tools | Tool result，不是 hosted proxy receipt |

三条路径都使用托管 SPM memory。Local Proxy 改变 Provider Key 的保管位置和模型流量路径，但不会把 SPM memory plane 移到用户机器。

Proxy 与 MCP 是不同实验路径。MCP 的调用时机和 context placement 由 Host 或模型影响，因此 Proxy 结果不能在缺少 matched-path 重跑时被称为 MCP 结果。

## 6. 删除与可审计性

删除是跨对象生命周期，不是单行数据库删除。Targeted purge 与 clear-memory 会执行 tenant、namespace、account epoch 与 generation 边界检查；清理符合条件的 authoritative/derived objects；推进或执行 memory fence；持久化操作证据并验证 absence。

Source tombstone 会阻止同一个 source identity 在同一 memory generation 中重新入队，从而降低 delayed job 或 index rebuild 导致的“删除后复活”。

活动系统删除不意味着早先生成的 backup、WAL、replica、Provider record 或客户侧副本会在其公开 retention/rotation 周期之前立即消失。

## 7. 当前有限的第一方观测

当前公开证据属于观测，不是普遍 benchmark 或保证。

| 观测 | 结果 | 边界 |
|---|---:|---|
| 一个符合条件的 Hosted Provider Proxy 请求 | 66,265 original input tokens -> 365 forwarded；另有 279 recalled | 单请求；不是均值、SLA 或普遍节省保证 |
| 一个 Starter limiter window | 45 次 burst 中 30 次成功、15 次 HTTP 429 | 一个 30 req/min 窗口；不是容量 benchmark |
| 一个生产 MCP remember/status 往返 | 8.23 秒 ready | 不是 latency SLO |
| 一个生产 MCP remember-to-read 序列 | 写入与读取文本 byte-for-byte 相同 | 不是普遍 integrity-rate benchmark |
| 一个历史 warm MCP recall | 4.93 秒 | 单次观测；不是分布或 SLO |

生产近似 embedding/retrieval stack 在较早内部实验后发生变化。历史 accuracy、evidence containment 和对比 token efficiency 数值继续从公开宣传中撤回，直到新的 immutable result package 满足 republication gate。

## 8. 当前局限

现有证据不能证明：

- 当前生产近似栈的 recall 或 final-answer accuracy；
- p95/p99 latency 分布；
- sustained soak 或 100+ concurrency；
- Hosted Proxy、Local Proxy 与 MCP 质量相同；
- 普遍 token/cost reduction；
- 第三方复现或独立认证；
- 完整自动 moderation、SOC 2、ISO 27001 或正式企业 SLA。

## 9. 后续评测计划

下一步有价值的实验包括：

1. 使用精确 commit、configuration、model/embedding identity、corpus identifier、launch command、raw per-case output、排除项和 digest 的 immutable 生产近似重跑；
2. 在控制下游模型、tool schema、调用策略、context placement、judge 和 seed 的条件下，配对比较 Proxy、Local Proxy 与 MCP；
3. 使用 stale fact、conflict、assistant speculation 和 semantic hard negative 的 evidence-admission ablation；
4. 覆盖 tool identifier、partial stream、reasoning state 与 stateful lineage 的 Provider-state integrity test；
5. 覆盖 delayed job、reindex、replay 与 repeated ingest 的删除 fault injection；
6. 分解 gateway、extraction、embedding、retrieval、reranking、queue 与 Provider execution 延迟。

## 10. 官方来源

- 官网：https://spmos.ai/
- 官方定义：https://docs.spmos.ai/official-definitions
- 架构：https://docs.spmos.ai/architecture
- 接入边界：https://docs.spmos.ai/integrations
- 记忆、证据与删除：https://docs.spmos.ai/memory
- 安全：https://docs.spmos.ai/security
- Benchmarks 与局限：https://docs.spmos.ai/benchmarks
- 开源 Local Proxy：https://github.com/VeridicalTech/spm-local-proxy

## 参考文献

1. Maharana et al. *Evaluating Very Long-Term Conversational Memory of LLM Agents.* arXiv:2402.17753.
2. Liu et al. *Lost in the Middle: How Language Models Use Long Contexts.* TACL 2023; arXiv:2307.03172.
3. Jin et al. *Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG.* arXiv:2410.05983.
4. Du et al. *Context Length Alone Hurts LLM Performance Despite Perfect Retrieval.* Findings of EMNLP 2025; arXiv:2510.05381.
5. Packer et al. *MemGPT: Towards LLMs as Operating Systems.* arXiv:2310.08560.

## 披露与权利

Veridical Tech, Inc. 开发 SPM 与 SPM-Polaris，因此与本报告存在直接产品利益。文中观测属于第一方结果，尚未得到第三方独立复现。报告使用了 AI 辅助编辑来帮助重组和润色；Veridical Tech, Inc. 已审查公开 claim boundary，并对发布内容负责。

建议引用：

> Veridical Tech, Inc. (2026). *SPM-Polaris：面向长时程 AI Agent 的证据治理记忆与上下文管理*（Version 1.0）。https://docs.spmos.ai/technical-report

Copyright © 2026 Veridical Tech, Inc. All rights reserved. 允许公开阅读与引用；转载或衍生发布需获得发布者许可。

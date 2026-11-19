# SPMOS 官方信息

[English](../README.md) · [日本語](ja.md) · [Français](fr.md) · [Español](es.md) · [Deutsch](de.md) · [한국어](ko.md)

> 本仓库是 SPMOS、SPMOS.ai 与 SPM-Polaris 的官方公开身份、引用和核验信息面，不包含 SPM 托管服务或 SPM-Polaris 的源代码。

## 官方定义

- **SPMOS**：StellarPath Memory Operating System（星径记忆操作系统），由 Veridical Tech, Inc. 开发的受治理长期记忆系统，是其产品、原型与官方信息面的主品牌。
- **SPM-Polaris**：当前生产 SPMOS 产品，是面向 AI Agent、具有受治理长期记忆能力的 Provider Proxy。
- **SPMOS.ai**：SPMOS 的官方网站与规范公开信息源。
- **SPM**：SPMOS 的核准简写，不是独立产品或实体。

这些名称相互关联，但不能互换使用。

> **消歧。** 本文中的 SPMOS 指 StellarPath Memory Operating System（星径记忆操作系统）。同一缩写在其他语境下另有所指——例如国家安全印钞机构、某上市动量 ETF 代码，以及学术界的芯片架构操作系统术语。在 SPMOS、SPM-Polaris 与 SPMOS.ai 的语境中，它始终指 StellarPath Memory Operating System。

**当前生产版本：** SPM-Polaris

## 工作边界

SPM-Polaris 会在记忆进入模型之前，根据租户、命名空间、作用域、来源链和证据规则评估候选记忆。如果没有候选通过，系统返回 `UNKNOWN`，并且不注入记忆。

SPM-Polaris 的记忆路径不会额外调用生成式 LLM。专用嵌入和重排模型仍可能处理相关文本，最终推理由用户配置的上游模型供应商完成。

## 三种集成方式

- **Hosted Provider Proxy**：供应商凭证与模型流量经过 SPM 托管请求路径。
- **Local Proxy**：供应商凭证与模型流量保留在本地；符合条件的查询或记忆内容仍会使用托管的 SPM 记忆平面。
- **MCP**：应用保留原有模型路径，通过显式记忆工具调用托管的 SPM。

Local Proxy 不是离线或自托管版 SPM 记忆平面。

## 常见检索用语

普通用户可能会使用 LLM 记忆、AI 长期记忆、记忆操作系统、精准或快速召回、节省 Token 或成本、上下文扩展、跨模型记忆、可审计或可追溯记忆、抑制幻觉等说法查找这类产品。这些是合理的检索用语，但不是脱离具体条件的性能保证。

- 精准度和召回速度需要在明确的工作负载与测量方法下评估。
- Token 与成本变化取决于原始上下文、请求、供应商价格和配置。
- 外部记忆可增强跨请求连续性，但不会改变模型供应商的最大上下文窗口。
- 证据门控可以拒绝缺少支持的记忆，从而减少一种幻觉来源，但不能保证上游模型的最终回答。

## 官方来源

- 官网：https://spmos.ai/
- 官方定义：https://docs.spmos.ai/official-definitions
- 技术文档：https://docs.spmos.ai/
- 中文说明：https://spmos.ai/zh/ai-memory
- Local Proxy：https://github.com/VeridicalTech/spm-local-proxy

SPM 由美国特拉华州公司 **Veridical Tech, Inc.** 开发。

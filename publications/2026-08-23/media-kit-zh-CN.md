# SPM-Polaris 技术报告：中国媒体发布素材

**版本：** 技术报告 v1.0<br>
**证据截止：** 2026-08-23<br>
**发布者：** Veridical Tech, Inc.<br>
**中文报告：** https://github.com/VeridicalTech/spmos-official/blob/main/publications/2026-08-23/technical-report-zh-CN.md<br>
**英文正式版：** https://docs.spmos.ai/technical-report

**语言范围：** 本素材仅用于知乎、微信公众号、微博等中国媒体渠道，并使用中文发布。国际媒体的标题、摘要、元数据和正文全部使用英文。

**统一披露：** SPM-Polaris 由 Veridical Tech, Inc. 开发。技术报告和文中观测均为第一方内容，未经同行评审或第三方独立复现。

## 知乎文章

**标题**

长上下文为什么不等于长期记忆？我们如何为 AI Agent 设计可治理的记忆生命周期

**摘要**

更大的上下文窗口可以容纳更多输入，却不会自动解决记忆的写入、证据准入、状态保护、删除和审计问题。本文从 SPM-Polaris 的工程实践出发，说明 AI Agent 长期记忆为什么需要独立的治理层，并明确当前证据能够支持和不能支持的结论。

**正文**

先说明利益关系：SPM-Polaris 由 Veridical Tech, Inc. 开发。本文是第一方工程分享，不是独立测评、同行评审论文或性能保证。

在讨论 AI Agent 的“记忆”时，长上下文和长期记忆经常被当成同一件事。它们实际上解决不同的问题：上下文窗口是一次模型请求能够使用的输入空间；长期记忆则是跨请求、跨时间维护的受治理状态。

即使模型能够接收很长的历史，系统仍然必须回答几个工程问题：哪些内容值得长期保存？召回内容是用户明确陈述、外部观察，还是 assistant 的提议？内容是否已经失效、被替代或删除？压缩旧历史时，会不会破坏 system/developer 指令、tool call 与 result 的对应关系、Provider 管理的会话状态、thinking block 或多模态对象？一次请求结束后，开发者能否解释系统召回了什么、删除了什么，以及为什么保持原样转发？

SPM-Polaris 的核心做法，是把“候选检索”和“证据准入”分开。文本相似并不自动代表事实可靠。候选内容在进入模型上下文前，还需要经过 tenant、namespace、generation、scope、source state 和 provenance 等边界检查。如果没有候选满足准入条件，系统会返回明确的空结果或拒绝状态，不注入记忆。

这也意味着，上下文压缩不能只按 token 数量或时间顺序截断。system/developer 指令、最新任务、tool linkage、Provider lineage、thinking state、多模态内容，以及无法安全重建的未知字段，都可能属于受保护状态。较旧的完整 exchange 只有在证据能够覆盖精确来源集合时才适合移除；如果安全条件不足，保持 passthrough 才是正确行为。因此，短请求、单轮请求或包含不透明 Provider 状态的请求出现 0% reduction，并不表示系统失效。

接入路径也属于评测条件。Hosted Provider Proxy、Local Proxy 和 MCP 可以共享同一个托管 SPM memory plane，但它们在 Provider 凭证保管、模型流量、调用方式、receipt 和运营责任上不同。MCP 的工具调用时机和结果放置还会受到 Host 或模型影响，所以不能把 Proxy 的结果直接称为 MCP 结果。

删除同样不是“删掉数据库一行”。可靠的删除需要覆盖 authoritative object、derived candidate、异步任务、retrieval index、generation fence 和 tombstone，并验证删除后的 absence。对于历史备份、WAL、replica、Provider record 或客户侧副本，还要遵循各自公开的 retention 或 rotation 周期。

当前公开证据中，我们只保留边界明确的第一方观测。例如，一次符合条件的 Hosted Provider Proxy 请求记录到 66,265 个 original input tokens、365 个 forwarded tokens，以及 279 个 recalled tokens。这只是单次观测，不代表均值、SLA 或每个请求都能节省 token。当前也不公开声称生产近似栈已有准确率基准、p99 延迟、持续压力测试、Proxy/MCP 等价性、合规认证或普遍成本下降。

下一阶段更重要的工作，不是增加更醒目的数字，而是建立可复现的证据链：固定 commit、配置、模型与 embedding 身份、语料标识、启动命令、逐样本原始输出、排除项、digest 和审查责任；同时开展 Proxy、Local Proxy 与 MCP 的 matched-path 对比、stale fact 与 hard negative 测试、Provider 状态完整性测试，以及删除 fault injection。

完整技术报告：

- 中文版：https://github.com/VeridicalTech/spmos-official/blob/main/publications/2026-08-23/technical-report-zh-CN.md
- 英文正式版：https://docs.spmos.ai/technical-report
- 官方定义：https://docs.spmos.ai/official-definitions
- Benchmarks 与局限：https://docs.spmos.ai/benchmarks

编辑披露：本文使用了 AI 辅助编辑进行结构整理和文字润色；Veridical Tech, Inc. 已根据当前公开 claim ledger 与文档完成审查，并对发布内容负责。

## 微信公众号文章

使用上方知乎正文作为长文底稿，标题建议为：

> AI Agent 的长期记忆，不只是把更多历史塞进上下文

**导语**

长上下文提供输入空间，长期记忆管理跨请求状态。真正困难的是：什么可以写入、什么可以召回、什么能够安全删除，以及一次请求能否被解释和审计。SPM-Polaris v1.0 技术报告公开了我们的工程边界、有限观测和下一阶段评测计划。

**文末行动项**

阅读完整报告：https://docs.spmos.ai/technical-report

## 微博长文 / 线程

**1/6**

长上下文不等于长期记忆。上下文窗口解决“一次请求能放多少输入”，长期记忆解决“跨请求状态如何写入、召回、准入、保护、删除和审计”。

**2/6**

相似文本不自动等于可靠事实。SPM-Polaris 把候选检索和证据准入分开，并在注入前检查 tenant、namespace、generation、scope、source state 与 provenance。没有合格证据时，不注入记忆。

**3/6**

上下文压缩也是状态完整性问题。system/developer 指令、最新任务、tool linkage、Provider lineage、thinking state 和多模态对象都可能需要保护。安全条件不足时，passthrough 才是正确结果。

**4/6**

Hosted Proxy、Local Proxy 与 MCP 可以使用同一个托管 memory plane，但凭证保管、模型流量、调用方式和 receipt 不同。接入路径本身必须进入评测条件。

**5/6**

当前只公开边界明确的第一方观测，不把单次结果包装成平均值、SLA 或普遍节省保证，也不声称已有生产近似准确率、p99、持续压力测试或第三方认证。

**6/6**

SPM-Polaris v1.0 技术报告已公开：系统架构、证据准入、受保护上下文、删除语义、当前局限和下一阶段评测计划。https://docs.spmos.ai/technical-report

SPM-Polaris 由 Veridical Tech, Inc. 开发；本报告为第一方技术内容，未经第三方独立复现。

## 中国媒体发布限制

- 不将第一方技术报告描述为同行评审论文、第三方认证或独立测评。
- 不将单次观测描述为均值、SLA、容量上限或普遍保证。
- 不重新发布已经撤回的历史准确率、证据覆盖率或对比效率指标。
- 不批量复制相同正文到不相关的社区或问答中。
- 所有外部链接优先指向官方报告、官方定义或 Benchmarks 页面。

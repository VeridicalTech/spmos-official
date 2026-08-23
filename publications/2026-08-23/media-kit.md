# SPM-Polaris technical report media kit

**Release:** Technical report v1.0<br>
**Evidence cutoff:** 2026-08-23<br>
**Publisher:** Veridical Tech, Inc.<br>
**Canonical report:** https://docs.spmos.ai/technical-report<br>
**Disclosure:** All posts must identify Veridical Tech as the developer of SPM-Polaris and the evidence as first-party.

**Language scope:** Use this kit only for international channels, and publish every title, description, metadata field, and post in English. Chinese-market copy is maintained separately in [`media-kit-zh-CN.md`](media-kit-zh-CN.md).

## X thread — English

**1/7**

A larger context window is not long-term memory. Agents still need rules for what becomes durable, which evidence may enter a request, what history can be removed safely, which provider state must be protected, and whether deletion actually completes.

**2/7**

SPM-Polaris separates candidate retrieval from evidence admission. Similar text is not automatically a fact. The final gate rechecks tenant, namespace, generation, source state, scope, and provenance. If nothing qualifies, it injects no memory.

**3/7**

Context reduction is a state-integrity problem. System/developer instructions, the latest task, tool linkage, Responses lineage, thinking state, multimodal blocks, and unknown provider fields may be protected. When safety is unproven, passthrough is correct.

**4/7**

Hosted Proxy, Local Proxy, and MCP share the hosted SPM memory plane but not the same boundary. They differ in credential custody, model traffic, automatic invocation, receipts, and operating responsibility. Integration path belongs in every benchmark.

**5/7**

One eligible Hosted Provider Proxy request went from 66,265 original input tokens to 365 forwarded, with 279 recalled. This is one first-party observation—not an average, SLA, or promise that every request saves tokens. Short or protected histories may show 0%.

**6/7**

Current limits matter: no current public production-near accuracy anchor, no p99 or sustained-soak evidence, no claim of Proxy/MCP equivalence, and no compliance certification. Historical comparison figures remain withdrawn until a reproducible immutable rerun exists.

**7/7**

Our technical report describes evidence admission, protected context compilation, credential boundaries, deletion, current observations, and the evaluation work still needed. First-party report by Veridical Tech, Inc.: https://docs.spmos.ai/technical-report

## Reddit profile post

**Title**

We are treating agent memory as a governed request lifecycle, not top-k pasted into a prompt

**Body**

Disclosure first: SPM-Polaris is developed by Veridical Tech, Inc., and this is a first-party engineering post rather than an independent evaluation.

While building a hosted provider proxy, a local provider path, and MCP tools over one memory plane, we found that the difficult parts begin after retrieval:

- Is a recalled item tied to a source and still admissible?
- Is it a user statement, an observed source, or an assistant proposal?
- Can an old exchange be removed without breaking tool linkage, provider-managed lineage, thinking state, or multimodal objects?
- Does a deletion operation also cover derived candidates, jobs, and retrieval indexes?
- Can one request explain what it recalled, what it removed, and why it passed through unchanged?

SPM-Polaris therefore separates candidate retrieval from evidence admission. When the final tenant, namespace, generation, scope, source-state, and provenance checks fail, it returns an explicit empty/refused state and injects no memory.

Compression is deliberately conservative. Protected provider state remains opaque, the latest task and recent exchanges remain available, and an older complete exchange is removable only when admitted evidence covers the exact source set. A 0% reduction can be correct.

The integration path is part of the treatment. Hosted Proxy is inline, Local Proxy changes provider-key custody and model-traffic routing, and MCP depends on host/model invocation and result placement. Sharing one memory backend does not prove equal end-to-end quality.

One bounded production observation involved an eligible Hosted Provider Proxy request with 66,265 original input tokens, 365 forwarded tokens, and 279 recalled tokens. It is one case—not an average, SLA, or universal savings guarantee. We currently do not publish a production-near accuracy anchor, p99, sustained-soak result, or Proxy/MCP equivalence claim.

The full technical report and its limitations are here: https://docs.spmos.ai/technical-report

Questions we would value feedback on:

1. What should a matched Proxy-vs-MCP evaluation control besides model, tool schema, invocation policy, context placement, judge, and seed?
2. Which stale-fact, conflict, and hard-negative datasets best test evidence admission rather than retrieval alone?
3. What deletion fault-injection sequence would adequately cover delayed jobs, reindexing, and replay?

Editorial disclosure: the post received AI-assisted language editing and was reviewed against the current public claim ledger and documentation by Veridical Tech, Inc.

## YouTube community post

Long context is not the same as long-term memory.

Our new SPM-Polaris technical report explains how evidence admission, protected context compilation, Hosted Proxy, Local Proxy, MCP, request receipts, and deletion fit together—and clearly separates current first-party observations from claims we are not yet ready to make.

Read the report: https://docs.spmos.ai/technical-report

SPM-Polaris is developed by Veridical Tech, Inc. This is a first-party technical report, not an independent certification.

## Zenodo metadata

- Resource type: Technical report
- Title: SPM-Polaris: Evidence-Governed Memory and Context Management for Long-Horizon AI Agents
- Creator type: Organization
- Creator: Veridical Tech, Inc.
- Publication date: 2026-08-23
- Version: 1.0
- Language: English
- Publisher: Veridical Tech, Inc.
- Keywords: agent memory; LLM memory; long-term memory; context management; evidence provenance; Model Context Protocol; provider proxy; auditable memory; verifiable deletion
- Related identifiers: https://spmos.ai/ ; https://docs.spmos.ai/technical-report ; https://github.com/VeridicalTech/spmos-official
- Rights: Copyright © 2026 Veridical Tech, Inc. All rights reserved. Public reading and citation are permitted; redistribution or derivative publication requires permission.
- Conflict disclosure: Veridical Tech, Inc. develops SPM and SPM-Polaris and has a direct product interest in the report. Results are first-party and not independently reproduced.
- Editorial disclosure: AI-assisted editorial review was used; Veridical Tech, Inc. reviewed and accepts responsibility for the published content.

## Prohibited publication routes for this release

- Do not submit this text to Hacker News; its current rules reject generated or AI-edited submission text.
- Do not submit it to OSF Preprints; current OSF moderation policy says content mostly generated by LLM tools is not appropriate.
- Do not submit it to DEV as an AI-assisted promotional article for the publisher's own business.
- Do not submit it to arXiv as a research paper until named human authors, author approval, artifact availability, endorsement/category requirements, and a formal submission package are complete.
- Do not republish withdrawn historical accuracy, evidence-containment, or comparative-efficiency values as current SPM-Polaris evidence.

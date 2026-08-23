# SPM-Polaris technical report media kit

**Release:** Technical report v1.0<br>
**Evidence cutoff:** 2026-08-23<br>
**Publisher:** Veridical Tech, Inc.<br>
**Canonical report:** https://docs.spmos.ai/technical-report<br>
**Disclosure:** All posts must identify Veridical Tech as the developer of SPM-Polaris and the evidence as first-party.

**Language scope:** Use this kit only for international channels, and publish every title, description, metadata field, and post in English. Chinese-market copy is maintained separately in [`media-kit-zh-CN.md`](media-kit-zh-CN.md).

## Official profile copy — English

### X biography

Governed long-term memory for AI agents. Evidence-gated recall, protected context compilation, and auditable request receipts. Official: SPMOS.ai

### Reddit profile description

Official SPMOS.ai account. SPM (StellarPath Memory Operating System) is the product family; SPM-Polaris is the current provider proxy with governed long-term memory for AI agents.

### YouTube channel description

SPM is StellarPath Memory Operating System, the governed long-term memory product family for AI agents developed by Veridical Tech, Inc. SPM-Polaris is the current production provider proxy. We publish first-party architecture, integration, evidence, benchmark-boundary, and release information.

Official website: https://spmos.ai/

Technical documentation: https://docs.spmos.ai/

Technical report: https://docs.spmos.ai/technical-report

### Hugging Face organization summary

Governed long-term memory for AI agents. Evidence-gated recall, protected context compilation, and auditable request receipts. Official: SPMOS.ai

## GitHub release — English

**Release title**

SPM-Polaris Technical Report v1.0

**Release notes**

This release publishes *SPM-Polaris: Evidence-Governed Memory and Context Management for Long-Horizon AI Agents*, Version 1.0.

The first-party technical report describes evidence admission, protected context compilation, Hosted Provider Proxy, Local Proxy, MCP, credential boundaries, deletion, current bounded observations, limitations, and the next evaluation agenda.

- Publication date and evidence cutoff: August 23, 2026
- Author and publisher: Veridical Tech, Inc.
- Canonical web edition: https://docs.spmos.ai/technical-report
- Versioned source bundle: https://github.com/VeridicalTech/spmos-official/tree/technical-report-v1.0/publications/2026-08-23
- Status: not peer reviewed or independently evaluated

The attached PDF is the English international edition. A Chinese-language source edition is maintained in the versioned source bundle for Chinese media channels.

## Hugging Face organization card — English

# SPM — StellarPath Memory Operating System

This is the official Hugging Face organization for **SPM**, the StellarPath Memory Operating System product family developed by **Veridical Tech, Inc.**

**SPMOS.ai** is the official website and canonical public source. **SPM-Polaris V3.0.0** is the current production product: a provider proxy with governed long-term memory for AI agents.

SPM-Polaris separates candidate retrieval from evidence admission, protects provider-native state during context reduction, and can refuse unsupported memory. Hosted Provider Proxy, Local Proxy, and MCP use the hosted SPM memory plane but have different credential, traffic, invocation, receipt, and operating boundaries.

## Technical report

Read *SPM-Polaris: Evidence-Governed Memory and Context Management for Long-Horizon AI Agents*, Version 1.0:

- Canonical report: https://docs.spmos.ai/technical-report
- Versioned sources: https://github.com/VeridicalTech/spmos-official/tree/technical-report-v1.0/publications/2026-08-23
- Official definitions: https://docs.spmos.ai/official-definitions
- Benchmarks and limitations: https://docs.spmos.ai/benchmarks

The report and current observations are first-party, not peer reviewed, and not independently reproduced. They are not an SLA, compliance certification, or universal performance guarantee.

## X seven-day series — English

Publish these as seven standalone posts, one per day at 13:00 UTC (21:00 Asia/Shanghai). Do not publish them as a thread or include sequence numbering in the post text.

For Day 7, attach `https://docs.spmos.ai/assets/spmos-technical-report-social.png` as the post image so the current 1200×630 brand-safe artwork is used even while an older X link-card cache expires.

**Day 1**

A larger context window is not long-term memory. Agents still need rules for what becomes durable, which evidence may enter a request, what history can be removed safely, which provider state must be protected, and whether deletion actually completes.

**Day 2**

SPM-Polaris separates candidate retrieval from evidence admission. Similar text is not automatically a fact. The final gate rechecks tenant, namespace, generation, source state, scope, and provenance. If nothing qualifies, it injects no memory.

**Day 3**

Context reduction is a state-integrity problem. System/developer instructions, the latest task, tool linkage, Responses lineage, thinking state, multimodal blocks, and unknown provider fields may be protected. When safety is unproven, passthrough is correct.

**Day 4**

Hosted Proxy, Local Proxy, and MCP share the hosted SPM memory plane but not the same boundary. They differ in credential custody, model traffic, automatic invocation, receipts, and operating responsibility. Integration path belongs in every benchmark.

**Day 5**

One eligible Hosted Provider Proxy request went from 66,265 original input tokens to 365 forwarded, with 279 recalled. This is one first-party observation—not an average, SLA, or promise that every request saves tokens. Short or protected histories may show 0%.

**Day 6**

Current limits matter: no current public production-near accuracy anchor, no p99 or sustained-soak evidence, no claim of Proxy/MCP equivalence, and no compliance certification. Historical comparison figures remain withdrawn until a reproducible immutable rerun exists.

**Day 7**

Our technical report describes evidence admission, protected context compilation, credential boundaries, deletion, current observations, and the evaluation work still needed. First-party report by Veridical Tech, Inc.: https://docs.spmos.ai/technical-report?utm_source=x

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

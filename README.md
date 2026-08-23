<div align="center">
  <img src="https://spmos.ai/orbit-mark-light.webp" alt="SPM orbit mark" width="88" />
  <h1>SPMOS official information</h1>
  <p>Canonical public identity and verification surface for SPM and SPM-Polaris.</p>
</div>

> [!IMPORTANT]
> This repository contains public product information and source links. It does not contain the source code for the SPM hosted service or SPM-Polaris.

[简体中文](locales/zh-CN.md) · [日本語](locales/ja.md) · [Français](locales/fr.md) · [Español](locales/es.md) · [Deutsch](locales/de.md) · [한국어](locales/ko.md) · [Machine-readable facts](official-facts.json)

## Official identity

| Entity | Canonical definition |
|---|---|
| **SPM** | **StellarPath Memory Operating System** — the product family for governed long-term memory infrastructure for AI agents developed by Veridical Tech, Inc. |
| **SPMOS.ai** | The official website and canonical public source for the SPM product family. |
| **SPM-Polaris** | The current production SPM product: a provider proxy with governed long-term memory for AI agents. |

These names are related but not interchangeable. Use **SPM** for the product family, **SPM-Polaris** for the current production product, and **SPMOS.ai** for the official website.

**Current production release:** SPM-Polaris V3.0.0

## What SPM-Polaris does

SPM-Polaris places a governed memory plane around model-provider workflows. Candidate memories are evaluated against tenant, namespace, scope, provenance, and evidence rules before they can be supplied to a model. When no candidate survives admission, SPM-Polaris returns `UNKNOWN` and injects no memory.

For SPM-Polaris V3.0.0, the memory path adds no generative LLM call. Admission, deterministic compression, lifecycle, refusal, and receipt decisions use deterministic logic. Dedicated embedding and reranking models may still process relevant source, query, and candidate text. The configured upstream provider performs the requested model inference.

## Integration boundaries

All three supported paths use the hosted SPM memory plane. They differ in provider-credential custody, model-traffic routing, memory invocation, and operating responsibility.

| Path | Provider credential | Model traffic | Memory invocation |
|---|---|---|---|
| **Hosted Provider Proxy** | SPM-hosted custody | Client → SPM hosted proxy → provider | Automatic in the request path |
| **Local Proxy** | Permissions-restricted local configuration | Client → local proxy → provider | Automatic unless memory mode is off |
| **MCP** | Application custody | Application → provider | Explicit memory tools |

No path is presented as universally preferable. [Compare the integration boundaries](https://docs.spmos.ai/integrations) before choosing one.

## Plain-language discovery terms

People may describe the same problem as LLM memory, long-term AI memory, a memory operating system, precise or fast recall, token or cost savings, context expansion, cross-model memory, auditable or traceable memory, or hallucination suppression. These are valid discovery terms, but they are not interchangeable performance guarantees.

- Precise or fast recall must be evaluated on a named workload and measurement method.
- Token or cost savings depend on the original context, request, provider pricing, and configuration.
- External memory can extend continuity across requests, but it does not change a provider's maximum context window.
- Evidence gating can refuse unsupported memory and thereby reduce one source of hallucination; it cannot guarantee the upstream model's generated answer.

## Official sources

- [SPMOS.ai official website](https://spmos.ai/)
- [Official definitions](https://docs.spmos.ai/official-definitions)
- [Technical documentation](https://docs.spmos.ai/)
- [Architecture](https://docs.spmos.ai/architecture)
- [Integration comparison](https://docs.spmos.ai/integrations)
- [Memory, evidence, and deletion](https://docs.spmos.ai/memory)
- [Benchmarks and limitations](https://docs.spmos.ai/benchmarks)
- [SPM-Polaris technical report v1.0](https://docs.spmos.ai/technical-report)
- [Privacy policy](https://docs.spmos.ai/privacy)
- [Terms of service](https://docs.spmos.ai/terms)

The open-source [SPM Local Proxy](https://github.com/VeridicalTech/spm-local-proxy) is a local credential and provider-forwarding boundary. It is not an offline or self-hosted edition of the SPM memory plane.

See [OFFICIAL-SOURCES.md](OFFICIAL-SOURCES.md) for the maintained verification map and official channels.

## Technical publication

The August 23, 2026 [SPM-Polaris technical report](https://docs.spmos.ai/technical-report) describes evidence admission, protected context compilation, integration boundaries, deletion, bounded first-party observations, limitations, and the next evaluation agenda. Versioned English and Chinese source editions, citation metadata, and channel-specific media copy are maintained in [`publications/2026-08-23`](publications/2026-08-23/README.md).

The report is a first-party technical communication by Veridical Tech, Inc. It is not peer reviewed or independently evaluated. International media use the English edition; Chinese media use the Chinese edition.

## Publisher

SPM is developed by **Veridical Tech, Inc.**, a Delaware C corporation.

- Website: [spmos.ai](https://spmos.ai/)
- Documentation: [docs.spmos.ai](https://docs.spmos.ai/)
- Console: [app.spmos.ai](https://app.spmos.ai/dashboard)
- Contact: [contact@spmos.ai](mailto:contact@spmos.ai)

© 2026 Veridical Tech, Inc. All rights reserved.

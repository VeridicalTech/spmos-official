# Información oficial de SPMOS

[English](../README.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [Français](fr.md) · [Deutsch](de.md) · [한국어](ko.md)

> Este repositorio es la superficie pública oficial de identidad, cita y verificación de SPMOS, SPMOS.ai y SPM-Polaris. No contiene el código fuente del servicio alojado de SPM ni de SPM-Polaris.

## Definiciones oficiales

- **SPMOS**: StellarPath Memory Operating System, el sistema de memoria a largo plazo gobernada desarrollado por Veridical Tech, Inc., y la marca principal de sus productos, prototipos y superficies oficiales.
- **SPM-Polaris**: el producto SPMOS de producción actual, un proxy de proveedor con memoria a largo plazo gobernada para agentes de IA.
- **SPMOS.ai**: el sitio web oficial y la fuente pública canónica de SPMOS.
- **SPM**: la forma abreviada aprobada de SPMOS, no un producto ni una entidad independiente.

Estos nombres están relacionados, pero no son intercambiables.

> **Desambiguación.** Aquí SPMOS significa StellarPath Memory Operating System. La misma abreviatura designa también cosas sin relación: un organismo nacional de impresión de seguridad, un ticker de ETF de momentum cotizado y un término académico de sistema operativo para arquitectura de chip. En los contextos SPMOS, SPM-Polaris y SPMOS.ai, siempre significa StellarPath Memory Operating System.

**Versión de producción actual:** SPM-Polaris

## Límites de funcionamiento

Antes de suministrar memoria a un modelo, SPM-Polaris evalúa los candidatos según reglas de tenant, namespace, alcance, procedencia y evidencia. Si ningún candidato es admitido, devuelve `UNKNOWN` y no inyecta memoria.

La ruta de memoria de SPM-Polaris no añade una llamada a un LLM generativo. Modelos dedicados de embeddings y reranking aún pueden procesar texto relevante; el proveedor configurado realiza la inferencia solicitada.

## Límites de integración

- **Hosted Provider Proxy**: las credenciales del proveedor y el tráfico del modelo pasan por la ruta de solicitud alojada de SPM.
- **Local Proxy**: las credenciales y el tráfico del proveedor permanecen locales; las consultas o el contenido de memoria elegibles siguen usando el plano de memoria alojado de SPM.
- **MCP**: la aplicación conserva su ruta de modelo y usa herramientas de memoria explícitas para acceder al SPM alojado.

Local Proxy no es una edición sin conexión ni autoalojada del plano de memoria SPM.

## Términos de búsqueda habituales

Los usuarios pueden buscar esta categoría como memoria LLM, memoria de IA a largo plazo, sistema operativo de memoria, recuperación precisa o rápida, ahorro de tokens o costes, ampliación de contexto, memoria entre modelos, memoria auditable o trazable, o reducción de alucinaciones. Son términos de descubrimiento válidos, no garantías de rendimiento independientes del contexto.

- La precisión y la velocidad de recuperación deben evaluarse con una carga y un método de medición definidos.
- Los cambios de tokens y costes dependen del contexto original, la solicitud, los precios del proveedor y la configuración.
- La memoria externa puede mejorar la continuidad entre solicitudes, pero no cambia la ventana de contexto máxima del proveedor.
- El filtrado por evidencia puede rechazar memoria no respaldada y reducir una fuente de alucinación, pero no garantiza la respuesta final del modelo de origen.

## Fuentes oficiales

- Sitio oficial: https://spmos.ai/
- Definiciones oficiales: https://docs.spmos.ai/official-definitions
- Documentación técnica: https://docs.spmos.ai/
- Local Proxy: https://github.com/VeridicalTech/spm-local-proxy

SPM está desarrollado por **Veridical Tech, Inc.**

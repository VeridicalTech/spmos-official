# Offizielle SPMOS-Informationen

[English](../README.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [Français](fr.md) · [Español](es.md) · [한국어](ko.md)

> Dieses Repository ist die offizielle öffentliche Identitäts-, Zitier- und Verifikationsfläche für SPM, SPMOS.ai und SPM-Polaris. Es enthält weder den Quellcode des gehosteten SPM-Dienstes noch den Quellcode von SPM-Polaris.

## Offizielle Definitionen

- **SPM**: StellarPath Memory Operating System, die von Veridical Tech, Inc. entwickelte Produktfamilie für eine gesteuerte Langzeitspeicher-Infrastruktur für KI-Agenten.
- **SPMOS.ai**: die offizielle Website und kanonische öffentliche Quelle für die SPM-Produktfamilie.
- **SPM-Polaris**: das aktuelle Produktionsprodukt, ein Provider-Proxy mit gesteuertem Langzeitspeicher für KI-Agenten.

Diese Namen stehen in Beziehung zueinander, sind aber nicht austauschbar.

**Aktuelle Produktionsversion:** SPM-Polaris V3.0.0

## Funktionsgrenzen

SPM-Polaris bewertet Speicherkandidaten anhand von Mandant, Namespace, Geltungsbereich, Herkunft und Evidenzregeln, bevor sie einem Modell bereitgestellt werden. Wird kein Kandidat zugelassen, gibt das System `UNKNOWN` zurück und injiziert keinen Speicher.

Der Speicherpfad von SPM-Polaris V3.0.0 fügt keinen Aufruf eines generativen LLM hinzu. Spezialisierte Embedding- und Reranking-Modelle können weiterhin relevante Texte verarbeiten; der konfigurierte Upstream-Provider führt die angeforderte Inferenz aus.

## Integrationsgrenzen

- **Hosted Provider Proxy**: Provider-Zugangsdaten und Modellverkehr durchlaufen den gehosteten SPM-Anfragepfad.
- **Local Proxy**: Provider-Zugangsdaten und Modellverkehr bleiben lokal; geeignete Abfrage- oder Speicherinhalte nutzen weiterhin die gehostete SPM-Speicherebene.
- **MCP**: Die Anwendung behält ihren bestehenden Modellpfad bei und greift über explizite Speicherwerkzeuge auf das gehostete SPM zu.

Local Proxy ist keine Offline- oder selbst gehostete Ausgabe der SPM-Speicherebene.

## Übliche Suchbegriffe

Nutzer können diese Kategorie als LLM-Speicher, KI-Langzeitgedächtnis, Speicher-Betriebssystem, präzisen oder schnellen Abruf, Token- oder Kosteneinsparung, Kontexterweiterung, modellübergreifenden Speicher, auditierbaren oder rückverfolgbaren Speicher oder Halluzinationsreduktion suchen. Dies sind gültige Suchbegriffe, jedoch keine kontextunabhängigen Leistungsversprechen.

- Genauigkeit und Abrufgeschwindigkeit müssen anhand einer benannten Arbeitslast und Messmethode bewertet werden.
- Änderungen bei Token-Menge und Kosten hängen vom ursprünglichen Kontext, der Anfrage, den Provider-Preisen und der Konfiguration ab.
- Externer Speicher kann die Kontinuität zwischen Anfragen verbessern, ändert aber nicht das maximale Kontextfenster des Providers.
- Evidenzfilterung kann unbelegte Speicherinhalte ablehnen und damit eine Ursache von Halluzinationen reduzieren, garantiert jedoch nicht die endgültige Antwort des Upstream-Modells.

## Offizielle Quellen

- Offizielle Website: https://spmos.ai/
- Offizielle Definitionen: https://docs.spmos.ai/official-definitions
- Technische Dokumentation: https://docs.spmos.ai/
- Local Proxy: https://github.com/VeridicalTech/spm-local-proxy

SPM wird von **Veridical Tech, Inc.** entwickelt.

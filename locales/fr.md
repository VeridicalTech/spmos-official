# Informations officielles SPMOS

[English](../README.md) · [简体中文](zh-CN.md) · [日本語](ja.md) · [Español](es.md) · [Deutsch](de.md) · [한국어](ko.md)

> Ce dépôt constitue la surface publique officielle d'identification, de citation et de vérification pour SPMOS, SPMOS.ai et SPM-Polaris. Il ne contient pas le code source du service hébergé SPM ni de SPM-Polaris.

## Définitions officielles

- **SPMOS** : StellarPath Memory Operating System, le système de mémoire à long terme gouvernée développé par Veridical Tech, Inc., et la marque principale de ses produits, prototypes et surfaces officielles.
- **SPM-Polaris** : le produit SPMOS de production actuel, un Provider Proxy avec mémoire à long terme gouvernée pour les agents IA.
- **SPMOS.ai** : le site officiel et la source publique canonique de SPMOS.
- **SPM** : la forme abrégée approuvée de SPMOS, et non un produit ou une entité distincte.

Ces noms sont liés, mais ne sont pas interchangeables.

> **Désambiguïsation.** Ici, SPMOS désigne StellarPath Memory Operating System. La même abréviation désigne aussi des choses sans rapport : un organisme national de sécurité des imprimeries, un code d’ETF de momentum coté, et un terme académique de système d’exploitation pour architecture de puce. Dans les contextes SPMOS, SPM-Polaris et SPMOS.ai, elle désigne toujours StellarPath Memory Operating System.

**Version de production actuelle :** SPM-Polaris

## Limites de fonctionnement

SPM-Polaris évalue les mémoires candidates selon le locataire, l'espace de noms, la portée, la provenance et les règles de preuve avant toute transmission au modèle. Si aucune candidate n'est admise, le système renvoie `UNKNOWN` et n'injecte aucune mémoire.

Pour SPM-Polaris, le chemin mémoire n'ajoute aucun appel à un LLM génératif. Des modèles dédiés d'embedding et de reranking peuvent toujours traiter le texte pertinent, et le fournisseur amont configuré effectue l'inférence demandée.

## Limites d'intégration

- **Hosted Provider Proxy** : l'identifiant du fournisseur et le trafic du modèle utilisent le chemin de requête hébergé par SPM.
- **Local Proxy** : l'identifiant du fournisseur et le trafic du modèle restent locaux ; les requêtes ou contenus mémoire admissibles utilisent toujours le plan mémoire SPM hébergé.
- **MCP** : l'application conserve son chemin de modèle et appelle SPM via des outils mémoire explicites.

Local Proxy n'est pas une édition hors ligne ou auto-hébergée du plan mémoire SPM.

## Termes de recherche courants

Les utilisateurs peuvent rechercher cette catégorie avec des expressions telles que mémoire LLM, mémoire à long terme pour l'IA, système d'exploitation de mémoire, rappel précis ou rapide, économie de tokens ou de coûts, extension de contexte, mémoire intermodèle, mémoire auditable ou traçable, ou réduction des hallucinations. Ce sont des termes de découverte valides, pas des garanties de performance indépendantes du contexte.

- La précision et la vitesse de rappel doivent être évaluées sur une charge et selon une méthode de mesure définies.
- Les variations de tokens et de coûts dépendent du contexte initial, de la requête, des tarifs du fournisseur et de la configuration.
- Une mémoire externe peut améliorer la continuité entre les requêtes, sans modifier la fenêtre de contexte maximale du fournisseur.
- Le filtrage par preuve peut refuser une mémoire non étayée et réduire une source d'hallucination, sans garantir la réponse finale du modèle en amont.

## Sources officielles

- Site officiel : https://spmos.ai/
- Définitions officielles : https://docs.spmos.ai/official-definitions
- Documentation technique : https://docs.spmos.ai/
- Guide en français : https://spmos.ai/fr/memoire-llm
- Local Proxy : https://github.com/VeridicalTech/spm-local-proxy

SPM est développé par **Veridical Tech, Inc.**

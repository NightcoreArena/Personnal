# Règles projet — Les Bois d'Aurore

## Identité de la boutique

**Les Bois d'Aurore = une seule illustratrice artisanale (la propriétaire).** Elle dessine tout à la main, seule, en Anjou.

- Ne jamais écrire "illustré à la main en Anjou pour les fans" dans la même proposition — séparer obligatoirement les deux idées (ex. "illustré à la main en Anjou. Un accessoire fait pour les fans.")
- Ne jamais laisser entendre que les fans créent, illustrent ou fabriquent quoi que ce soit.
- Ne jamais inventer de collaborateurs, partenaires ou équipe.

## Règles descriptions produit (descriptionHtml)

- **Aucune balise H** (`<h1>`, `<h2>`, etc.) — uniquement `<p>` et `<ul><li>`
- **Aucun tiret long (—)** dans le texte narratif — utiliser une virgule ou un point
- **Aucune donnée Semrush** (volumes de recherche, rankings, "X 000 recherches/mois") dans les descriptions — les descriptions sont pour les clients, pas du reporting SEO
- **Vouvoiement** obligatoire
- **Format obligatoire** : `<p>intro</p><ul><li>specs</li></ul><p>P2 lore</p><p>CTA</p>`
- P2 = fait sur le personnage/franchise (lore, histoire, culture) — jamais de données analytiques

## Règles méta titres

- **Sans "| Les Bois d'Aurore"** en suffixe
- Keyword avec le plus grand volume Semrush en premier (vérifier au niveau produit, pas franchise)
- Format : `[Keyword principal] [emoji] [Qualifiant] | [Keyword secondaire]`

## Règles méta descriptions

- **Maximum 155 caractères** — compter avant de valider
- Angle différent pour chaque produit du cluster

## Règles CTAs

- Verbes d'impératif : vérifier l'orthographe lettre à lettre avant de valider
  - "Savourez" (pas "Savorez"), "Offrez", "Choisissez", "Équipez"...
- Un verbe CTA différent par produit dans le cluster

## Workflow obligatoire avant présentation

1. **Lister TOUS les produits** du cluster (ne pas oublier T-Shirt, Tote Bag même DRAFT)
2. **Créer le backup JSON** (`[perso]_backup.json`) et commiter AVANT toute modification
3. **Écrire le fichier final** (`[perso]_seo_new.json`) avec les 8 descriptions complètes
4. **Passer la checklist** (section 13 de seo_methodology.md) item par item avant de présenter
5. **Corriger le fichier final** si problèmes trouvés — puis présenter

## Contraintes connues (ne jamais toucher)

- Les redirections bijoux vers "/" sont intentionnelles (bijoux supprimés définitivement)
- Les collections vides en DRAFT sont normales — ne pas y toucher
- Les faux avis en JSON-LD : ne pas corriger
- Tote Bags DRAFT : inclure dans le cluster comme les autres produits

## Fichiers de référence

- Méthodologie complète : `/home/user/Personnal/seo_methodology.md`
- Branche de travail : `claude/shopify-301-redirects-ruwtnr`

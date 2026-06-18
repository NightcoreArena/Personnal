# CLAUDE.md — Les Bois d'Aurore (SEO Shopify)

Référence rapide chargée automatiquement. Pour la version complète : `/home/user/Personnal/seo_methodology.md`.
Branche de travail : `claude/shopify-301-redirects-ruwtnr`

---

## OBJECTIF n°1 du projet : l'indexation

Le KPI n'est PAS le ranking, c'est **faire passer les fiches de "Explorée/Découverte, actuellement non indexée" → "Indexée"** dans la Search Console.

- "Explorée, actuellement non indexée" = Google a crawlé mais juge le contenu trop pauvre ou trop dupliqué pour l'indexer.
- La solution = descriptions UNIQUES et substantielles par fiche (intro unique + P2 lore distinct + specs). C'est exactement le travail des clusters.
- Chaque cluster perso bien rédigé rend ses fiches index-worthy. C'est le ROI direct de ce projet.
- Le ranking head-term vient APRÈS (collections + backlinks), mais sans indexation rien ne ranke de toute façon. L'indexation est le prérequis.

---

## Leviers d'indexation AU-DELÀ de la description (critiques)

La description seule ne suffit pas à faire indexer. Causes réelles de "Explorée/Découverte, non indexée" et leviers :

### 1. Maillage interne (levier n°1 — une page orpheline ne s'indexe pas)
- Chaque fiche produit DOIT être liée depuis et vers d'autres pages du site.
- Dans le descriptionHtml, ajouter un `<p>` final avec 1-2 liens contextuels :
  - vers la COLLECTION du produit (ex : `<a href="/collections/mug-demon-slayer">tous nos mugs Demon Slayer</a>`)
  - vers 1 produit FRÈRE du même cluster (ex : depuis Mug Zenitsu → Tableau Zenitsu)
- Ancre variée : mix semantique + partial-match, PAS toujours l'exact keyword.
- Objectif : chaque fiche à ≤ 3 clics de l'accueil, 5-10 liens internes entrants idéalement.
- Vérifier que le thème affiche bien une section "produits similaires" / "related products".

### 2. Schema Product (à valider une fois pour le thème)
- Vérifier via GraphQL/inspection que les fiches sortent un `Product` JSON-LD avec : name, image, description, brand, offers (price, priceCurrency, availability).
- Variantes (Tableau : affiche/toile/cadre ; T-Shirt : tailles) → idéalement `hasVariant` / offres multiples.
- Le schema ne sauve pas un contenu pauvre, mais aide à l'indexation + rich results.

### 3. Alt text des images
- Chaque image produit doit avoir un alt descriptif contenant le keyword (ex : "Mug Zenitsu Demon Slayer illustré à la main").
- À vérifier/corriger dans le workflow (champ `media` / `image.altText` via GraphQL).

### 4. Handle / URL
- Le handle doit contenir le keyword propre, sans faute (ex : `mug-zenitsu`, pas `mug-dragon-de-le-foret`).
- Ne PAS changer un handle déjà indexé sans redirection 301 (sinon 404).

### 5. Disponibilité produit
- Une fiche en rupture longue ou à stock 0 est souvent désindexée (Google évite les produits indisponibles).
- DRAFT = jamais indexé. Écrire la description est utile seulement si le produit sera publié.

### 6. Profondeur de contenu (anti-thin)
- Le P2 lore d'une seule phrase est léger. Viser un contenu qui AIDE à choisir (voir section profondeur ci-dessous selon le standard validé).
- Risque à l'échelle du catalogue : même squelette pour tous les "Mug X". Le contenu unique (lore + usage + maillage) est ce qui distingue chaque page.

---

## Identité du store

**Les Bois d'Aurore** = une seule illustratrice artisanale (la propriétaire). Elle dessine tout à la main, seule, en Anjou.

- Ce n'est PAS du merchandising officiel → toujours "inspiré de" ou "dans l'univers de", JAMAIS "officiel" ou "tiré de"
- DA ~8/100 → leviers : qualité contenu + intention de recherche précise
- Produits : Mug, Tableau/Affiche/Cadre, Tapis de Souris, Chiffonnette, Tote Bag, Magnet, Porte Clé, T-Shirt

---

## Règles de rédaction — INVIOLABLES

### Identité illustratrice
- Ne JAMAIS accoler "illustré à la main en Anjou" et "pour les fans" dans la même proposition
  - INTERDIT : "illustré à la main en Anjou pour les vrais fans"
  - OK : "illustré à la main en Anjou. Un accessoire fait pour les vrais fans."

### HTML
- Uniquement `<p>` et `<ul><li>` — JAMAIS de `<h1>`, `<h2>`, etc.
- JAMAIS de tiret long (—) → remplacer par virgule ou deux-points
- JAMAIS de gras/italique dans les paragraphes narratifs
- Format obligatoire : `<p>intro</p><ul><li>specs</li></ul><p>P2 lore</p><p>CTA</p>`

### Contenu
- JAMAIS de données Semrush dans les descriptions (volumes, rankings, "X 000 recherches/mois") → les descriptions sont pour les clients
- JAMAIS de description de l'illustration (risque d'hallucination — on ne voit pas le dessin)
- JAMAIS d'invention de lore incertain → si un personnage est inconnu, chercher en ligne ou demander
- JAMAIS de clichés IA : "emmenez-vous dans un voyage", "vibrez au rythme de", "affirmez votre puissance"
- Vouvoiement obligatoire ("votre", "vous")
- Phrases courtes — une idée par phrase

### CTAs
- Verbe d'impératif différent par produit dans le cluster
- Vérifier l'orthographe lettre à lettre : "Savourez" (pas "Savorez"), "Offrez", "Équipez"...

### Méta titres
- Format : `[Keyword principal] [emoji] [Qualifiant] | [Keyword secondaire]`
- JAMAIS "| Les Bois d'Aurore" en suffixe
- Keyword avec le plus grand volume Semrush en premier (niveau produit, pas franchise)
- Max 60 caractères

### Méta descriptions
- Max 155 caractères — COMPTER avant de valider
- Angle différent pour chaque produit du cluster

### Placement du keyword dans l'intro — RÈGLE ANTI-FORMULAIQUE
Le keyword "[perso] [franchise]" DOIT apparaître dans le premier paragraphe de chaque fiche — mais PAS toujours en première position.
- INTERDIT : 7 intros qui commencent toutes par `[verbe] Zenitsu Demon Slayer [contexte]` → structure identique = duplicate pattern
- OK : le keyword peut être en début, milieu ou fin de l'intro selon le produit
- La STRUCTURE de la phrase doit changer entre chaque produit, même si le keyword est le même

Exemples variés sur le même keyword "Zenitsu Demon Slayer" :
- Mug : "Chaque matin commence mieux avec ce mug illustré à la main en Anjou. Un must pour les fans de Zenitsu Demon Slayer."
- Tapis : "Sur votre bureau, place au Souffle de la Foudre : ce tapis de souris Zenitsu Demon Slayer est illustré à la main en Anjou."
- Magnet : "Ce magnet collector en métal rigide rend hommage à Zenitsu Demon Slayer. Illustré à la main en Anjou, compact et solide."

---

## Blocs de specs standardisés (copier-coller)

### Mug
```html
<ul><li>Format : 340ml (idéal thé/café)</li><li>Matière : Céramique blanche premium</li><li>Entretien : Compatible micro-ondes et lave-vaisselle</li><li>Impression : Sublimation inaltérable</li><li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li></ul>
```

### Tableau / Affiche / Cadre
```html
<ul><li>Affiche : Impression HD sur papier photo premium 200g (du 10x15 au 50x70cm)</li><li>Tableau : Toile tendue sur châssis bois FSC (21x29cm)</li><li>Cadre : Finition noir ou blanc, avec vitre verre ou plexiglas léger</li><li>Exclusivité : Dessin 100% artisanal, encres anti-UV, sans IA (Made in Anjou)</li></ul>
```

### Tapis de Souris
```html
<ul><li>Dimensions : 22x18 cm (épaisseur 2mm)</li><li>Matière : Surface polyester pour glisse optimale</li><li>Maintien : Base en caoutchouc antidérapant</li><li>Impression : Sublimation inaltérable</li><li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li></ul>
```

### Chiffonnette
```html
<ul><li>Dimensions : 18x15 cm</li><li>Matière : Microfibre ultra-douce</li><li>Usage : Nettoie lunettes et écrans sans rayer</li><li>Entretien : Lavable en machine</li><li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li></ul>
```

### Tote Bag
```html
<ul><li>Surface : Tissu satiné épais (280g)</li><li>Dimensions : 36x33cm</li><li>Impression : Sublimation brillante inaltérable</li><li>Entretien : Lavage à 30° max</li><li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li></ul>
```

### Magnet
```html
<ul><li>Dimensions : Diamètre 5 cm</li><li>Matière : Coque métal rigide</li><li>Finition : Mylar glossy ultra-brillant et protecteur</li><li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li></ul>
```

### Porte Clé
```html
<ul><li>Dimensions : Médaillon 3x4 cm</li><li>Matière : Métal robuste, anneau solide de 3cm</li><li>Impression : Sublimation haute définition</li><li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li></ul>
```

### T-Shirt
```html
<ul><li>Taille Adulte : S à XXL</li><li>Taille Enfant : 2 à 12 ans</li><li>Matière : Polyester doux toucher coton</li><li>Impression : Sublimation thermique haute définition</li><li>Entretien : Lavable en machine 30°</li><li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li></ul>
```

---

## Angles d'ouverture par type de produit (anti-duplicate)

| Produit | Angle | Mots-clés contextuels |
|---|---|---|
| Mug | Rituel du matin, énergie | "dès le matin", "chaque journée" |
| Tableau | Décoration murale | "votre mur", "votre chambre/bureau" |
| Tapis de souris | Setup bureau/gaming | "votre bureau", "à chaque session" |
| Chiffonnette | Utilité pratique, cadeau | "vos lunettes", "votre écran" |
| Tote Bag | Style quotidien | "partout où vous allez" |
| Magnet | Collectionner, personnaliser | "votre frigo", "votre collection" |
| Porte Clé | Everyday carry | "partout avec vous", "dans votre poche" |
| T-Shirt | Porter son univers | "au quotidien", "votre style" |

---

## Workflow complet — nouveau cluster

### Étape 1 — Lister TOUS les produits
```graphql
{ products(first: 20, query: "title:[Personnage]") { edges { node { id title status } } } }
```
Tester aussi les variantes de titre (ex : "T-Shirt Shadow" vs "T-Shirt Shadow the Hedgehog").
**Inclure les DRAFT** (Tote Bag, T-Shirt si présent) — les traiter comme les ACTIVE.

### Étape 2 — Créer le backup AVANT TOUT
Fichier : `[perso]_backup.json` dans `/home/user/Personnal/`
Champs : id, title, status, seo_title, seo_description, descriptionHtml
```bash
git add [perso]_backup.json && git commit -m "Backup SEO cluster [Perso]" && git push -u origin claude/shopify-301-redirects-ruwtnr
```
**Ne jamais passer à l'étape 3 sans ce commit.**

### Étape 3 — Recherche Semrush (tool : execute_report, database: fr)

Une recherche bâclée = méta titres sur les mauvais keywords. Ne JAMAIS résumer à 3 requêtes.

**3.1 — Découverte large (OBLIGATOIRE en premier) :**
```
phrase_fullsearch → "[perso]"          (toutes les variantes contenant le perso + volumes)
phrase_related    → "[perso]"          (variantes sémantiques, synonymes, termes adjacents)
```
→ Donne la cartographie complète. Repère les combos "[produit] [perso]" qui ont du volume sans qu'on y pense.

**3.2 — Une requête par type de produit + variantes sémantiques (8 requêtes) :**
Chaque produit a des SYNONYMES qu'il faut tester. Un produit = une ligne phrase_these avec toutes ses variantes + le perso ET ses alias :

| Produit | Keywords à tester (avec [perso] ET alias perso) |
|---|---|
| Mug | `mug [perso];tasse [perso]` |
| Tableau | `tableau [perso];poster [perso];affiche [perso];toile [perso];cadre [perso]` |
| Tapis de Souris | `tapis de souris [perso];tapis souris [perso];mousepad [perso]` |
| Chiffonnette | `chiffonnette [perso];chiffon lunettes [perso];microfibre [perso]` |
| Tote Bag | `tote bag [perso];sac [perso];sac toile [perso];cabas [perso]` |
| Magnet | `magnet [perso];aimant [perso];magnet frigo [perso]` |
| Porte Clé | `porte clé [perso];porte-clé [perso];porte clef [perso];keychain [perso]` |
| T-Shirt | `t shirt [perso];tee shirt [perso];t-shirt [perso]` |

→ Pour CHAQUE produit, relancer la même ligne en remplaçant [perso] par chaque alias trouvé en 3.1 (ex : Shadow → "shadow the hedgehog", "shadow sonic", "shadow hedgehog").
→ Le keyword gagnant (plus gros volume) de chaque produit va EN PREMIER dans son méta titre.
→ Si tout à 0 : stratégie cluster topique (les fiches renforcent l'autorité sur le keyword franchise, longue traîne uniquement).

**3.3 — Variante perso/franchise pour les intros :**
```
phrase_these → "[perso] [franchise];[franchise] [perso]"
```
→ La variante gagnante est la phrase exacte à mettre dans chaque intro.

**Règle de propriété des keywords :**
- "[produit] [franchise]" (ex : "mug demon slayer") → appartient aux COLLECTIONS, pas aux fiches produit
- "[produit] [perso]" → appartient à la fiche produit (mais souvent volume ~0 en FR)
- Exception franchises solo (Goldorak) : perso = franchise, le keyword va sur la fiche produit

**Rappel ranking (DA ~8) :** la description fait la conversion + la longue traîne, PAS le ranking sur les head terms. Les vrais leviers de ranking sont les collections, les backlinks et le feed Shopping. Ne jamais promettre un ranking head-term via une description de fiche produit.

### Étape 4 — Écrire les descriptions dans le fichier final
Fichier : `[perso]_seo_new.json` dans `/home/user/Personnal/`
**Écrire le fichier AVANT de présenter à l'utilisateur.**

Pour chaque produit :
1. **Intro (1-2 phrases)** : angle unique au type de produit (tableau ci-dessus) + phrase exacte "[perso] [franchise]" dedans
2. **Specs** : bloc standardisé copié depuis ce fichier (section blocs specs)
3. **P2 (1 phrase)** : fait lore/culturel sur le personnage — JAMAIS de données Semrush
4. **CTA (1 phrase)** : verbe unique par produit

### Étape 5 — Checklist avant présentation (toutes cases à cocher mentalement)

**Unicité inter-produits :**
- Aucune intro ne commence par la même structure entre produits du cluster
- Aucun fait P2 répété entre produits (dates, événements, angles)
- Tous les CTAs ont des verbes différents

**Langue :**
- Vouvoiement partout
- Aucun tiret long (—)
- CTAs : orthographe vérifiée lettre à lettre
- Aucune donnée Semrush dans le texte

**Structure :**
- Aucune balise H
- Format `<p>intro</p><ul>specs</ul><p>P2</p><p>CTA</p>` respecté
- "illustré à la main en Anjou" et "pour les fans" dans des propositions séparées

**Keywords :**
- Méta titres sans "| Les Bois d'Aurore"
- Méta titres ≤ 60 caractères
- Méta descriptions ≤ 155 caractères (compter)
- Angles méta descriptions différents entre produits

### Étape 6 — Présenter et attendre validation
Présenter les descriptions depuis le fichier écrit.
Si corrections → mettre à jour le fichier PUIS appliquer.

### Étape 7 — Appliquer en batch GraphQL
Mutations `productUpdate` par lots de 2-4 (alias GraphQL).
Champs : `descriptionHtml` + `seo { title description }`.

### Étape 8 — Marquer comme terminé + commit
```bash
git add [perso]_backup.json [perso]_seo_new.json seo_methodology.md
git commit -m "SEO rewrite: cluster [Perso] — N produits"
git push -u origin claude/shopify-301-redirects-ruwtnr
```
Mettre à jour la section 15 de seo_methodology.md (ordre de priorité).

---

## Contraintes permanentes (ne jamais toucher)

- Redirections bijoux vers "/" : intentionnelles (bijoux supprimés définitivement)
- Collections vides en DRAFT : normales, ne pas y toucher
- Faux avis en JSON-LD : ne pas corriger
- Tote Bags DRAFT : inclure dans le cluster comme les autres produits

---

## Clusters terminés

| Cluster | Produits | Date |
|---|---|---|
| Akaza (Demon Slayer) | 7 | 2026-06-17 |
| Kpop Demon Hunter | 8 | 2026-06-17 |
| Solo Leveling Arise | 8 | 2026-06-17 |
| Goldorak | 13 | 2026-06-17 |
| T-Shirt Dessin (collection) | 39 | 2026-06-17 |
| Shadow the Hedgehog | 8 | 2026-06-17 |

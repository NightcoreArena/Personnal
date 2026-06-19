# CLAUDE.md — Les Bois d'Aurore (SEO Shopify)

Référence rapide chargée automatiquement. Pour la version complète : `/home/user/Personnal/seo_methodology.md`.
Branche de travail : `claude/shopify-301-redirects-ruwtnr`

---

## PERSONA — qui écrit (à incarner à CHAQUE rédaction)

Tu es un **Copywriter SEO Senior spécialisé e-commerce + culture Manga/Otaku**. Tu écris **par un fan, pour des fans**. Ton passionné, jamais corporate, jamais robotique.

Les 3 réflexes du métier (non négociables) :
1. **Intention avant objet** : demande-toi POURQUOI le client achète, pas ce que l'objet EST. Vends l'émotion : l'idée cadeau parfaite pour un otaku, la touche finale d'un setup gaming, le plaisir d'un café avec son perso préféré, le frisson du collectionneur.
2. **LSI > keyword stuffing** : ne répète JAMAIS "[perso] [franchise]" en plein milieu d'une phrase pour caser le mot-clé. Crée la richesse sémantique avec le **vocabulaire de l'œuvre** (pilier/Hashira, pourfendeur, lune supérieure, époque Taishō, souffle, katana/Nichirin, Art du Sang Démoniaque, Muzan, etc.). Google comprend la pertinence par le champ lexical, pas par la répétition.
3. **Persona par produit** : le Poster vise un décorateur, le Magnet/Porte-clé un collectionneur, le Mug/T-Shirt un self-buy ou cadeau, le Tote Bag un usage quotidien. Calibre l'angle sur l'acheteur dominant de CHAQUE produit.

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
**Le maillage EXISTE déjà** dans le thème (template product.*.json, bloc `custom_liquid_CA68qx`) :
- Il est **server-rendered en Liquid** (donc crawlable, contrairement aux reco JS de Shopify).
- Il génère en HTML : "Collections associées" (liens vers les collections du produit) + 6 produits liés (rec-cards avec alt text).
- Match par métachamp thème (`custom.manga_anime`, `kawaii_mignonneries`, `nature_paysages`, `vehicules`, `fantaisie_magie`, `animaux`) et type DIFFÉRENT du produit courant.

→ **Ne PAS doubler ce maillage** (collections associées + 6 produits liés sont déjà crawlables). En revanche ce module a un angle borgne : il lie **même franchise / type différent**, jamais **même personnage**. Mug Nezuko peut pointer vers Tableau Tanjiro, jamais vers Tableau Nezuko.

**Le vrai levier = vérifier les dépendances de données du maillage (sinon il rend du vide = page orpheline) :**
- [ ] Le métachamp thème (`custom.manga_anime` etc.) est rempli sur CHAQUE produit du cluster. Si vide → 0 produit lié → orphelin. 🔴 priorité
- [ ] Le produit est bien assigné à ses collections (type + franchise). Sinon pas de "Collections associées".
- [ ] Produit en stock (`available`) : un produit à 0 stock est exclu du module et perd ses liens entrants.

**Maillage intra-cluster (lien sémantique même personnage) — complémentaire, non redondant :**
Ajouter **1 lien `<a>` par fiche**, tissé naturellement dans la prose (jamais un bloc "Voir aussi" fixe).
- **Cible** : un autre produit ACTIF du même cluster (type différent), en **chaîne circulaire** (chaque page reçoit 1 lien entrant ET donne 1 lien sortant)
- **Placement varié** : P1, CTA ou phrase de transition — chaque lien doit s'intégrer naturellement dans la logique de SON produit. **INTERDIT : pattern formulaïque répété sur tous les produits** (ex : "Savourez X, et prolongez avec le Y" sur 6/6 fiches). Idéal : chaque lien a une raison narrative d'être là (cadeau double en P1, setup gaming en P1, collection en P1, etc.) — le placement découle du contenu, pas d'une formule.
- **Ancre descriptive** : "notre poster Nezuko", "le porte-clé Nezuko", etc. — jamais "cliquez ici" ni URL nue
- **JAMAIS pointer vers un DRAFT** (pas d'URL publique — lien mort)
- **Format** : `<a href="/products/[handle]">[ancre]</a>` (URL relative)
- Construire la chaîne au début du cluster (ex : Mug → Tableau → Porte Clé → T-Shirt → Chiffonnette → Tapis → Magnet → Mug), noter les handles réels (vérifier via GraphQL)

### 2. Schema Product — OK (confirmé par la propriétaire)
- Le thème sort déjà un `Product` JSON-LD correct. Ne pas y retoucher sauf demande explicite.

### 3. Alt text des images
- Chaque image produit doit avoir un alt descriptif contenant le keyword (ex : "Mug Zenitsu Demon Slayer illustré à la main").
- À vérifier/corriger dans le workflow (champ `media` / `image.altText` via GraphQL).

### 4. Handle / URL
- Le handle doit contenir le keyword propre, sans faute (ex : `mug-zenitsu`, pas `mug-dragon-de-le-foret`).
- Ne PAS changer un handle déjà indexé sans redirection 301 (sinon 404).

### 5. Disponibilité produit
- Une fiche en rupture longue ou à stock 0 est souvent désindexée (Google évite les produits indisponibles).
- DRAFT = jamais indexé. Écrire la description est utile seulement si le produit sera publié.

### 6. Profondeur de contenu (anti-thin) — RÉGLÉ
- Une section FAQ (`collapsible-content`) existe déjà sur chaque page produit, MAIS elle est générique par type de produit (mêmes 5 questions sur tous les mugs). Elle ajoute de la profondeur, pas de l'unicité.
- Ne PAS ajouter de FAQ dans le descriptionHtml (redondant).
- Conséquence : sur chaque page, le SEUL contenu vraiment unique = titre + NOTRE description (intro/lore/CTA) + le maillage qui en découle. FAQ, specs, badges, bp1-bp5 sont templatés.
- DONC : la qualité et l'unicité de la description sont LE levier anti-thin. C'est la raison d'être du travail cluster. Chaque intro/lore/CTA doit être unique entre produits ET refléter le perso (pas un texte générique réutilisable).

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
- Le paragraphe artisan EST en gras (`<strong>`), les autres paragraphes narratifs JAMAIS
- Format obligatoire (2 paragraphes de prose AVANT les specs) :
  `<p>P1 hook + intention d'achat + keyword</p><p>P2 lore/univers en LSI (vocabulaire de l'œuvre)</p><ul><li>specs</li></ul><p><strong>P3 artisan unique</strong></p><p>CTA varié</p>`

### Longueur (anti-thin — levier d'indexation n°1)
- **130 à 160 mots de prose UNIQUE** par fiche (P1 + P2 + P3 artisan + CTA, hors specs templatées).
- Raison : specs + FAQ + badges sont templatés par le thème. La prose est le SEUL contenu unique de la page. Trop court = "explorée, non indexée". La richesse du texte EST le ROI du projet.
- P1 et P2 = 2-3 phrases chacun. Pas de remplissage : chaque phrase apporte une info (émotion, usage, ou lore).

### Contenu
- JAMAIS de données Semrush dans les descriptions (volumes, rankings, "X 000 recherches/mois") → les descriptions sont pour les clients
- JAMAIS de description de l'illustration (risque d'hallucination — on ne voit pas le dessin). Décrire le PERSONNAGE (lore canon) est OK, décrire NOTRE dessin est INTERDIT.
- JAMAIS d'invention de lore incertain → si un personnage est inconnu, chercher en ligne ou demander
- JAMAIS de clichés IA : "emmenez-vous dans un voyage", "vibrez au rythme de", "affirmez votre puissance"
- Vouvoiement obligatoire ("votre", "vous")
- Phrases courtes — une idée par phrase
- **Power words pour l'audience otaku/collectionneur** (à doser, pas à empiler) : collector, exclusif, édition, fait main, rare, introuvable ailleurs, pièce unique. Surtout sur Magnet, Porte-clé, Pin's (instinct de collection).
- **Synonymes pour ratisser large** : alterner Mug/Tasse, Poster/Affiche/Tableau/Toile/Cadre, Tapis de souris/Tapis Gaming, Tote Bag/Sac/Cabas, Magnet/Aimant. Ne jamais répéter 4× le même mot produit. JAMAIS d'anglicismes dans les méta titres ni les descriptions ("mousepad", "tee" seul, etc.).

### CTAs
- Verbe d'impératif différent par produit dans le cluster
- Vérifier l'orthographe lettre à lettre : "Savourez" (pas "Savorez"), "Offrez", "Équipez"...
- **Varier le REGISTRE, pas seulement le verbe** : ne JAMAIS finir par "recevez votre X sous quelques jours" sur plusieurs fiches (redondant). Alterner les registres : cadeau ("offrez-le à un passionné"), collection ("ajoutez-le à votre collection"), usage ("glissez-la dans votre sac"), fierté ("portez vos couleurs"), déco ("sublimez votre intérieur").

### Méta titres
- Format : `[Keyword principal] [emoji produit] [Franchise] | [Synonyme/Attribut]`
- JAMAIS "| Les Bois d'Aurore" en suffixe
- JAMAIS "| Kimetsu no Yaiba" ou autre keyword secondaire franchise — remplacer par le suffixe pour éviter la cannibalisation entre fiches
- **Le suffixe après le pipe doit travailler en double** : caser un SYNONYME du produit (capte une 2e requête) ET/OU l'attribut technique majeur. Ne pas gâcher ce slot en spec pure quand un synonyme à volume existe.
  - Exemples : "| Tasse Céramique" (capte tasse), "| Affiche & Toile", "| Tapis Gaming" (capte tapis gaming), "| Sac Satiné" (capte sac), "| Aimant Métal" (capte aimant), "| Du S au XXL" (capte la recherche par taille)
- **VARIER le suffixe entre clusters FRÈRES (même franchise) — règle anti-redondance INTER-cluster** : ne JAMAIS réutiliser le même suffixe sur le même type de produit d'un cluster voisin de la même franchise. Ex : si Mug Goku Enfant et Mug Goku Nuage Magique finissent déjà par "| Tasse Dragon Ball", le Mug du cluster suivant doit prendre un AUTRE synonyme/attribut ("| Tasse Céramique", "| Chope 340ml"...). Ce n'est pas de la cannibalisation (l'ouverture du titre diffère) mais un suffixe templaté répété sur 3+ fiches paraît automatisé. **Procédure** : avant de figer les suffixes d'un cluster, lister via GraphQL les `seo.title` des clusters déjà faits de la même franchise (`query: "[franchise ou perso racine]"`), repérer les suffixes déjà pris par type de produit, et choisir un synonyme/attribut encore libre. Banque de rotation par produit : Mug → Tasse Céramique / Chope 340ml / Tasse à Café ; Tableau → Poster & Toile / Affiche & Cadre / Toile Tendue ; Porte-clé → Breloque Métal / Médaillon Métal / Porte-clé Acier ; Chiffonnette → Chiffon Lunettes / Microfibre Douce / Lingette Écran ; Tapis → Tapis Gamer / Tapis Gaming / Base Antidérapante ; Tote Bag → Sac Satiné / Cabas Coton / Sac Toile ; Magnet → Aimant Frigo / Aimant Métal / Aimant Collector. Toujours garder un VRAI synonyme ou attribut (jamais varier pour varier en perdant la capture sémantique).
- **Emoji VARIÉ par type de produit** (scan visuel + CTR en SERP) : ☕ Mug, 🖼️ Poster/Tableau, 🔑 Porte-clé, 👕 T-Shirt, 🧼 Chiffonnette, 🖱️ Tapis de souris, 👜 Tote Bag, 🧲 Magnet. Ne PAS mettre le même emoji sur les 8 fiches d'un cluster.
- Keyword avec le plus grand volume Semrush en premier (niveau produit, pas franchise)
- Max 60 caractères

### Méta descriptions
- Max 155 caractères — COMPTER avant de valider
- **C'est une PROMESSE, pas une fiche technique.** Structure : bénéfice/émotion + soft CTA. Donner une raison de cliquer plutôt que le concurrent.
- **Keyword dans les ~10 premiers mots** : Google met en gras les termes de la requête → le keyword doit être tôt pour attirer l'œil dans la SERP.
- **INTERDIT en méta description** : "sans IA", "Made in Anjou", specs brutes ("céramique 340ml") → c'est du jargon interne qui ne fait pas cliquer. Ces arguments vont dans le CORPS (preuve de confiance), pas dans la vitrine.
- **Franchise une seule fois** : ne pas répéter "Demon Slayer" 2× (keyword stuffing visible).
- JAMAIS de superlatif auto-décerné ("les plus beaux posters", "les plus touchants") → pas crédible.
- Angle différent pour chaque produit du cluster.

### Anti-duplicate à l'échelle du SITE (pas seulement du cluster)
- "Illustré à la main en Anjou" est répété sur des CENTAINES de fiches tous clusters confondus → boilerplate que Google peut dévaluer.
- VARIER l'expression de la valeur artisanale d'un cluster à l'autre, pas seulement à l'intérieur d'un cluster. Banque de formulations à faire tourner (voir Étape 4, P3 artisan).

### 🔁 GATE anti-footprint inter-cluster — squelettes par type de produit (vérif AVANT application)
Le vrai duplicate inter-cluster n'est PAS la prose complète (chaque perso a un lore distinct → les P2 divergent naturellement). Le risque réel = le **SQUELETTE répété par TYPE de produit**, car l'angle d'ouverture (P1) et le P3 artisan sont dictés par le produit, pas par le perso. En écrivant deux clusters de la même franchise à la suite, on calque inconsciemment le nouveau sur le précédent.
- **Exemple réel (Vegeta SSJ → Gohan SSJ2, 2026-06-19)** : 6/7 P1 et 7/7 P3 partageaient le même squelette ("Compact et collector, ce porte-clé...", "Votre setup mérite [X]...", "Ce magnet... s'accroche sur votre frigo et ne lâche plus", P3 "Dessiné ligne à ligne à la main sur tablette en Anjou..." **verbatim**). Cause racine : banque P3 à 4 entrées rotées dans le même ordre = récurrence garantie.
- **Procédure (légère, juste avant l'Étape 7)** : ouvrir le DERNIER `_seo_new.json` de la même franchise et comparer, produit par produit du même type :
  - (a) les **4-5 premiers mots du P1** → doivent différer (verbe/structure d'attaque) ;
  - (b) la **formule P3 artisan** → doit différer (verbe d'attaque + construction).
- **Ne PAS** diff la prose entière (inutile : perso différent = texte différent). Si collision sur (a) ou (b) → reformuler l'ouverture / piocher une autre entrée P3.
- **Banque P3 ÉLARGIE** (faire tourner, ne jamais réutiliser la même que le cluster précédent du même type) :
  1. "Tracé à la main sur tablette graphique, ce dessin numérique est garanti sans IA, imprimé dans notre atelier de l'Anjou."
  2. "Cette illustration numérique naît d'un trait fait main, sans la moindre IA, et prend vie en France au cœur de l'Anjou."
  3. "Pensé et dessiné à la main sur tablette, ce motif numérique ne doit rien à l'IA : une création artisanale 100% angevine."
  4. "Né sous le stylet, à la main, ce visuel numérique est garanti sans IA et façonné en Anjou."
  5. "Chaque trait de ce visuel numérique est posé à la main au stylet, sans aucune IA, dans notre atelier de l'Anjou."
  6. "Conçu au stylet et dessiné à la main, ce visuel numérique ne doit rien à l'IA, façonné dans l'Anjou."
  7. "Réalisé à la main au stylet, ce visuel numérique ne contient aucune IA et naît dans notre atelier angevin."
  8. "Dessin numérique né sous le stylet, entièrement à la main et sans IA, façonné en Anjou au cœur de la France."
  9. "Façonné à la main au stylet dans l'atelier angevin, ce motif numérique est garanti 100% sans IA."

### Placement du keyword dans l'intro — RÈGLE ANTI-FORMULAIQUE
Le keyword "[perso] [franchise]" DOIT apparaître dans le premier paragraphe de chaque fiche — mais PAS toujours en première position.
- INTERDIT : 7 intros qui commencent toutes par `[verbe] Zenitsu Demon Slayer [contexte]` → structure identique = duplicate pattern
- OK : le keyword peut être en début, milieu ou fin de l'intro selon le produit
- La STRUCTURE de la phrase doit changer entre chaque produit, même si le keyword est le même

Exemples variés sur le même keyword "Zenitsu Demon Slayer" :
- Mug : "Chaque matin commence mieux avec ce mug illustré à la main en Anjou. Un must pour les fans de Zenitsu Demon Slayer."
- Tapis : "Sur votre bureau, place au Souffle de la Foudre : ce tapis de souris Zenitsu Demon Slayer est illustré à la main en Anjou."
- Magnet : "Ce magnet collector en métal rigide rend hommage à Zenitsu Demon Slayer. Illustré à la main en Anjou, compact et solide."

### 🎯 Règle du Filet de Sécurité (Intentions Larges) — ABSOLUE
**OBLIGATOIRE sur 100% des fiches.** Ne te repose JAMAIS uniquement sur le nom du personnage ou sur le lore de niche. Tu dois IMPÉRATIVEMENT intégrer des "intentions de recherche larges" (transactionnelles) sur CHAQUE fiche du cluster pour capter le trafic de masse de la franchise mère. C'est le filet qui rattrape les clusters topiques purs (combos perso = 0) : même si "[produit] [perso]" ne pèse rien, "[produit] [franchise]" et "cadeau [franchise]" pèsent souvent des centaines de recherches/mois.

- **Le Lexique obligatoire** : piocher dans des termes comme "cadeau [Franchise]", "goodies [Franchise]", "déco manga", "idée cadeau otaku", "[Produit] [Franchise]" (ex : Mug Dragon Ball, Poster One Piece). Les volumes franchise sont au registre `keywords_ledger.md` (réutilisables sans re-mesurer).
- **Application ASYMÉTRIQUE — couvrir TOUT le cluster** : vérifie fiche par fiche. N'oublie JAMAIS le Tableau, le Porte-clé ou le Magnet sous prétexte qu'ils ont moins de texte. Le piège classique = mettre "cadeau Dragon Ball" sur le Mug et la Chiffonnette puis oublier le reste. Chaque fiche doit contenir au moins une intention large.
- **Intégration NATURELLE** : ces termes se tissent fluidement dans la prose (P1, P2 ou CTA), jamais en bloc ni en répétition mécanique. Une intention large par fiche suffit si elle a une raison narrative d'être là (cadeau, déco, setup, collection). Objectif : ne jamais alerter les filtres de keyword stuffing de Google.
- **Check final** : avant présentation, relis les 7-8 fiches et confirme que CHACUNE contient une intention large. Si une fiche n'en a pas → l'ajouter avant validation.

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
{ products(first: 30, query: "[Personnage]") { edges { node { id title status } } } }
```
Note : utiliser `query: "[Personnage]"` (recherche full-text), PAS `title:[Personnage]` qui rate des produits.
Tester aussi les variantes de titre (ex : "T-Shirt Shadow" vs "T-Shirt Shadow the Hedgehog").
**Inclure les DRAFT** (Tote Bag, T-Shirt si présent) — les traiter comme les ACTIVE.

### Étape 1.5 — Métachamps : NE PLUS VÉRIFIER (fait par la propriétaire)
La propriétaire a confirmé que les métachamps thème (`manga_anime` etc.) sont remplis sur tous les produits. **Ne plus lancer cette vérif**, sauf si elle le redemande explicitement. Récupérer uniquement seo/descriptionHtml au moment du backup.

### Étape 2 — Backup : SUPPRIMÉ (redondant)
L'historique git + l'historique Shopify suffisent. Ne plus créer de fichier `_backup.json`.

### Étape 2.5 — Title (H1) + Handle : quand et comment modifier

**Rôle de chaque champ — NE PAS confondre :**
- **Title (H1)** = ce que le CLIENT voit sur la fiche produit. Format court : `[Type produit] [Personnage]`. Exemple : "Mug Ace", "Mug Rumi". La franchise n'est PAS nécessaire dans le title — elle pollue l'UX pour le client.
- **Meta title** = ce que GOOGLE affiche dans les SERPs. C'est ICI que va le keyword complet : "Mug Ace One Piece ☕ | Tasse Poing Ardent". C'est le levier SERP, pas le title.
- **Handle (URL)** = levier SEO URL. Doit contenir la franchise si le perso est ambigu (ex : "mug-ace-one-piece", pas "mug-ace" qui peut être confondu avec autre chose).

**Format standard du title :** `[Type produit] [Personnage]` (jamais la franchise sauf si le perso seul est incompréhensible sans elle — rare)

**Quand modifier le handle (et créer sa 301) :**
- Handle actuel ≠ slugification du keyword dominant → renommer
- Perso ambigu sans franchise dans l'URL (ex : "mug-ace" → "mug-ace-one-piece")
- Incohérence intra-cluster (certains produits ont la franchise dans le handle, d'autres non) → uniformiser

**Quand modifier le title :**
- Uniquement si le title actuel est vraiment erroné (mauvais perso, faute) ou si la franchise est tellement longue qu'elle est absente même du handle ET de la meta — cas rare

**Procédure :**
1. Mettre à jour `handle` (et `title` si nécessaire) via `productUpdate`
2. Créer les redirections 301 via `urlRedirectCreate` pour chaque handle modifié
   Format : `{ path: "/products/[ancien-handle]", target: "/products/[nouveau-handle]" }`
3. Mettre à jour les liens du maillage dans le fichier JSON (les `<a href>` pointent vers les nouveaux handles)
4. Faire tout en batch (aliases GraphQL) pour tous les produits du cluster en une seule passe

**JAMAIS changer un handle sans créer sa 301 — sinon 404.**

### Étape 3 — Recherche Semrush (tool : execute_report, database: fr)

Une recherche bâclée = méta titres sur les mauvais keywords. Ne JAMAIS résumer à 3 requêtes.

**RÈGLE D'OR — preuve fraîche obligatoire (anti-erreur Ulquiorra "poster 20/mois oublié") :**
- AUCUN chiffre de volume (y compris "= 0") ne peut être affirmé sans un résultat Semrush lancé DANS LA SESSION COURANTE. Interdit de recopier une note d'un fichier précédent, de la mémoire, ou de supposer "ça doit être 0".
- Le keyword qui ouvre CHAQUE méta titre doit être le gagnant prouvé par une requête de cette session. Si je n'ai pas le chiffre sous les yeux, je relance la requête AVANT d'écrire le méta titre.
- Les volumes trouvés sont consignés dans le JSON du cluster (bloc `semrush_data`, voir Étape 4) : un méta titre sans preuve dans `semrush_data` = non valide.
- Rappel paramètre : `phrase_these` / `phrase_fullsearch` utilisent le champ **`phrase`** (pas `keyword`). Caractères accentués OK dans `phrase`, jamais dans un alias GraphQL.

**3.1 — Découverte large (OBLIGATOIRE en premier, et à LIRE vraiment) :**
```
phrase_fullsearch → "[perso]"          (TOUTES les phrases contenant le perso + volumes, en 1 appel)
phrase_related    → "[perso]"          (variantes sémantiques, synonymes, termes adjacents)
```
→ C'est LE filet principal : `phrase_fullsearch` remonte d'un coup les combos "[produit] [perso]" à volume qu'on n'aurait pas devinés (ex : "poster ulquiorra" 20/mois ne sort qu'ici ou en testant le synonyme exact). Ne PAS sauter cette étape, ne PAS la survoler : lire chaque ligne, surligner les combos produit qui ont du volume.
→ Si `phrase_fullsearch` ramène peu, c'est un signal pour tester manuellement TOUS les synonymes en 3.2 (un produit à 0 sur son mot canonique peut avoir du volume sur un synonyme : tableau=0 mais poster=20).

**3.1bis — NOMS ALTERNATIFS du perso (OBLIGATOIRE — angle mort fréquent) :**
Un perso est souvent cherché sous un AUTRE nom que son nom principal. Lister TOUS ses alias AVANT de figer les métas, puis lancer `phrase_fullsearch` + le balayage produit 3.2 sur chacun qui a du volume :
- **Épithète / titre** : Pilier Insecte (Shinobu), Kazekage (Gaara), Cuarta Espada (Ulquiorra), Hokage, Lune Supérieure...
- **Romanisations** : Kocho / Kochou / Kochō, Cifer / Schiffer
- **Nom EN vs FR**, surnom, alias héroïque, **nom de forme/transformation** (Two Blue Vortex pour Boruto)
→ **DEUX issues, à trancher pour chaque alias (c'est l'adaptation clé) :**
  1. **Si "[produit] [alias]" a du volume** (ex : un "mug [épithète]" cherché) → l'alias peut OUVRIR ou enrichir le méta titre / le suffixe. Le consigner dans `semrush_data`.
  2. **Si seul l'alias NU a du volume, en informationnel/lore** (ex : "pilier insecte" 70, "pilier de l'insecte" 210, mais "mug/poster pilier insecte" = 0) → l'alias va dans le **TEXTE** (P1 hook ou P2 lore), JAMAIS dans le méta titre. C'est de la longue traîne lore, pas une requête d'achat.
→ Cas Shinobu (vérifié 2026-06-18) : épithète informationnel seulement → "Pilier Insecte" tissé dans chaque description, méta titres inchangés. Toujours TESTER avant de conclure (preuve fraîche).

**3.2 — Une requête par type de produit + variantes sémantiques (8 requêtes) :**
Chaque produit a des SYNONYMES qu'il faut tester. Un produit = une ligne phrase_these avec toutes ses variantes + le perso ET ses alias.
**Tester TOUS les synonymes ci-dessous, même ceux qu'on croit nuls : un appel `phrase_these` couvre toute une ligne, donc le coût est nul et les surprises sont réelles (ex : Gaara → tout produit à 0 sauf "poster" 20 et "sac" 20 ; "t shirt gaara" 20 alors que pas de produit). Ne JAMAIS raccourcir la liste.**

| Produit | Keywords à tester (avec [perso] ET alias perso) |
|---|---|
| Mug | `mug [perso];tasse [perso];gobelet [perso];chope [perso];mug café [perso]` |
| Tableau | `tableau [perso];poster [perso];affiche [perso];toile [perso];cadre [perso];peinture [perso];déco [perso];décoration murale [perso];poster mural [perso];kakemono [perso]` |
| Tapis de Souris | `tapis de souris [perso];tapis souris [perso];mousepad [perso];tapis gaming [perso];tapis gamer [perso];deskmat [perso];tapis xxl [perso]` |
| Chiffonnette | `chiffonnette [perso];chiffon lunettes [perso];chiffon [perso];chiffon écran [perso];microfibre [perso];lingette microfibre [perso]` |
| Tote Bag | `tote bag [perso];sac [perso];sac toile [perso];cabas [perso];sac shopping [perso];sac coton [perso];sac tissu [perso];sac courses [perso]` |
| Magnet | `magnet [perso];aimant [perso];magnet frigo [perso];aimant frigo [perso]` |
| Porte Clé | `porte clé [perso];porte-clé [perso];porte clef [perso];porte clés [perso];keychain [perso];breloque [perso]` |
| T-Shirt | `t shirt [perso];tee shirt [perso];t-shirt [perso];tshirt [perso]` |

→ **AVANT cette table, lancer le filet 3.1 `phrase_fullsearch "[perso]"` ET LE LIRE LIGNE PAR LIGNE** : il remonte d'un coup tout combo produit à volume (même un synonyme imprévu) jusqu'à la limite d'affichage. Si un combo produit y apparaît, le tester en clair en 3.2 pour confirmer le volume exact. La table 3.2 reste obligatoire même si fullsearch semble vide (les volumes 20 passent sous le seuil d'affichage du top).
→ Pour CHAQUE produit, relancer la même ligne en remplaçant [perso] par chaque alias trouvé en 3.1 (ex : Shadow → "shadow the hedgehog", "shadow sonic", "shadow hedgehog").
→ Le keyword gagnant (plus gros volume PROUVÉ cette session) de chaque produit va EN PREMIER dans son méta titre. Ex Ulquiorra : "poster ulquiorra" (20) > "tableau ulquiorra" (0) → méta titre Tableau commence par "Poster", le H1 reste "Tableau Ulquiorra".
→ Le mot produit du méta titre peut donc DIFFÉRER du H1 : on suit le volume, pas le nom du produit. Toujours vérifier l'ordre Mug/Tasse, Tableau/Poster/Affiche, Tapis/Mousepad, Magnet/Aimant, Tote/Sac, Porte-clé/Keychain.
→ Si tout à 0 (vérifié, pas supposé) : stratégie cluster topique (les fiches renforcent l'autorité sur le keyword franchise, longue traîne uniquement). Même à 0, consigner "0 (vérifié [date])" dans `semrush_data`.

**3.3 — Variante perso/franchise pour les intros :**
```
phrase_these → "[perso] [franchise];[franchise] [perso]"
```
→ La variante gagnante est la phrase exacte à mettre dans chaque intro.

**3.4 — Intentions larges (OBLIGATOIRE si keyword exact < 50/mois) :**
Si "[produit] [perso]" a moins de 50 recherches/mois, lancer une recherche sur les intentions plus larges à intégrer dans les textes :
```
phrase_these → "cadeau [franchise];goodies [franchise];goodies manga;mug manga;t shirt manga;affiche [franchise];poster [franchise];décoration [franchise]"
```
→ Les keywords à volume (ex : "cadeau demon slayer" 210/mois, "poster demon slayer" 720/mois) sont à intégrer NATURELLEMENT dans le P1 et/ou la méta description.
→ Objectif : capter un trafic plus large que le seul "[produit] [perso]" quasi nul.
→ Ne PAS forcer — si ça ne rentre pas naturellement, ne pas l'inclure.

**3.5 — Questions / longue traîne (nourrit le P2 lore ET la longue traîne) :**
```
phrase_questions → "[perso]"      (qui est, mort, vs, âge, citation, signification du nom...)
```
→ Facile à ranker en DA ~8. Les questions à volume orientent le CHOIX du fait lore en P2 : si "ulquiorra mort" a du volume, le magnet (angle mort/cendres) capte cette intention. On aligne l'angle lore de chaque produit sur une question recherchée quand c'est possible.
→ Ne JAMAIS mettre la question telle quelle en stuffing : on choisit le SUJET du P2 en fonction d'elle, on rédige en prose naturelle.

**3.6 — Gap concurrentiel (trouver les combos qui convertissent vraiment) :**
```
organic_research → domaine d'une boutique de goodies manga concurrente (ex : un gros e-commerce FR du secteur)
```
→ Repère les combos "[produit] [perso/franchise]" sur lesquels les concurrents rankent et qu'on n'avait pas testés. C'est la source des keywords "qu'on n'imagine pas". À lancer 1 fois par grande franchise (pas par perso) pour cartographier le marché.
→ Filtrer sur les requêtes transactionnelles (mug, poster, figurine, tote...) et noter celles à volume dans le registre (3.8).

**3.7 — Registre `keywords_ledger.md` : DATA CONCRÈTE réutilisable, jamais de prédiction.**
Le registre n'est PAS un devin ("poster gagne d'habitude, teste-le en premier" = interdit). Tester tous les synonymes d'un produit coûte UN seul appel `phrase_these` → on mesure frais à chaque perso, toujours. Le registre sert à deux choses concrètes seulement :

a) **Réutiliser les keywords NIVEAU FRANCHISE déjà mesurés (le vrai gain).**
   - Propres au perso ("ulquiorra", "poster ulquiorra") → re-mesurés frais à CHAQUE perso.
   - Niveau franchise ("cadeau bleach", "goodies bleach", "poster manga", "figurine bleach", "[franchise] anime") → IDENTIQUES pour tous les persos d'une même œuvre. Mesurés UNE fois par franchise (étape 3.4), puis réutilisés tels quels pour chaque perso suivant de cette franchise. Ce n'est pas une prédiction : c'est le même keyword, déjà mesuré.
   - DONC pour un perso d'une franchise déjà au registre : on lit la section franchise (broad-intent déjà chiffré), et on ne lance frais QUE les combos "[produit] [perso]" du nouveau perso.

b) **Trace auditable** : tout volume retenu pour un méta titre est consigné avec sa date, pour pouvoir re-vérifier une décision sans la refaire de mémoire.

→ Y consigner aussi les combos transactionnels trouvés en gap concurrentiel (3.6).
→ Toute donnée du registre porte une DATE. Si elle a plus de ~6 mois, re-mesurer (les volumes bougent).

**Règle de propriété des keywords :**
- "[produit] [franchise]" (ex : "mug demon slayer") → appartient aux COLLECTIONS pour le méta titre, MAIS peut apparaître naturellement dans le texte des fiches produit
- "[produit] [perso]" → keyword du méta titre de la fiche produit (même à volume faible)
- Exception franchises solo (Goldorak) : perso = franchise, le keyword va sur la fiche produit

**Rappel ranking (DA ~8) :** la description fait la conversion + la longue traîne, PAS le ranking sur les head terms. Les vrais leviers de ranking sont les collections, les backlinks et le feed Shopping. Ne jamais promettre un ranking head-term via une description de fiche produit.

### Étape 4 — Écrire les descriptions dans le fichier final
Fichier : `[perso]_seo_new.json` dans `/home/user/Personnal/`
**Écrire le fichier AVANT de présenter à l'utilisateur.**

**Bloc `semrush_data` OBLIGATOIRE en tête du JSON (traçabilité keywords) :**
Consigner les volumes réellement retournés cette session, produit par produit, avec le gagnant retenu. Sert de preuve auditable : on ne réécrit jamais un méta titre sans regarder ce bloc.
```json
"semrush_data": {
  "date_recherche": "AAAA-MM-JJ",
  "perso": { "ulquiorra": 3600, "ulquiorra schiffer": 2900 },
  "par_produit": {
    "Mug":      { "mug ulquiorra": 0, "tasse ulquiorra": 0, "gagnant": "mug ulquiorra (topique, 0)" },
    "Tableau":  { "tableau ulquiorra": 0, "poster ulquiorra": 20, "affiche ulquiorra": 0, "gagnant": "poster ulquiorra (20)" }
  }
}
```

Pour chaque produit (130-160 mots de prose unique au total) :
1. **P1 (2-3 phrases) — l'INTENTION** : pourquoi on achète CE produit (persona dominant : décorateur, collectionneur, cadeau, usage quotidien). Keyword "[perso]" placé tôt mais structure de phrase VARIÉE entre produits. Intégrer un keyword d'intention large si naturel (cadeau franchise, goodies manga, poster franchise).
2. **P2 (2-3 phrases) — le LORE en LSI** : un fait canon DISTINCT sur le perso (pas répété entre produits), raconté avec le vocabulaire de l'œuvre (Hashira, pourfendeur, époque Taishō, Art du Sang, Muzan...). C'est ce paragraphe qui crée la richesse sémantique SANS stuffing.
3. **Specs** : bloc standardisé copié depuis ce fichier (section blocs specs)
4. **P3 artisan en gras** : phrase 100% UNIQUE par produit ET variée d'un cluster à l'autre, intégrant les 4 notions : illustration numérique + dessinée à la main + sans IA + Anjou/France.
   - Banque de formulations (à faire tourner, ne jamais copier-coller) : "Tracé à la main sur tablette graphique, ce dessin numérique est garanti sans IA, imprimé dans notre atelier de l'Anjou." / "Cette illustration numérique naît d'un trait fait main, sans la moindre IA, et prend vie en France au cœur de l'Anjou." / "Pensé et dessiné à la main sur tablette, ce motif numérique ne doit rien à l'IA : une création artisanale 100% angevine." / "Né sous le stylet, à la main, ce visuel numérique est garanti sans IA et façonné en Anjou."
5. **CTA (1 phrase) — registre varié** : voir règle CTAs (ne pas finir tout le cluster par "recevez votre X sous quelques jours").

### Étape 5 — Checklist avant présentation (toutes cases à cocher mentalement)

**Unicité inter-produits :**
- Aucun P1 ne commence par la même structure entre produits du cluster
- Aucun fait lore P2 répété entre produits (dates, événements, angles)
- Tous les CTAs ont des registres différents (pas seulement des verbes différents)

**Ton (persona Copywriter Senior) :**
- Chaque P1 répond à POURQUOI on achète ce produit précis (pas juste ce qu'il est)
- LSI présent : vocabulaire de l'œuvre dans P2, PAS de stuffing "[perso] [franchise]" en milieu de phrase
- Synonymes utilisés (Mug/Tasse, Poster/Affiche...), pas 4× le même mot produit
- Power words présents sur les produits collection (Magnet, Porte-clé)

**Langue :**
- Vouvoiement partout
- Aucun tiret long (—)
- CTAs : orthographe vérifiée lettre à lettre
- Aucune donnée Semrush dans le texte

**Structure & longueur :**
- Aucune balise H
- Format `<p>P1 intention</p><p>P2 lore LSI</p><ul>specs</ul><p><strong>P3 artisan</strong></p><p>CTA</p>` respecté
- **130-160 mots de prose unique** (hors specs) — COMPTER
- P3 artisan : 4 notions (numérique + à la main + sans IA + Anjou/France), formulation unique intra-cluster ET variée vs autres clusters

**Keywords / métas :**
- **GATE PREUVE** : chaque mot d'ouverture de méta titre correspond au `gagnant` du bloc `semrush_data`, lui-même issu d'une requête de CETTE session. Si une case n'a pas de chiffre prouvé → relancer Semrush avant de valider. Aucun "0" supposé.
- **GATE SYNONYME** : le balayage COMPLET de la table 3.2 a été lancé pour chaque produit (TOUS les synonymes, pas juste le mot canonique) + `phrase_fullsearch "[perso]"` lu ligne par ligne. Couverture minimale : Mug→tasse/gobelet/chope, Tableau→poster/affiche/toile/peinture/déco, Tapis→mousepad/tapis gaming, Magnet→aimant/magnet frigo, Tote→sac/cabas/sac toile, Porte-clé→keychain/porte clef/breloque, Chiffonnette→chiffon/microfibre, T-Shirt→tee shirt/tshirt. Le méta titre suit le volume, pas le nom du H1. Tout synonyme à volume mais SANS produit correspondant est consigné au registre (opportunité produit future).
- **GATE NOM ALTERNATIF** (3.1bis) : tous les alias du perso (épithète/titre, romanisations, nom EN/FR, forme/transformation) ont été listés ET testés à Semrush cette session. Pour chaque alias à volume : si "[produit] [alias]" convertit → méta titre/suffixe ; si l'alias nu n'a de volume qu'en informationnel/lore → placé dans le TEXTE (P1/P2), pas le méta. Consigné dans `semrush_data`.
- Méta titres sans "| Les Bois d'Aurore" ni "| [franchise secondaire]"
- Méta titres ≤ 60 caractères, emoji VARIÉ par type, synonyme dans le suffixe
- Méta descriptions ≤ 155 caractères (compter), keyword dans les 10 premiers mots
- Méta desc SANS "sans IA"/"Anjou"/specs brutes, franchise 1× max, pas de superlatif auto-décerné
- Angles méta descriptions différents entre produits

### Étape 6 — Présenter et attendre validation
Présenter les descriptions depuis le fichier écrit.
Si corrections → mettre à jour le fichier PUIS appliquer.

### Étape 7 — Appliquer en batch GraphQL
Mutations `productUpdate` par lots de 2-4 (alias GraphQL).
Champs : `descriptionHtml` + `seo { title description }`.
**CRITIQUE : toujours passer `title` ET `description` ensemble dans l'objet `seo {}`. Passer seulement `title` efface la `description` existante (Shopify écrase le champ entier).**

### Étape 7.5 — Mettre à jour les alt texts des images
Pour chaque produit, récupérer les IDs d'images via :
```graphql
{ product(id: "...") { media(first: 10) { nodes { ... on MediaImage { id image { altText } } } } } }
```
Puis mutation `productUpdateMedia` par lot :
- Format alt : `[Produit] [Perso] [Franchise] illustré à la main en Anjou`
- Pour le Tableau : conserver le type dans l'alt (ex : "Cadre Noir Nezuko...", "Poster Nezuko...", "Affiche Nezuko...")
- JAMAIS de description de l'illustration (couleurs, pose, détails visuels) → risque d'hallucination
- Si pas d'image (ex : Tote Bag DRAFT) : passer.

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

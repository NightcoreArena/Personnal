# Méthodologie SEO — Les Bois d'Aurore

> Specs HTML par type de produit → **`seo_specs.md`** (parsé par le lint, copier VERBATIM).

---

> **Journal des clusters terminés → `clusters_done.md`** (sorti d'ici le 2026-06-22 pour stabiliser les n° de ligne des sections R ci-dessous). Y vérifier "déjà fait ?" et y ajouter l'entrée après application.

# 🔧 RÉFÉRENCE OPÉRATIONNELLE DÉTAILLÉE (source de vérité — déplacée de CLAUDE.md le 2026-06-20)

CLAUDE.md ne garde que le cœur (persona + règles de jugement + résumés). Le détail mécanique vit ici et se lit À LA DEMANDE au moment de l'étape concernée.

## R1. Maillage intra-cluster (lien sémantique même personnage)

Ajouter **1 lien `<a>` par fiche**, tissé naturellement dans la prose (jamais un bloc "Voir aussi" fixe).
- **Cible** : un autre produit ACTIF du même cluster (type différent), en **chaîne circulaire** (chaque page reçoit 1 lien entrant ET donne 1 lien sortant)
- **Placement : TOUJOURS dans P1** (jamais dans le CTA, jamais en fin de fiche). Le lien s'intègre dans la 2e ou 3e phrase du premier paragraphe. **INTERDIT : pattern formulaïque répété sur tous les produits** (ex : "À associer avec notre X pour un duo…" sur 6/6 fiches). Chaque lien a une raison narrative (cadeau double, setup complet, duo collector) — la formulation varie, le placement reste en P1.
- **Ancre descriptive** : "notre poster [Franchise]", "le porte-clé [Franchise]" — jamais "cliquez ici" ni URL nue. Ancre courte (sans franchise) UNIQUEMENT si le nom du perso est long et déjà 2× dans P1 (anti-stuffing).
- **JAMAIS pointer vers un DRAFT** (lien mort). **Format** : `<a href="/products/[handle]">[ancre]</a>` (URL relative).
- Construire la chaîne au début du cluster, noter les handles réels (vérifier via GraphQL).

## R2. GATE anti-footprint inter-cluster (vérif AVANT application)

Le risque réel = le **SQUELETTE répété par TYPE de produit** : P1 (ouverture), CTA, P3 artisan, phrases de remplissage dictés par le PRODUIT, pas le perso. **LE FOOTPRINT EST CROSS-FRANCHISE.** On compare TOUJOURS aux 3 derniers clusters faits, TOUTES franchises confondues (via `footprint_log.md`).

**Procédure OBLIGATOIRE (juste avant l'application) :**
1. AVANT d'écrire : ouvrir `footprint_log.md`, lire les lignes du type de produit. Choisir pour CHAQUE produit un angle P1, un verbe/registre CTA et une entrée P3 différents des 3 dernières lignes.
2. APRÈS application : ajouter une ligne par produit (date, perso, type, angle P1, verbe CTA, n° P3).
3. Diff de contrôle, produit par produit du même type, contre les 3 dernières entrées :
   - (a) 4-5 premiers mots du P1 → doivent différer ;
   - (b) verbe d'impératif + structure du CTA → doivent différer ;
   - (c) phrase de remplissage produit → reformuler les tics récurrents ;
   - (d) formule P3 artisan → entrée de banque différente des 3 derniers du même type.

**Banque P3 (faire tourner, jamais la même que le cluster précédent du même type) :**
1. "Tracé à la main sur tablette graphique, ce dessin numérique est garanti sans IA, imprimé dans notre atelier de l'Anjou."
2. "Cette illustration numérique naît d'un trait fait main, sans la moindre IA, et prend vie en France au cœur de l'Anjou."
3. "Pensé et dessiné à la main sur tablette, ce motif numérique ne doit rien à l'IA : une création artisanale 100% angevine."
4. "Né sous le stylet, à la main, ce visuel numérique est garanti sans IA et façonné en Anjou."
5. "Chaque trait de ce visuel numérique est posé à la main au stylet, sans aucune IA, dans notre atelier de l'Anjou."
6. "Conçu au stylet et dessiné à la main, ce visuel numérique ne doit rien à l'IA, façonné dans l'Anjou."
7. "Réalisé à la main au stylet, ce visuel numérique ne contient aucune IA et naît dans notre atelier angevin."
8. "Dessin numérique né sous le stylet, entièrement à la main et sans IA, façonné en Anjou au cœur de la France."
9. "Façonné à la main au stylet dans l'atelier angevin, ce motif numérique est garanti 100% sans IA."

## R3. Placement du keyword dans l'intro (anti-formulaïque)

Le keyword "[perso] [franchise]" DOIT apparaître dans P1 de chaque fiche, mais PAS toujours en première position. INTERDIT : 7 intros qui commencent toutes par `[verbe] [perso] [franchise] [contexte]`. La STRUCTURE de la phrase change entre chaque produit, même si le keyword est le même.

## R4. Filet de Sécurité (Intentions Larges) — ABSOLU, 100% des fiches

Intégrer une "intention de recherche large" transactionnelle sur CHAQUE fiche (même le Tableau, le Porte-clé, le Magnet). Lexique : "cadeau [Franchise]", "goodies [Franchise]", "déco manga", "idée cadeau otaku", "[Produit] [Franchise]", "cadeau gaming"/"jeu vidéo" (franchises jeu vidéo). Volumes franchise réutilisables → `keywords_ledger.md`. Intégration NATURELLE (P1, P2 ou CTA), jamais en bloc. Check final : chaque fiche contient au moins une intention large.

## R5. Angles d'ouverture par type de produit

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

> **Règle ownership** : les mots-clés `[produit] [franchise]` (ex : "poster demon slayer") appartiennent aux pages COLLECTION — ne jamais les utiliser comme méta titre d'une fiche produit (cannibalisation).

## R6. Procédure Semrush détaillée (database: fr)

**RÈGLE D'OR — preuve fraîche obligatoire :** AUCUN volume (y compris "= 0") affirmé sans un résultat Semrush lancé DANS LA SESSION COURANTE. Le keyword qui ouvre CHAQUE méta titre = gagnant prouvé cette session, consigné dans `semrush_data` du JSON. Rappel param : `phrase_these`/`phrase_fullsearch` utilisent le champ `phrase` (accents OK dans phrase, jamais dans un alias GraphQL).

**3.1 — Découverte large (en premier, à LIRE ligne par ligne) :**
`phrase_fullsearch → "[perso]"` (toutes les phrases + volumes) ; `phrase_related → "[perso]"`. Remonte les combos "[produit] [perso]" à volume imprévus. Si peu de retour → tester manuellement tous les synonymes en 3.2.

**3.1bis — NOMS ALTERNATIFS (angle mort fréquent) :** lister TOUS les alias (épithète/titre, romanisations, nom EN/FR, forme/transformation) et lancer fullsearch + balayage 3.2 sur chacun à volume. Deux issues : (1) "[produit] [alias]" à volume → peut ouvrir/enrichir le méta titre ; (2) alias nu à volume informationnel/lore seulement → va dans le TEXTE (P1/P2), jamais le méta titre.

**3.2 — Une requête `phrase_these` par type de produit, TOUS les synonymes :**
🔴 **GATE ORDRE DES MOTS** : Semrush compte "[produit] [perso]" et "[perso] [produit]" comme 2 keywords distincts. Tester les DEUX ordres (ou `phrase_fullsearch` + `display_filter: "+|Ph|Co|poster"` par terme produit). Volume retenu = somme des 2 ordres.

| Produit | Keywords à tester (avec [perso] ET alias) |
|---|---|
| Mug | `mug [perso];tasse [perso];gobelet [perso];chope [perso];mug café [perso]` |
| Tableau | `tableau [perso];poster [perso];affiche [perso];toile [perso];cadre [perso];peinture [perso];déco [perso];décoration murale [perso];poster mural [perso];kakemono [perso]` |
| Tapis de Souris | `tapis de souris [perso];tapis souris [perso];mousepad [perso];tapis gaming [perso];tapis gamer [perso];deskmat [perso];tapis xxl [perso]` |
| Chiffonnette | `chiffonnette [perso];chiffon lunettes [perso];chiffon [perso];chiffon écran [perso];microfibre [perso];lingette microfibre [perso]` |
| Tote Bag | `tote bag [perso];sac [perso];sac toile [perso];cabas [perso];sac shopping [perso];sac coton [perso];sac tissu [perso];sac courses [perso]` |
| Magnet | `magnet [perso];aimant [perso];magnet frigo [perso];aimant frigo [perso]` |
| Porte Clé | `porte clé [perso];porte-clé [perso];porte clef [perso];porte clés [perso];keychain [perso];breloque [perso]` |
| T-Shirt | `t shirt [perso];tee shirt [perso];t-shirt [perso];tshirt [perso]` |

Le keyword gagnant (plus gros volume PROUVÉ) ouvre le méta titre. Le mot produit du méta titre peut DIFFÉRER du H1 (on suit le volume). Si tout à 0 (vérifié) : cluster topique, consigner "0 (vérifié [date])".

**3.3 — Variante perso/franchise pour les intros :** `phrase_these → "[perso] [franchise];[franchise] [perso]"`. La gagnante = phrase exacte à mettre dans chaque intro.

**3.4 — Intentions larges (si "[produit] [perso]" < 50/mois) :** `phrase_these → "cadeau [franchise];goodies [franchise];goodies manga;mug manga;t shirt manga;affiche [franchise];poster [franchise];décoration [franchise]"`. Intégrer NATURELLEMENT les keywords à volume.

**3.5 — Questions / longue traîne :** `phrase_questions → "[perso]"`. Les questions à volume orientent le CHOIX du fait lore en P2 (consigner dans `semrush_data` bloc `questions_lore`, aligner chaque question à volume sur un P2).

**3.6 — Gap concurrentiel :** `organic_research → domaine concurrent goodies manga` (1× par grande franchise). Noter les combos transactionnels au registre.

**3.7 — Registre `keywords_ledger.md` :** réutiliser les keywords NIVEAU FRANCHISE déjà mesurés (cadeau/goodies/poster manga/figurine [franchise]) ; re-mesurer frais les combos "[produit] [perso]". Toute donnée porte une DATE ; > ~6 mois → re-mesurer. **Lecture économe : ne PAS lire le fichier entier — consulter l'index en tête, puis `Grep "### [Franchise]" -A 15` pour charger uniquement sa table (+ §1 générique).**

**Règle de propriété :** "[produit] [franchise]" → COLLECTIONS (méta titre), mais OK dans le texte produit. "[produit] [perso]" → méta titre de la fiche produit. Exception franchise solo (Goldorak, Elden Ring, Cowboy Bebop, Haikyuu) : perso = franchise, le keyword va sur la fiche produit.

## R7. Workflow d'exécution étape par étape

**Étape 1 — Lister TOUS les produits :** `{ products(first: 30, query: "[Personnage]") { edges { node { id title status } } } }` (full-text, PAS `title:`). Inclure les DRAFT.

**Étape 1.5 — Métachamps :** NE PLUS VÉRIFIER (rempli par la propriétaire). Récupérer seo/descriptionHtml uniquement.

**Étape 2.5 — Title (H1) + Handle :**
- Title (H1) = vu par le CLIENT, format `[Type produit] [Personnage]`, sans franchise (sauf perso incompréhensible seul).
- Meta title = vu par GOOGLE, porte le keyword complet.
- Handle (URL) = contient la franchise si perso ambigu.
- Modifier le handle (+ créer 301) si : handle ≠ slug du keyword dominant, perso ambigu, incohérence intra-cluster. Procédure : `productUpdate` handle/title → `urlRedirectCreate` `{ path: "/products/[ancien]", target: "/products/[nouveau]" }` → MAJ liens maillage dans le JSON → batch aliases GraphQL. **JAMAIS changer un handle sans 301.**

**Étape 4 — Écrire le fichier `[perso]_seo_new.json`** AVANT de présenter. Bloc `semrush_data` OBLIGATOIRE en tête (volumes + gagnant par produit). Par produit (130-160 mots de prose unique) : P1 intention + keyword tôt (structure variée) + intention large ; P2 lore LSI distinct ; specs (copier depuis `seo_specs.md` VERBATIM) ; P3 artisan en gras (banque R2, tournante) ; CTA registre varié.

**Étape 6.5 — LINT OBLIGATOIRE :** `python3 /home/user/Personnal/seo_lint.py [perso]_seo_new.json`. **1 FAIL = interdiction d'appliquer.** Corriger, relancer, appliquer sur exit code 0 seulement. Re-lint après toute correction.

**Étape 7 — Appliquer en batch GraphQL :** `productUpdate` par lots de 2-4. Champs `descriptionHtml` + `seo { title description }`. **CRITIQUE : toujours passer `title` ET `description` ensemble — passer seul `title` efface la description.**

**Étape 7.5 — Alt texts :** récupérer IDs via `{ product(id){ media(first:10){ nodes{ ... on MediaImage { id image { altText } } } } } }`. `productUpdateMedia` par lot. Format : `[Produit] [Perso] [Franchise] illustré à la main en Anjou`. Tableau : conserver le type (Cadre Noir / Poster / Affiche). Jamais décrire l'illustration.

**Étape 8 — Commit :** `git add [perso]_seo_new.json footprint_log.md clusters_done.md` → commit `SEO rewrite: cluster [Perso] — N produits` → `git push -u origin [branch-courante]`. MAJ footprint_log.md (1 ligne par produit) + entrée cluster dans `clusters_done.md`.

## R8. Banque de rotation des suffixes méta titres (anti-redondance inter-cluster)

Le suffixe après le pipe doit travailler en double : caser un SYNONYME du produit (capte une 2e requête) ET/OU l'attribut technique. **VARIER le suffixe entre clusters FRÈRES de la même franchise** sur un même type de produit (un suffixe templaté répété sur 3+ fiches paraît automatisé). Procédure : avant de figer, lister via GraphQL les `seo.title` des clusters déjà faits de la même franchise, repérer les suffixes pris par type, choisir un synonyme/attribut encore libre. Toujours garder un VRAI synonyme/attribut (jamais varier pour varier en perdant la capture sémantique).

Banque par produit :
- **Mug** → Tasse Céramique / Chope 340ml / Tasse à Café
- **Tableau** → Poster & Toile / Affiche & Cadre / Toile Tendue / Affiche & Toile
- **Porte-clé** → Médaillon Métal / Métal Brossé / Acier Collector / Porte-clé Acier — **INTERDIT : "Breloque"** (dévalorise un produit en métal brossé de qualité)
- **Chiffonnette** → Chiffon Lunettes / Microfibre Douce / Lingette Écran
- **Tapis** → Tapis Gamer / Tapis Gaming / Base Antidérapante
- **Tote Bag** → Sac Satiné / Cabas Coton / Sac Toile
- **Magnet** → Aimant Frigo / Aimant Métal / Aimant Collector
- **T-Shirt** → Du S au XXL (capte la recherche par taille)

Emoji varié par type (scan visuel + CTR SERP) : ☕ Mug, 🖼️ Poster/Tableau, 🔑 Porte-clé, 👕 T-Shirt, 🧼 Chiffonnette, 🖱️ Tapis, 👜 Tote Bag, 🧲 Magnet.

## R9. Compléments rationale + exemples (remis le 2026-06-20, complétude)

**Anti-boilerplate à l'échelle du SITE (rationale de la rotation P3) :** "Illustré à la main en Anjou" est répété sur des CENTAINES de fiches tous clusters confondus → boilerplate que Google peut dévaluer. VARIER l'expression de la valeur artisanale d'un cluster à l'autre (pas seulement à l'intérieur d'un cluster) : c'est la raison d'être de la banque P3 tournante (R2).

**Dépendances de données du maillage (sinon page orpheline) :** le module thème ne rend des liens que si (a) le métachamp thème (`custom.manga_anime` etc.) est rempli sur chaque produit — sinon 0 produit lié = orphelin ; (b) le produit est assigné à ses collections (type + franchise) ; (c) le produit est en stock (`available`) — un produit à 0 stock est exclu du module et perd ses liens entrants. NB : la propriétaire confirme que les métachamps sont remplis (ne plus vérifier sauf demande).

**Exemples placement keyword anti-formulaïque (R3), même keyword "Zenitsu Demon Slayer" :**
- Mug : "Chaque matin commence mieux avec ce mug illustré à la main en Anjou. Un must pour les fans de Zenitsu Demon Slayer."
- Tapis : "Sur votre bureau, place au Souffle de la Foudre : ce tapis de souris Zenitsu Demon Slayer est illustré à la main en Anjou."
- Magnet : "Ce magnet collector en métal rigide rend hommage à Zenitsu Demon Slayer. Illustré à la main en Anjou, compact et solide."
→ Le keyword peut être en début, milieu ou fin ; la STRUCTURE de la phrase change entre chaque produit.

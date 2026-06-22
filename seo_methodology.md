# Méthodologie SEO — Les Bois d'Aurore

> Specs HTML par type de produit → **`seo_specs.md`** (parsé par le lint, copier VERBATIM).

---
## 15. Ordre de priorité pour les clusters suivants

Traiter par franchise, pas par type de produit (pour garder la cohérence topique) :

**Demon Slayer** :
- [x] Akaza — 7 produits traités (2026-06-17)
- [x] Zenitsu — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Maillage vérifié (métachamps OK).
- [x] Nezuko — 8 produits traités (2026-06-18) : Mug, Poster, Porte Clé, T-Shirt, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Maillage vérifié (métachamps OK). Intentions larges : cadeau DS 210/mois, poster DS 720/mois, t-shirt manga 720/mois.
- [x] Shinobu Kocho — 7 produits (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: shinobu (14800). 7×301 (suppression -pilier-insecte).
- [x] Muzan Kibutsuji — 7 produits (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: muzan (8100). 7×301 (suppression -kibutsuji).
- [ ] Inosuke
- [ ] Tanjiro
- [ ] Rengoku
- [ ] Doma
- [ ] (autres personnages DS)

**Pokémon** :
- [x] Pikachu (mug existant, à vérifier)
- [x] Evoli — 8 produits (2026-06-19) : Mug, Tableau, Porte Clé, T-Shirt, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: evoli (18100). 1×301 (t-shirt-pokemon-enfant→t-shirt-evoli).
- [ ] (autres personnages Pokémon)

**Kpop Demon Hunter** :
- [x] Cluster complet — 8 produits traités (2026-06-17) : Mug, Tableau, Tapis de Souris, Chiffonnette, Tote Bag, Magnet, Porte Clé, T-Shirt
- [x] Rumi — 6 produits traités (2026-06-18) : Mug, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Pas de Tableau. Keyword principal : rumi kpop demon hunters (14800/mois). Erreurs factuelles corrigées (Tapis + Magnet décrivaient Mirko/MHA). Fichier final → rumi_seo_new.json.
- [ ] Mira
- [ ] Zoey
- [ ] Huntrix (personnage individuel)

**Solo Leveling Arise** :
- [x] Cluster complet — 8 produits traités (2026-06-17) : Mug, Tableau (renommé Arise), Tapis de Souris, Chiffonnette, Tote Bag, Magnet, Porte Clé, T-Shirt Sung Jinwoo
- Note : "Tableau Solo Leveling" → renommé "Tableau Solo Leveling Arise" (Option A, cohérence cluster)
- Note : T-Shirt Sung Jinwoo corrigé (bug "Mao Mao" dans méta description)

**Goldorak** :
- [x] Cluster complet — 13 produits traités (2026-06-17) : Mug, Mug Vaisseau, Tableau, Tableau Vaisseau, T-Shirt, Porte Clé, Porte Clé Vaisseau, Chiffonnette, Chiffonnette Vaisseau, Tapis de Souris, Tapis de Souris Vaisseau, Magnet, Magnet Vaisseau
- Note : Goldorak = franchise solo → keywords "[produit] goldorak" appartiennent aux pages produit (pas aux collections)

**Shadow the Hedgehog** :
- [x] Cluster complet — 8 produits traités (2026-06-17) : Mug, Tableau, T-Shirt, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT)
- Note : "shadow sonic" (9 900/mois) > "shadow the hedgehog" (4 400/mois) → keyword secondaire dans méta titres
- Note : Volumes product-level quasi nuls → stratégie cluster topique uniquement
- Note : fichier final → shadow_seo_new.json

**One Piece** :
- [x] Trafalgar Law — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Intentions larges intégrées (cadeau one piece 1300/mois, poster one piece 1900/mois, mug one piece 880/mois). Fichier final → law_seo_new.json.
- [x] Ace — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : ace one piece (6600/mois). Cluster topique pur. Handles uniformisés en *-ace-one-piece + 4x301. 10 alt texts mis à jour. Fichier final → ace_seo_new.json.
- [ ] (autres personnages One Piece)

**Sword Art Online** :
- [x] Asuna (solo + duo Asuna & Kirito) — 14 produits traités (2026-06-18) : 7 solo (Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet, Tote Bag DRAFT) + 7 duo. Volumes [produit] asuna quasi nuls — stratégie cluster topique pur. 22 alt texts mis à jour. Fichier final → asuna_seo_new.json.
- [ ] (autres personnages SAO)

**Les Carnets de l'Apothicaire** :
- [x] Cluster complet — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Keyword principal : les carnets de l'apothicaire (60 500/mois). Volumes [produit] = 0 → cluster topique pur. Handles renommés de carnet → les-carnets + 7×301 redirects. 11 alt texts mis à jour. Fichier final → carnets_seo_new.json.

**Boruto / Naruto** :
- [x] Boruto Uzumaki — 7 produits (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: boruto (22200). 0 handle renommé.
- [x] Gaara — 7 produits (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: gaara (9900). 0 handle renommé.
- [ ] Sarada Uchiha
- [ ] Hinata

**Bleach** :
- [x] Ulquiorra Schiffer — 7 produits (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet, Tote Bag. Keyword: ulquiorra (3600). 1×301 (porte-cle-ulquiorra-schiffer→porte-cle-ulquiorra).
- [ ] (autres personnages Bleach)

**Dragon Ball** :
- [x] Shenron — 7 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: shenron (4400). 7×301 (handles renommés vers "shenron").
- [x] Goku Nuage Magique — 5 produits (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis. Keyword: goku nuage magique (170). 0 handle renommé.
- [x] Goku Enfant / Sangoku — 7 produits (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, T-Shirt, Magnet. Keyword: sangoku (14800). 2×301 (magnet/t-shirt-goku→-goku-enfant).
- [x] Goku Shenron — 7 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: goku shenron (30). 7×301 (goku-dragon-enfant→goku-shenron).
- [x] Vegeta SSJ4 — 7 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: vegeta ssj4 (590). 0 handle renommé.
- [x] Vegeta SSJ — 7 produits (2026-06-19) : Mug, T-Shirt, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: vegeta ssj (880). 5×301 (vegeta-ssj→vegeta).
- [x] Gohan SSJ2 — 7 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: gohan ssj2 (1900). 2×301 (gohan-ssj2-poster→tableau-gohan-ssj2).

**Hunter x Hunter** :
- [x] Hisoka — 7 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: hisoka (9900). 0 handle renommé.
- [x] Meruem — 6 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: meruem (4400). 0 handle renommé.

**Berserk** :
- [x] Guts Berserk — 8 produits (2026-06-19) : Mug, Tableau, Porte Clé, T-Shirt, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: guts berserk (5400). 6×301 (fautes bersek→berserk + manque guts).

**Yu-Gi-Oh!** :
- [x] Dark Magician Girl — 7 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: dark magician girl (1900 EN). 0 handle renommé.

**One Punch Man** :
- [x] Saitama — 7 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Tote Bag, Magnet. Keyword: saitama one punch man (720). 6×301 (one-punch-man→saitama).

**Chainsaw Man** :
- [x] Makima — 6 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: makima chainsaw man (1300). 0 handle renommé.

**Gachiakuta** :
- [x] Rudo Surebrec — 6 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: rudo gachiakuta (1300). 6×301 (-gachiakuta→-rudo-gachiakuta).

**Dragon Ball Super (groupe)** :
- [x] Dragon Ball Super — 6 produits (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: dragon ball super poster (90). 0 handle renommé.

**Akeno Himejima (High School DxD)** :
- [x] Akeno Himejima — 6 produits (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: akeno himejima (topique pur). 5×301 (ajout -himejima).

**Haikyuu** :
- [x] Haikyuu — 6 produits (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: poster haikyuu (50). 0 handle renommé. ⚠️ Mug Hinata (handle mug-hinata) à traiter dans un cluster Hinata dédié.

**Elden Ring** :
- [x] Elden Ring — 6 produits (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: tableau elden ring (110). 0 handle renommé.

**Cowboy Bebop** :
- [x] Cowboy Bebop — 6 produits (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: poster cowboy bebop (110). 0 handle renommé.

**Blue Lock** :
- [x] Blue Lock — 6 produits (2026-06-22) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: poster blue lock (170). 0 handle renommé.

**Kimetsu no Yaiba (groupe illustration)** :
- [x] Kimetsu no Yaiba — 6 produits (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: poster kimetsu no yaiba (140). 0 handle renommé.

**Frieren (Sousou no Frieren)** :
- [x] Frieren — 6 produits (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet. Keyword: frieren (33100). 0 handle renommé.

**T-Shirt Dessin (collection)** :
- [x] Cluster complet — 39 produits traités (2026-06-17)

---

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

**3.7 — Registre `keywords_ledger.md` :** réutiliser les keywords NIVEAU FRANCHISE déjà mesurés (cadeau/goodies/poster manga/figurine [franchise]) ; re-mesurer frais les combos "[produit] [perso]". Toute donnée porte une DATE ; > ~6 mois → re-mesurer.

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

**Étape 8 — Commit :** `git add [perso]_seo_new.json footprint_log.md seo_methodology.md` → commit `SEO rewrite: cluster [Perso] — N produits` → `git push -u origin [branch-courante]`. MAJ footprint_log.md (6 lignes) + entrée cluster ici.

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

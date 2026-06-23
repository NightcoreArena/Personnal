# Méthodologie SEO — Les Bois d'Aurore
*Référence opérationnelle. NE PAS lire en entier (coût token) : `grep -n "^#" ` puis `Read` offset/limit sur la section voulue.*

Structure (numéros non séquentiels : conservés pour les pointeurs de CLAUDE.md) :
- **§5** mots-clés Collections vs Produit · **§9** politique fichiers · **§10** blocs specs · **§13** checklist · **§15** mémoire clusters
- **R1→R9** = cœur opérationnel (maillage, GATE footprint, keyword, filet large, angles, Semrush, workflow, suffixes, rationale)

Le contexte store, la persona, les règles de rédaction et de méta vivent dans **CLAUDE.md** (chargé à chaque session). Les anciennes sections §1-4/§6-8/§11-12/§14 (dupliquées dans CLAUDE.md + R1-R9 + le linter) ont été retirées le 2026-06-23 — voir l'historique git si besoin.

---

## 5. Mots-clés détenus par les COLLECTIONS (data — ne pas viser en méta titre produit)

La RÈGLE (collection owns `[produit] [franchise]` / produit owns `[produit] [perso]`) est en **R6 « Règle de propriété »**. Ici, juste la data : ces keywords appartiennent aux pages collection, ne PAS les cibler en méta titre produit (cannibalisation). Quand le combo produit nu est à ~0 (cluster topique), la fiche convertit + renforce l'autorité topique ; mettre la phrase `[perso] [franchise]` exacte dans le texte (pas le combo collection).

| Keyword (ex. Demon Slayer) | Volume | → Collection |
|---|---|---|
| porte clé demon slayer | 210/mois | Porte Clé Demon Slayer |
| tapis de souris demon slayer | 140/mois | Tapis de Souris Demon Slayer |
| tableau demon slayer | 110/mois | Tableau Demon Slayer |
| mug demon slayer | ~200/mois | Mug Demon Slayer |
| magnet / tote bag demon slayer | 20/mois | resp. collections |
| chiffonnette demon slayer | 0/mois | Chiffonnette Demon Slayer |
| [produit] manga | variable | Collections Manga par produit |

---

## 9. Politique fichiers (PAS de backup — décision 2026-06-23)

**AUCUN `[perso]_backup.json`.** Ils gonflaient l'arbre pour rien. Shopify est la source de vérité ; en cas de besoin de rollback, requêter l'état du produit AVANT la mutation et le garder en contexte (pas de fichier écrit).

**`[perso]_seo_new.json` = fichier de travail TRANSITOIRE.** On l'écrit pour linter et appliquer, puis on le SUPPRIME après application réussie (`rm`). Il n'est PAS committé : la mémoire durable du cluster vit dans `footprint_log.md` + la note cluster (§15) + Shopify live. L'arbre ne doit jamais accumuler plus d'un `_seo_new.json` (le cluster en cours / en attente).

---

## 10. Blocs de specs standardisés par type de produit

Ces blocs sont identiques pour tous les personnages du même type de produit. C'est du contenu structuré standardisé : Google ne le pénalise pas comme duplicate.

### Mug
```html
<ul>
  <li>Format : 340ml (idéal thé/café)</li>
  <li>Matière : Céramique blanche premium</li>
  <li>Entretien : Compatible micro-ondes et lave-vaisselle</li>
  <li>Impression : Sublimation inaltérable</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
```

### Tableau / Affiche / Cadre
```html
<ul>
  <li>Affiche : Impression HD sur papier photo premium 200g (du 10x15 au 50x70cm)</li>
  <li>Tableau : Toile tendue sur châssis bois FSC (21x29cm)</li>
  <li>Cadre : Finition noir ou blanc, avec vitre verre ou plexiglas léger</li>
  <li>Exclusivité : Dessin 100% artisanal, encres anti-UV, sans IA (Made in Anjou)</li>
</ul>
```

### Tapis de Souris
```html
<ul>
  <li>Dimensions : 22x18 cm (épaisseur 2mm)</li>
  <li>Matière : Surface polyester pour glisse optimale</li>
  <li>Maintien : Base en caoutchouc antidérapant</li>
  <li>Impression : Sublimation inaltérable</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
```

### Chiffonnette
```html
<ul>
  <li>Dimensions : 18x15 cm</li>
  <li>Matière : Microfibre ultra-douce</li>
  <li>Usage : Nettoie lunettes et écrans sans rayer</li>
  <li>Entretien : Lavable en machine</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
```

### Tote Bag
```html
<ul>
  <li>Surface : Tissu satiné épais (280g)</li>
  <li>Dimensions : 36x33cm</li>
  <li>Impression : Sublimation brillante inaltérable</li>
  <li>Entretien : Lavage à 30° max</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
```

### Magnet
```html
<ul>
  <li>Dimensions : Diamètre 5 cm</li>
  <li>Matière : Coque métal rigide</li>
  <li>Finition : Mylar glossy ultra-brillant et protecteur</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
```

### Porte Clé
```html
<ul>
  <li>Dimensions : Médaillon 3x4 cm</li>
  <li>Matière : Métal robuste, anneau solide de 3cm</li>
  <li>Impression : Sublimation haute définition</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
```

---

## 13. Checklist avant de publier un cluster de descriptions

### Unicité inter-produits (erreurs Goldorak)
- [ ] Aucune intro ne commence par la même structure entre les produits "Vaisseau" du cluster
- [ ] Aucune date (ex : "1978") ne revient plus d'une fois dans les P2 du cluster
- [ ] Aucune P2 "Vaisseau" n'utilise le même angle d'information (design, reconnaissance, lore, popularité...)
- [ ] Aucune P2 ne commence par la même construction de phrase entre produits

### Orthographe et langue
- [ ] Tous les verbes d'imperatif sont orthographiés correctement : "Savourez" (pas "Savorez"), "Offrez", "Portez"... — vérifier lettre à lettre chaque CTA
- [ ] Aucune faute d'accord ou de conjugaison dans les CTAs

### Structure HTML
- [ ] Aucune balise H dans le descriptionHtml
- [ ] Aucun tiret long (—) dans le texte narratif
- [ ] Format : `<p>intro</p><ul><li>...</li></ul><p>P2</p><p>CTA</p>` uniquement

### Keywords
- [ ] Méta titres : keyword le plus cherché en premier (vérifié sur Semrush — données produit, pas franchise)
- [ ] Méta titres sans "| Les Bois d'Aurore"
- [ ] Méta descriptions < 155 caractères
- [ ] Méta descriptions avec angles différents entre elles

### Contenu
- [ ] Chaque description a un angle d'ouverture unique (pas de copie entre produits)
- [ ] "[perso] [franchise]" (ou keyword produit-niveau) apparaît dans chaque intro
- [ ] Tous les CTAs utilisent des verbes différents
- [ ] Vouvoiement respecté
- [ ] Aucune description de l'illustration (risque d'hallucination)
- [ ] "inspiré de" et non "tiré de" pour les oeuvres non officielles
- [ ] Identité : Les Bois d'Aurore = UNE SEULE illustratrice (la propriétaire). Ne jamais accoler "illustré à la main en Anjou" et "pour les fans" dans la même proposition — séparer les deux idées. Ex. INTERDIT : "illustré à la main en Anjou pour les vrais fans". Ex. OK : "illustré à la main en Anjou. Un accessoire fait pour les vrais fans."

### Fichiers
- [ ] PAS de backup (§9 : règle abrogée)
- [ ] Fichier `[perso]_seo_new.json` (transitoire) écrit avec toutes les descriptions AVANT présentation à l'utilisateur
- [ ] Si corrections demandées : fichier mis à jour AVANT d'appliquer sur Shopify
- [ ] Après application réussie : `rm [perso]_seo_new.json` (non committé — voir §9)

---

## 15. Clusters terminés

| Cluster | Date | N | Keyword méta | Suffixes (Mug/Tab/PK/Chiff/Tapis/Tote/Magnet/TShirt) | 301 |
|---|---|---|---|---|---|
| T-Shirt Dessin | 2026-06-17 | 39 | — | — | — |
| Goldorak | 2026-06-17 | 13 | goldorak | — | — |
| Solo Leveling Arise | 2026-06-17 | 8 | — | — | — |
| Shadow the Hedgehog | 2026-06-17 | 8 | shadow sonic (9900) | — | — |
| KPop DH (cluster) | 2026-06-17 | 8 | — | — | — |
| Akaza (DS) | 2026-06-17 | 7 | — | — | — |
| Rumi (KPop DH) | 2026-06-18 | 6 | rumi kpop demon hunters (14800) | — | — |
| Zenitsu (DS) | 2026-06-18 | 7 | zenitsu demon slayer | Tab=Poster Zenitsu | — |
| Nezuko (DS) | 2026-06-18 | 8 | nezuko | — | — |
| Trafalgar Law (OP) | 2026-06-18 | 7 | — | — | — |
| Ace (OP) | 2026-06-18 | 7 | ace one piece (6600) | — | 4 |
| Asuna+duo (SAO) | 2026-06-18 | 14 | asuna | — | — |
| Carnets Apothicaire | 2026-06-18 | 7 | les carnets apothicaire (60500) | — | 7 |
| Boruto | 2026-06-18 | 7 | boruto (22200) | Tab=Poster Boruto | — |
| Gaara | 2026-06-18 | 7 | gaara (9900) | Tab=Poster Gaara | — |
| Ulquiorra (Bleach) | 2026-06-18 | 7 | ulquiorra (3600) | — | 1 |
| Shinobu (DS) | 2026-06-18 | 7 | shinobu (14800) | Tab=Poster Shinobu Kocho | 7 |
| Muzan (DS) | 2026-06-18 | 7 | muzan (8100) | — | 7 |
| Goku Nuage Magique (DB) | 2026-06-18 | 5 | goku nuage magique (170) | — | — |
| Goku Enfant/Sangoku (DB) | 2026-06-18 | 7 | sangoku (14800) | Mug=Mug Sangoku / Tab=Poster Goku Enfant / Tshirt=T-Shirt Sangoku | 2 |
| Goku Shenron (DB) | 2026-06-19 | 7 | goku shenron (30) | Mug=Tasse Céramique / Tab=Poster & Toile / PK=Breloque Métal / Chiff=Chiffon Lunettes / Tapis=Tapis Gamer / Tote=Sac Satiné / Magnet=Aimant Frigo | 7 |
| Vegeta SSJ4 (DB) | 2026-06-19 | 7 | vegeta ssj4 (590) | Mug=Chope 340ml / Tab=Affiche & Cadre / PK=Médaillon Métal / Chiff=Lingette Écran / Tapis=Base Antidérapante / Tote=Cabas Coton / Magnet=Aimant Collector | 0 |
| Vegeta SSJ (DB) | 2026-06-19 | 7 | vegeta ssj (880) | Mug=Tasse à Café / PK=Porte-clé Acier / Chiff=Microfibre Douce / Tapis=Tapis XXL / Tote=Sac Tissu / Magnet=Aimant Métal / Tshirt=Adulte & Enfant | 5 |
| Gohan SSJ2 (DB) | 2026-06-19 | 7 | gohan ssj2 (1900) | Mug=Tasse DBZ / Tab=Toile Tendue / PK=Médaillon Acier / Chiff=Chiffon Optique / Tapis=Tapis DBZ / Tote=Sac Toile / Magnet=Aimant DBZ | 2 |
| Evoli (Pokémon) | 2026-06-19 | 8 | evoli (18100) | Mug=Tasse Evoli / Tab=Affiche & Toile / PK=Breloque Métal / Chiff=Microfibre Douce / Tapis=Tapis Gaming / Tote=Sac Satiné / Magnet=Aimant Collector / Tshirt=Du S au XXL | 1 |
| Hisoka (HxH) | 2026-06-19 | 7 | hisoka (9900) | Mug=Tasse HxH / Tab=Poster & Toile / PK=Breloque Métal / Chiff=Chiffon Lunettes / Tapis=Tapis Gaming / Tote=Sac Satiné / Magnet=Aimant HxH | 0 |
| Meruem (HxH) | 2026-06-19 | 6 | meruem (4400) | Mug=Tasse Céramique / Tab=Affiche & Cadre / PK=Médaillon Métal / Chiff=Lingette Écran / Tapis=Tapis Gamer / Magnet=Aimant Collector | 0 |
| Guts (Berserk) | 2026-06-19 | 8 | guts berserk (5400) | Mug=Tasse Céramique / Tab=Affiche & Toile / PK=Breloque Métal / Chiff=Microfibre Douce / Tapis=Tapis Gaming / Tote=Sac Satiné / Magnet=Aimant Collector / Tshirt=Du S au XXL | 6 |
| Dark Magician Girl (YGO) | 2026-06-19 | 7 | dark magician girl (1900 EN) | Mug=Tasse Yu-Gi-Oh / Tab=Affiche & Toile / PK=Médaillon Métal / Chiff=Microfibre Douce / Tapis=Tapis Gaming / Tote=Sac Satiné / Magnet=Aimant YGO | 0 |
| Saitama (OPM) | 2026-06-19 | 7 | saitama one punch man (720) | Mug=Tasse Céramique / Tab=Affiche & Toile / PK=Médaillon Métal / Chiff=Microfibre Douce / Tapis=Tapis Gaming / Tote=Sac Satiné / Magnet=Aimant Collector | 6 |
| Makima (CSM) | 2026-06-19 | 6 | makima chainsaw man (1300) | Mug=Tasse Céramique / Tab=Affiche & Toile / PK=Médaillon Métal / Chiff=Microfibre Douce / Tapis=Tapis Gamer / Magnet=Aimant Collector | 0 |
| Rudo (Gachiakuta) | 2026-06-19 | 6 | rudo gachiakuta (1300) | Mug=Chope 340ml / Tab=Affiche & Cadre / PK=Acier Collector / Chiff=Chiffon Lunettes / Tapis=Tapis Gaming / Magnet=Aimant Métal | 6 |
| Dragon Ball Super | 2026-06-19 | 6 | dragon ball super | Mug=Tasse Céramique / Tab=Affiche & Toile / PK=Acier Collector / Chiff=Chiffon Lunettes / Tapis=Tapis Gaming / Magnet=Aimant Frigo | 0 |
| Akeno Himejima (HS DxD) | 2026-06-20 | 6 | akeno himejima | Mug=Chope 340ml / Tab=Affiche & Cadre / PK=Médaillon Métal / Chiff=Lingette Écran / Tapis=Tapis Gamer / Magnet=Aimant Métal | 5 |
| Haikyuu | 2026-06-20 | 6 | poster haikyuu (50) | Mug=Tasse Manga / Tab=Affiche & Toile / PK=Médaillon Métal / Chiff=Microfibre Douce / Tapis=Base Antidérapante / Magnet=Aimant Métal | 0 |
| Elden Ring | 2026-06-20 | 6 | tableau/tapis elden ring | Mug=Tasse Jeu Vidéo / Tab=Poster & Affiche / PK=Médaillon Métal / Chiff=Microfibre Douce / Tapis=Tapis Gaming / Magnet=Aimant Collector | 0 |
| Cowboy Bebop | 2026-06-20 | 6 | poster cowboy bebop (90+110) | Mug=Tasse Anime / Tab=Affiche & Toile / PK=Médaillon Métal / Chiff=Microfibre Douce / Tapis=Tapis Gaming / Magnet=Aimant Collector | 0 |
| Kimetsu no Yaiba (groupe) | 2026-06-20 | 6 | kimetsu no yaiba | Mug=Tasse Céramique / Tab=Affiche & Toile / PK=Acier Collector / Chiff=Microfibre Douce / Tapis=Tapis Gaming / Magnet=Aimant Collector | 0 |
| Mira (KPop DH) | 2026-06-22 | 6 | mira kpop demon hunters (8100) | — | — |
| Zoey (KPop DH) | 2026-06-22 | 6 | zoey kpop demon hunters (12100) | — | — |

**À traiter :**
- Demon Slayer : Inosuke, Tanjiro, Rengoku, Doma
- One Piece : (autres persos)
- Dragon Ball : (autres persos)
- Naruto/Boruto : Sarada Uchiha, Hinata
- Bleach : (autres persos)
- KPop DH : Huntrix
- Pokémon : Pikachu (vérifier mug existant)
- SAO : (autres persos)

---

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

## R6. Procédure Semrush détaillée (database: fr)

**RÈGLE D'OR — preuve fraîche obligatoire :** AUCUN volume (y compris "= 0") affirmé sans un résultat Semrush lancé DANS LA SESSION COURANTE. Le keyword qui ouvre CHAQUE méta titre = gagnant prouvé cette session, consigné dans `semrush_data` du JSON. Rappel param : `phrase_these`/`phrase_fullsearch` utilisent le champ `phrase` (accents OK dans phrase, jamais dans un alias GraphQL).

**3.1 — Découverte large (en premier, à LIRE ligne par ligne) :**
`phrase_fullsearch → "[perso]"` (toutes les phrases + volumes) ; `phrase_related → "[perso]"`. Remonte les combos "[produit] [perso]" à volume imprévus. Si peu de retour → tester manuellement tous les synonymes en 3.2.

**3.1bis — NOMS ALTERNATIFS (angle mort fréquent) :** lister TOUS les alias (épithète/titre, romanisations, nom EN/FR, forme/transformation) et lancer fullsearch + balayage 3.2 sur chacun à volume. Deux issues : (1) "[produit] [alias]" à volume → peut ouvrir/enrichir le méta titre ; (2) alias nu à volume informationnel/lore seulement → va dans le TEXTE (P1/P2), jamais le méta titre.

**3.2 — UNE seule requête `phrase_these` globale (tous types en un appel) :**
🔴 **GATE NOM NU** : `[perso]` = le nom SEUL (`mira`, `shadow`), JAMAIS nom+franchise. `mug mira` et non `mug mira kpop demon hunters`. (Vécu : Mira/Zoey conclu « NOTHING FOUND » à tort.)
🔴 **GATE ORDRE DES MOTS** : `phrase_fullsearch` (3.1) couvre déjà les deux ordres. Pour phrase_these : on teste l'ordre "[produit] [perso]" (le plus cherché en FR) — si fullsearch n'a rien remonté sur un type, l'absence = 0 implicite.

Construire **une seule** requête `phrase_these` avec tous les synonymes :

`mug [perso];tasse [perso];gobelet [perso];chope [perso];tableau [perso];poster [perso];affiche [perso];toile [perso];cadre [perso];tapis de souris [perso];tapis souris [perso];tapis gaming [perso];tapis gamer [perso];tapis xxl [perso];chiffonnette [perso];chiffon lunettes [perso];chiffon [perso];microfibre [perso];tote bag [perso];sac [perso];sac toile [perso];cabas [perso];magnet [perso];aimant [perso];aimant frigo [perso];porte clé [perso];porte-clé [perso];porte clef [perso];t shirt [perso];tee shirt [perso];tshirt [perso]`

Lire les résultats : toute ligne avec volume > 0 = winner potentiel. Absence d'un type = 0 confirmé. Garder la table de synonymes ci-dessus en tête si un type manque et qu'on veut creuser.

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
- 🔴 **RACCOURCIR quand l'épithète/franchise est superflue** et que le nom nu est le keyword dominant (cf. GATE nom nu 3.2). Ex : `mug shadow the hedgehog` → H1 « Mug Shadow » + handle `mug-shadow` ; `magnet muzan kibutsuji` → « Magnet Muzan » + `magnet-muzan`. Le méta titre peut, lui, garder la forme longue pour Google si elle aide. Garder la forme longue UNIQUEMENT si le nom nu est ambigu ou sans volume.
- Modifier le handle (+ créer 301) si : nom nu dominant (raccourcir), handle ≠ slug du keyword dominant, perso ambigu, incohérence intra-cluster. Procédure : `productUpdate` handle/title → `urlRedirectCreate` `{ path: "/products/[ancien]", target: "/products/[nouveau]" }` → MAJ liens maillage dans le JSON → batch aliases GraphQL. **JAMAIS changer un handle sans 301.**

**Étape 4 — Écrire le fichier `[perso]_seo_new.json`** AVANT de présenter. Bloc `semrush_data` OBLIGATOIRE en tête (volumes + gagnant par produit). Par produit (130-160 mots de prose unique) : P1 intention + keyword tôt (structure variée) + intention large ; P2 lore LSI distinct ; specs (bloc §10) ; P3 artisan en gras (banque R2, tournante) ; CTA registre varié.

**Étape 6.5 — LINT OBLIGATOIRE :** `python3 /home/user/Personnal/seo_lint.py [perso]_seo_new.json`. **1 FAIL = interdiction d'appliquer.** Corriger, relancer, appliquer sur exit code 0 seulement. Re-lint après toute correction.

**Étape 7 — Appliquer en batch GraphQL :** `productUpdate` par lots de 2-4. Champs `descriptionHtml` + `seo { title description }`. **CRITIQUE : toujours passer `title` ET `description` ensemble — passer seul `title` efface la description.**

**Étape 7.5 — Alt texts :** récupérer IDs via `{ product(id:$id){ media(first:10){ nodes{ ... on MediaImage { id image { altText } } } } } }`. Mutation : **`fileUpdate`** (PAS `productUpdateMedia` — dépréciée). Format alt text : `[Produit] [Perso] [Franchise] illustré à la main en Anjou`. Tableau : conserver le type (Cadre Noir / Poster / Affiche). Jamais décrire l'illustration.

**Étape 8 — Commit + nettoyage :** PAS de backup, PAS de `_seo_new` committé (§9 : fichier transitoire). MAJ footprint_log.md (6 lignes) + entrée cluster (§15), puis `git add footprint_log.md seo_methodology.md` → commit `SEO rewrite: cluster [Perso] — N produits` → `git push -u origin [branche active]`. Enfin `rm [perso]_seo_new.json` pour garder l'arbre propre (Shopify = source de vérité).

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

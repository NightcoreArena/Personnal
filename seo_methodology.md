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

## 15. Ordre de priorité pour les clusters suivants

Traiter par franchise, pas par type de produit (pour garder la cohérence topique) :

**Demon Slayer** (cluster par cluster) :
- [x] Akaza — 7 produits traités (2026-06-17)
- [x] Zenitsu — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Maillage vérifié (métachamps OK). Tableau méta titre = "Poster Zenitsu" (à confirmer Semrush).
- [ ] Inosuke
- [ ] Tanjiro
- [x] Nezuko — 8 produits traités (2026-06-18) : Mug, Poster, Porte Clé, T-Shirt, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Maillage vérifié (métachamps OK). Intentions larges intégrées (cadeau DS 210/mois, poster DS 720/mois, t-shirt manga 720/mois, goodies manga 210/mois).
- [ ] Rengoku
- [ ] Doma
- [ ] (autres personnages DS)

**Pokémon** :
- [x] Pikachu (mug existant, à vérifier)
- [ ] (autres personnages Pokémon)

**Kpop Demon Hunter** :
- [x] Cluster complet — 8 produits traités (2026-06-17) : Mug, Tableau, Tapis de Souris, Chiffonnette, Tote Bag, Magnet, Porte Clé, T-Shirt
- [x] Rumi — 6 produits traités (2026-06-18) : Mug, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Pas de Tableau. Keyword principal : rumi kpop demon hunters (14800/mois). Erreurs factuelles corrigées (Tapis + Magnet décrivaient Mirko/MHA). Backup → rumi_backup.json, fichier final → rumi_seo_new.json.
- [x] Mira — 6 produits traités (2026-06-22) : Mug, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Keyword principal : mira kpop demon hunters (8100/mois). Backup → mira_backup.json, fichier final → mira_seo_new.json.
- [x] Zoey — 6 produits traités (2026-06-22) : Mug, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Keyword principal : zoey kpop demon hunters (12100/mois). Backup → zoey_backup.json, fichier final → zoey_seo_new.json.
- [ ] Huntrix (personnage individuel)

**Solo Leveling Arise** :
- [x] Cluster complet — 8 produits traités (2026-06-17) : Mug, Tableau (renommé Arise), Tapis de Souris, Chiffonnette, Tote Bag, Magnet, Porte Clé, T-Shirt Sung Jinwoo
- Note : "Tableau Solo Leveling" → renommé "Tableau Solo Leveling Arise" (Option A, cohérence cluster)
- Note : T-Shirt Sung Jinwoo corrigé (bug "Mao Mao" dans méta description)

**Goldorak** :
- [x] Cluster complet — 13 produits traités (2026-06-17) : Mug, Mug Vaisseau, Tableau, Tableau Vaisseau, T-Shirt, Porte Clé, Porte Clé Vaisseau, Chiffonnette, Chiffonnette Vaisseau, Tapis de Souris, Tapis de Souris Vaisseau, Magnet, Magnet Vaisseau
- Note : Goldorak = franchise solo → keywords "[produit] goldorak" appartiennent aux pages produit (pas aux collections)
- Note : Backup → goldorak_backup.json (originaux avant réécriture)

**Shadow the Hedgehog** :
- [x] Cluster complet — 8 produits traités (2026-06-17) : Mug, Tableau, T-Shirt, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT)
- Note : "shadow sonic" (9 900/mois) > "shadow the hedgehog" (4 400/mois) → keyword secondaire dans méta titres
- Note : Volumes product-level quasi nuls → stratégie cluster topique uniquement
- Note : Backup → shadow_backup.json, fichier final → shadow_seo_new.json

**One Piece** :
- [x] Trafalgar Law — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Intentions larges intégrées (cadeau one piece 1300/mois, poster one piece 1900/mois, mug one piece 880/mois). Backup → law_backup.json, fichier final → law_seo_new.json.
- [x] Ace — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : ace one piece (6600/mois). Cluster topique pur. Handles uniformisés en *-ace-one-piece + 4x301. 10 alt texts mis à jour. Fichier final → ace_seo_new.json.
- [ ] (autres personnages One Piece)

**Sword Art Online** :
- [x] Asuna (solo + duo Asuna & Kirito) — 14 produits traités (2026-06-18) : 7 solo (Mug, Tableau, Porte Clé, Chiffonnette, Tapis, Magnet, Tote Bag DRAFT) + 7 duo. Volumes [produit] asuna quasi nuls — stratégie cluster topique pur. 22 alt texts mis à jour. Backup → asuna_backup.json, fichier final → asuna_seo_new.json.
- [ ] (autres personnages SAO)

**Les Carnets de l'Apothicaire** :
- [x] Cluster complet — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Keyword principal : les carnets de l'apothicaire (60 500/mois). Volumes [produit] = 0 → cluster topique pur. Handles renommés de carnet → les-carnets + 7×301 redirects. 11 alt texts mis à jour. Fichier final → carnets_seo_new.json.

**Boruto / Naruto** :
- [x] Boruto Uzumaki — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : boruto (22200/mois). Cluster topique pur. Poster boruto (20/mois) > tableau/affiche (20, tied) → méta titre Tableau = "Poster Boruto". 11 alt texts mis à jour. Fichier final → boruto_seo_new.json.
- [x] Gaara — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : gaara (9900/mois), gaara naruto (1600/mois). Cluster topique pur. Poster gaara (20/mois, tied avec tableau) → méta titre Tableau = "Poster Gaara". Sac gaara (20/mois) → suffixe Tote Bag. Balayage synonymes exhaustif (table 3.2 complète + fullsearch). 10 alt texts mis à jour (Tote Bag DRAFT sans image). Fichier final → gaara_seo_new.json.
- [ ] Sarada Uchiha
- [ ] Hinata

**Bleach** :
- [x] Ulquiorra Schiffer — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet, Tote Bag (DRAFT). Keyword principal : ulquiorra (3600/mois) > ulquiorra schiffer (2900/mois). Cluster topique pur. H1 courts uniformisés sur "ulquiorra" (sans "Schiffer"). Handle porte-cle-ulquiorra-schiffer → porte-cle-ulquiorra + 1×301. 11 alt texts mis à jour. Fichier final → ulquiorra_seo_new.json.
- [ ] (autres personnages Bleach)

**Demon Slayer** :
- [x] Shinobu Kocho — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : shinobu (14800/mois), shinobu kocho (4400/mois). Cluster topique pur. Poster shinobu kocho (20/mois) → méta titre Tableau = "Poster Shinobu Kocho". Handles renommés : suppression -pilier-insecte sur 7 produits + 7×301. 10 alt texts mis à jour (Tote Bag DRAFT sans image). Fichier final → shinobu_seo_new.json.
- [x] Muzan Kibutsuji — 7 produits traités (2026-06-18)

**Dragon Ball** (cluster par cluster) :
- [x] Goku Nuage Magique — 5 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris. Keyword : goku nuage magique (170/mois). Cluster topique pur (kintoun = 0, tous combos = NOTHING FOUND). Handles OK (pas de renommage). 10 alt texts mis à jour. Franchise : Dragon Ball > DBZ pour les méta. Fichier final → goku_nuage_magique_seo_new.json. : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : muzan (8100/mois), muzan kibutsuji (2400/mois). Cluster 100% topique pur (tous combos produit = NOTHING FOUND). Handles renommés : suppression -kibutsuji sur 7 produits + 7×301. 11 alt texts mis à jour (Tote Bag DRAFT sans image). Alias 3.1bis : muzan jackson (480) et muzan michael jackson (260) = informationnel seulement. Fichier final → muzan_seo_new.json.

- [x] Goku Enfant / Sangoku — 7 produits traités (2026-06-18) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, T-Shirt, Magnet. Keyword : sangoku (14800/mois), goku enfant (480/mois). Cluster topique pur — DÉCOUVERTE : t shirt sangoku (110/mois) et poster goku (70/mois) → méta T-Shirt = "T-Shirt Sangoku", méta Tableau = "Poster Goku Enfant", méta Mug = "Mug Sangoku" (mug sangoku = mug goku = 20). Handles renommés : magnet-goku → magnet-goku-enfant, t-shirt-goku → t-shirt-goku-enfant + 2×301. 13 alt texts mis à jour. Fichier final → goku_enfant_seo_new.json.
- [x] Goku Shenron — 7 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : goku shenron (30/mois). Cluster 100% topique pur (tous combos = 0). ⚠️ Cluster "Shenron" distinct déjà existant (dragon seul) → ce cluster = duo Goku enfant sur Shenron. Handles renommés : [produit]-goku-dragon-enfant → [produit]-goku-shenron + 7×301. Suffixes méta variés anti-redondance inter-cluster DB : Tasse Céramique / Poster & Toile / Breloque Métal / Chiffon Lunettes / Tapis Gamer / Sac Satiné / Aimant Frigo. 11 alt texts mis à jour. Fichier final → goku_shenron_seo_new.json.
- [x] Vegeta SSJ4 — 7 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : vegeta ssj4 (590/mois). Cluster 100% topique pur (tous combos = NOTHING FOUND). Alias : vegeta super saiyan 4 (320) → LSI texte uniquement. 0 handle renommé. Suffixes méta : Chope 340ml / Affiche & Cadre / Médaillon Métal / Lingette Écran / Base Antidérapante / Cabas Coton / Aimant Collector. 11 alt texts mis à jour. Fichier final → vegeta_ssj4_seo_new.json.
- [x] Vegeta SSJ (= "Vegeta") — 7 produits traités (2026-06-19)
- [x] Gohan SSJ2 — 7 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : gohan ssj2 (1900/mois). Cluster topique pur (tous combos = 0 sauf poster gohan ssj2 = 20). Handle Tableau corrigé : gohan-ssj2-poster → tableau-gohan-ssj2 + 2×301 (cadre-gohan-ssj2 mis à jour). Suffixes méta : Tasse DBZ / Toile Tendue / Médaillon Acier / Chiffon Optique / Tapis DBZ / Sac Toile / Aimant DBZ. GATE anti-footprint appliquée (12/12 collisions corrigées vs Vegeta SSJ). 11 alt texts mis à jour. Fichier final → gohan_ssj2_seo_new.json. : Mug, T-Shirt, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. ⚠️ Pas de Tableau dans ce cluster. Keyword : vegeta ssj (880/mois) ; WINNER cluster = t shirt vegeta (110/mois). H1 uniformisés sur "Vegeta" (suppression "SSJ"). 5 handles renommés : mug/pk/chiff/tapis/tote-bag-vegeta-ssj → -vegeta + 5×301. Suffixes méta : Tasse à Café / Adulte & Enfant / Porte-clé Acier / Microfibre Douce / Tapis XXL / Sac Tissu / Aimant Métal. 9 alt texts mis à jour. Fichier final → vegeta_ssj_seo_new.json.

**Pokémon** :
- [x] Evoli — 8 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, T-Shirt, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : evoli (18100/mois). DÉCOUVERTE : tasse evoli (40) > mug evoli (20) → méta Mug = "Tasse Evoli". sac evoli (170/mois) → méta Tote Bag = "Sac Evoli". t shirt evoli (30/mois) → méta T-Shirt. poster evoli (20/mois) → méta Tableau. 1 handle renommé : t-shirt-pokemon-enfant → t-shirt-evoli + 1×301. Suffixes méta : Mug Céramique / Affiche & Toile / Du S au XXL / Breloque Métal / Microfibre Douce / Tapis Gaming / Tote Bag Satiné / Aimant Collector. PREMIÈRE franchise Pokémon : broad-intent consigné au ledger. 13 alt texts mis à jour (Tote Bag DRAFT sans image). Fichier final → evoli_seo_new.json.

**Hunter x Hunter** :
- [x] Hisoka — 7 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : hisoka (9900/mois). Combos produit : mug/tapis/porte-clé/poster hisoka = 20/mois ; chiff/tote bag/magnet = 0 (topique). 0 handle renommé. Suffixes méta : Tasse HxH / Poster & Toile / Breloque Métal / Chiffon Lunettes / Tapis Gaming / Sac Satiné / Aimant HxH. PREMIÈRE franchise HxH : intentions larges mesurées (poster hxh/hunter x hunter 210/mois, t shirt hxh 210/mois) et consignées au ledger. 10 alt texts mis à jour (Tote Bag DRAFT sans image). Fichier final → hisoka_seo_new.json.
- [x] Meruem — 6 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet (pas de Tote Bag ni T-Shirt). Keyword : meruem (4400/mois). Combos produit testés DANS LES 2 ORDRES DE MOTS : seul "meruem poster" 20 + "poster meruem" 10 (~30) ressort, tout le reste = 0 → cluster topique pur. "roi des fourmis" polysémique → texte uniquement. 0 handle/title renommé. Suffixes méta : Tasse Céramique / Affiche & Cadre / Médaillon Métal / Lingette Écran / Tapis Gamer / Aimant Collector (tous ≠ Hisoka). 10 alt texts mis à jour. 2e cluster HxH : broad-intent réutilisé du ledger. LEÇON : GATE ordre des mots ajoutée au CLAUDE.md (Étape 3.2). Fichier final → meruem_seo_new.json.

**Berserk** :
- [x] Guts Berserk — 8 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, T-Shirt, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : guts berserk (5400/mois). Alias "Black Swordsman" (2900) = informationnel, tissé dans le texte. Cluster 100% topique pur. 6 handles corrigés (fautes "bersek"→"berserk" + manque "guts") + 6×301. T-Shirt title corrigé (parenthèses supprimées). Suffixes méta : Tasse Céramique / Affiche & Toile / Breloque Métal / Du S au XXL / Microfibre Douce / Tapis Gaming / Sac Satiné / Aimant Collector. PREMIÈRE franchise Berserk : broad-intent consigné au ledger. 13 alt texts mis à jour (Tote Bag DRAFT sans image). Fichier final → guts_berserk_seo_new.json.

**Yu-Gi-Oh!** :
- [x] Dark Magician Girl (Magicienne des Ténèbres) — 7 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Keyword : dark magician girl (1900/mois EN) > magicienne des ténèbres (590/mois FR). Méta titres en EN car volume 3x supérieur (nom propre international, pas un anglicisme produit). Cluster 100% topique pur (tous combos = NOTHING FOUND). 0 handle renommé. Suffixes méta : Tasse Yu-Gi-Oh / Affiche & Toile / Médaillon Métal / Microfibre Douce / Tapis Gaming / Sac Satiné / Aimant YGO. (PK corrigé 2026-06-19 : Breloque Métal → Médaillon Métal) PREMIÈRE franchise Yu-Gi-Oh! : broad-intent consigné au ledger. 10 alt texts mis à jour (Tote Bag DRAFT sans image). Fichier final → dark_magician_girl_seo_new.json.

**One Punch Man / OPM** :
- [x] Saitama — 7 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Tote Bag (DRAFT), Magnet. Exclus : Tote Bag Genos (autre perso). Keyword : saitama one punch man (720/mois combiné). "saitama" seul polysémique (ville japonaise) → toujours combiner avec "One Punch Man" dans les méta titres. Cluster quasi-topique pur (mug saitama 20 et poster saitama 20 seulement). "poster one punch man" (70) = keyword COLLECTION, non utilisé en méta titre fiche. 6 handles renommés (one-punch-man → saitama) + 6×301. Tableau title corrigé ("Tableau One Punch Man" → "Tableau Saitama"). Suffixes méta : Tasse Céramique / Affiche & Toile / Médaillon Métal / Microfibre Douce / Tapis Gaming / Sac Satiné / Aimant Collector. PREMIÈRE franchise OPM : broad-intent consigné au ledger. 11 alt texts mis à jour (Tote Bag DRAFT sans image). Fichier final → saitama_seo_new.json.

**Chainsaw Man** :
- [x] Makima — 6 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet (pas de Tote Bag ni T-Shirt). Keyword : makima chainsaw man (1300/mois) — "makima" seul 8100 mais NSFW-contaminé, toujours combiner avec "Chainsaw Man" dans les méta titres. Combos produit : poster makima (20) seul non-nul, tous les autres à 0. "makima mousepad" 20 = anglicisme interdit → Tapis de Souris retenu. "makima is listening" (880) = capté par Tapis P2 + CTA. "why did makima kill power" (40) = top question → P2 Chiffonnette (Power sacrifiée pour briser Denji). Organic research (manga-shop.fr) : aucun gap CSM actionnable. 0 handle/title renommé. Suffixes méta : Tasse Céramique / Affiche & Toile / Médaillon Métal / Microfibre Douce / Tapis Gamer / Aimant Collector. PREMIÈRE franchise Chainsaw Man : broad-intent consigné au ledger. 10 alt texts mis à jour. Fichier final → makima_seo_new.json.

**Gachiakuta** :
- [x] Rudo (Rudo Surebrec) — 6 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet. Keyword : rudo gachiakuta (1300/mois combiné) — "rudo" seul polysémique (film espagnol), "gachiakuta" seul utilisable mais toujours combiner. Combos produit : poster gachiakuta (30) seul non-nul → Tableau méta titre commence par "Poster". Questions lore : "is amo dead in gachiakuta" 30 → Amo mentionnée Magnet P2. Lore clé : Sacred (outil de nettoyage → arme), Le Gouffre, la Sphère, rage mode. 6 handles renommés (-gachiakuta → -rudo-gachiakuta) + 6×301. Suffixes méta : Chope 340ml / Affiche & Cadre / Acier Collector / Chiffon Lunettes / Tapis Gaming / Aimant Métal. PREMIÈRE franchise Gachiakuta : broad-intent consigné au ledger. 10 alt texts mis à jour. Fichier final → rudo_gachiakuta_seo_new.json.

**Dragon Ball Super (groupe illustration)** :
- [x] Dragon Ball Super — 6 produits traités (2026-06-19) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet. Illustration : Goku + Vegeta en Super Saiyan Blue + Shenron (arc DBS). Exception "perso = franchise" (groupe — traité comme Goldorak). Keyword produits : mug dragon ball super (20), dragon ball super poster (90), tapis dragon ball super (20), topique pour PK/Chiff/Magnet. Lore : SSB/ki divin/Beerus, Tournoi de la Puissance/Ultra Instinct, Black Goku/Zamasu, Super Dragon Balls/Shenron cosmique. 0 handle renommé (tous déjà corrects). Suffixes méta : Tasse Céramique / Affiche & Toile / Acier Collector / Chiffon Lunettes / Tapis Gaming / Aimant Frigo. 10 alt texts mis à jour (5 variantes Tableau). Fichier final → dragon_ball_super_seo_new.json.

**Akeno Himejima (High School DxD)** :
- [x] Akeno Himejima — 6 produits traités (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet. Cluster topique pur : tous [produit] akeno himejima = 0, poster high school dxd = 10 (collection). "akeno" seul polysémique (akeno hijama = bien-être, 1000/mois) : "himejima" ajouté partout. 5 handles renommés (mug/pk/magnet/tapis/chiff + "-himejima") + 5×301. Suffixes méta : Chope 340ml / Affiche & Cadre / Médaillon Métal / Lingette Écran / Tapis Gamer / Aimant Métal. Lore : Foudre Sacrée (fusion angélique + ange déchu), "Ara ara~" persona duelle, Baraqiel/Grigori, mère miko tuée, pièce Reine de Rias, Issei Hyoudou. PREMIÈRE franchise High School DxD. 10 alt texts mis à jour (5 variantes Tableau). Fichier final → akeno_himejima_seo_new.json.

**Haikyuu** :
- [x] Haikyuu — 6 produits traités (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet. Personnage illustré : Hinata Shoyo (n°10, Karasuno). Cluster franchise (perso = franchise). Keywords produits : poster haikyuu (50), tapis de souris haikyuu (20), porte clé haikyuu (20), topique pour Mug/Chiff/Magnet. Broad-intent : poster manga (1000), cadeau manga (590), poster anime (590), mug manga (260), goodies manga (210). Lore : synchrone set Hinata/Kageyama/164cm (Mug), Karasuno "Corbeau déclinant"/slogan (Tableau), Petit Géant/héritage (PK), Guerre des Poubelles/Nekoma (Chiff), Nationals vs Inarizaki/jumeaux Miya (Tapis), ambition Petit Géant/moteur de la série (Magnet). 0 handle renommé (poster-haikyuu déjà optimal). Suffixes méta : Tasse Manga / Affiche & Toile / Médaillon Métal / Microfibre Douce / Base Antidérapante / Aimant Métal. PREMIÈRE franchise Haikyuu. 1 produit à traiter séparément : Mug Hinata (handle mug-hinata, cluster Hinata dédié). Alt texts mis à jour. Fichier final → haikyuu_seo_new.json.

**Elden Ring** :
- [x] Elden Ring — 6 produits traités (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet. Cluster franchise jeu vidéo (perso = franchise). Keywords produits : tableau elden ring (110), tapis de souris elden ring (50), mug elden ring (20), topique pour PK/Chiff/Magnet. Broad-intent : cadeau gaming / cadeau jeu vidéo (40), figurine elden ring (720). Lore : George R.R. Martin/Marika/Radahn/Ranni (Mug), Leyndell/Stormveil/Farum Azula/GOTY 2022 (Tableau), Ranni/Ordre Doré/Ère des Étoiles (PK), Malenia/Lame de Miquella/"I have never known defeat" (Chiff), Starscourge Radahn/Léonard/Festival de Radahn/DLC Enir-Ilim (Tapis), Shadow of the Erdtree/Messmer l'Empaleur/fils secret de Marika (Magnet). 0 handle renommé (tous déjà corrects). Suffixes méta : Tasse Jeu Vidéo / Poster & Affiche / Médaillon Métal / Microfibre Douce / Tapis Gaming / Aimant Collector. PREMIÈRE franchise jeu vidéo standalone (angle "cadeau gaming"/"jeu vidéo" à la place de "manga"/"anime"). 10 alt texts mis à jour (5 variantes Tableau). Fichier final → elden_ring_seo_new.json.

**Cowboy Bebop** :
- [x] Cowboy Bebop — 6 produits traités (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet. Cluster topique pur : seuls "poster cowboy bebop" (90) et "cowboy bebop poster" (110) ont du volume. Handle Tableau déjà "poster-cowboy-bebop" (optimal). 0 handle renommé. Lore : Yoko Kanno/The Seatbelts/sessions jazz, Spike Spiegel/Red Dragon/Julia/Vicious/Jeet Kune Do/Swordfish II, Faye Valentine/cryogénie 50 ans/Venus/amnésie, Jet Black/ex-ISSP, fin ambiguë "You're gonna carry that weight". PREMIÈRE franchise Cowboy Bebop. Broad-intent : poster manga (1000), poster anime (590), mug manga (260). Suffixes méta : Tasse Anime / Affiche & Toile / Médaillon Métal / Microfibre Douce / Tapis Gaming / Aimant Collector. 10 alt texts mis à jour (5 variantes Tableau). Fichier final → cowboy_bebop_seo_new.json.

**Kimetsu no Yaiba (groupe illustration)** :
- [x] Kimetsu no Yaiba — 6 produits traités (2026-06-20) : Mug, Tableau, Porte Clé, Chiffonnette, Tapis de Souris, Magnet. Illustration : Tanjiro, Nezuko, Zenitsu et Inosuke dynamique (groupe). Exception "perso = franchise" (groupe — traité comme DBS/Goldorak). Keyword produits : "[produit] demon slayer" appartient aux pages COLLECTION → utiliser "Kimetsu no Yaiba" comme identifiant unique dans les méta titres pour éviter cannibalisation. Combos produit : poster kimetsu no yaiba (140), mug kimetsu no yaiba (0 propre mais couvert via "mug demon slayer" collection). Lore : Tanjiro/souffle de l'eau, Nezuko/Art du Sang Démoniaque, Zenitsu/Souffle de la Foudre, Inosuke/Souffle de la Bête, époque Taishō, Muzan Kibutsuji. 0 handle renommé (tous déjà corrects). Suffixes méta : Tasse Céramique / Affiche & Toile / Acier Collector / Microfibre Douce / Tapis Gaming / Aimant Collector. 10 alt texts mis à jour. Fichier final → kimetsu_no_yaiba_seo_new.json.

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

## R6. Procédure Semrush détaillée (database: fr)

**RÈGLE D'OR — preuve fraîche obligatoire :** AUCUN volume (y compris "= 0") affirmé sans un résultat Semrush lancé DANS LA SESSION COURANTE. Le keyword qui ouvre CHAQUE méta titre = gagnant prouvé cette session, consigné dans `semrush_data` du JSON. Rappel param : `phrase_these`/`phrase_fullsearch` utilisent le champ `phrase` (accents OK dans phrase, jamais dans un alias GraphQL).

**3.1 — Découverte large (en premier, à LIRE ligne par ligne) :**
`phrase_fullsearch → "[perso]"` (toutes les phrases + volumes) ; `phrase_related → "[perso]"`. Remonte les combos "[produit] [perso]" à volume imprévus. Si peu de retour → tester manuellement tous les synonymes en 3.2.

**3.1bis — NOMS ALTERNATIFS (angle mort fréquent) :** lister TOUS les alias (épithète/titre, romanisations, nom EN/FR, forme/transformation) et lancer fullsearch + balayage 3.2 sur chacun à volume. Deux issues : (1) "[produit] [alias]" à volume → peut ouvrir/enrichir le méta titre ; (2) alias nu à volume informationnel/lore seulement → va dans le TEXTE (P1/P2), jamais le méta titre.

**3.2 — Une requête `phrase_these` par type de produit, TOUS les synonymes :**
🔴 **GATE NOM NU** : `[perso]` dans la table ci-dessous = le nom SEUL du personnage (`mira`, `shadow`, `zoey`), JAMAIS nom+franchise. Tester `mug mira`, **PAS** `mug mira kpop demon hunters` : appender la franchise réduit à une longue traîne quasi vide et fait conclure « 0 » à tort, alors que le combo nu porte le volume réel. La franchise se mesure en 3.3 (intro), pas ici. (Vécu : cluster Mira/Zoey conclu « NOTHING FOUND » par ajout abusif de la franchise au combo produit.)
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
- 🔴 **RACCOURCIR quand l'épithète/franchise est superflue** et que le nom nu est le keyword dominant (cf. GATE nom nu 3.2). Ex : `mug shadow the hedgehog` → H1 « Mug Shadow » + handle `mug-shadow` ; `magnet muzan kibutsuji` → « Magnet Muzan » + `magnet-muzan`. Le méta titre peut, lui, garder la forme longue pour Google si elle aide. Garder la forme longue UNIQUEMENT si le nom nu est ambigu ou sans volume.
- Modifier le handle (+ créer 301) si : nom nu dominant (raccourcir), handle ≠ slug du keyword dominant, perso ambigu, incohérence intra-cluster. Procédure : `productUpdate` handle/title → `urlRedirectCreate` `{ path: "/products/[ancien]", target: "/products/[nouveau]" }` → MAJ liens maillage dans le JSON → batch aliases GraphQL. **JAMAIS changer un handle sans 301.**

**Étape 4 — Écrire le fichier `[perso]_seo_new.json`** AVANT de présenter. Bloc `semrush_data` OBLIGATOIRE en tête (volumes + gagnant par produit). Par produit (130-160 mots de prose unique) : P1 intention + keyword tôt (structure variée) + intention large ; P2 lore LSI distinct ; specs (bloc §10) ; P3 artisan en gras (banque R2, tournante) ; CTA registre varié.

**Étape 6.5 — LINT OBLIGATOIRE :** `python3 /home/user/Personnal/seo_lint.py [perso]_seo_new.json`. **1 FAIL = interdiction d'appliquer.** Corriger, relancer, appliquer sur exit code 0 seulement. Re-lint après toute correction.

**Étape 7 — Appliquer en batch GraphQL :** `productUpdate` par lots de 2-4. Champs `descriptionHtml` + `seo { title description }`. **CRITIQUE : toujours passer `title` ET `description` ensemble — passer seul `title` efface la description.**

**Étape 7.5 — Alt texts :** récupérer IDs via `{ product(id){ media(first:10){ nodes{ ... on MediaImage { id image { altText } } } } } }`. `productUpdateMedia` par lot. Format : `[Produit] [Perso] [Franchise] illustré à la main en Anjou`. Tableau : conserver le type (Cadre Noir / Poster / Affiche). Jamais décrire l'illustration.

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

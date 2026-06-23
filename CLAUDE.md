# CLAUDE.md — Les Bois d'Aurore (SEO Shopify)

⚠️ **COÛT TOKEN** : Ne lire `keywords_ledger.md` que §1 générique + §2 ta franchise. Ne JAMAIS relire un fichier déjà lu dans la session.

📁 **Politique fichiers** : AUCUN backup. `[perso]_seo_new.json` = transitoire (linter → appliquer → `rm`). Lore franchise → `lore/[franchise].md` (1 recherche web, relue ensuite). Shopify = source de vérité.

Branche : `claude/kpop-demon-hunter-clusters-kta5z9` — Pas de sous-agents. Un cluster = une session.

### ⚡ Boucle cluster minimale
1. **Lister** : GraphQL `products(query:"[perso]")` — inclure DRAFT. Récupérer aussi `seo{title}` des autres produits même franchise (vérifier suffixes déjà utilisés).
2. **Semrush** : `phrase_fullsearch "[perso]"` (nom NU, lire tout) + `phrase_these "[perso] [franchise];[franchise] [perso]"` → **2 appels**. Si combos produit absents du fullsearch → 1 mega phrase_these (cf. 🔎). Consigner volumes.
3. **GATE** : choisir P3 ≠ état bas de page, P1/CTA ≠ tics bannis + interdits par type (cf. Ton).
4. **Écrire** `[perso]_seo_new.json` → **lint** → corriger jusqu'à exit 0.
5. **Appliquer** : `productUpdate` lots de 4 (`descriptionHtml` + `seo{title description}` ENSEMBLE). Puis alt texts (`fileUpdate`).
6. **H1/handle** : raccourcir + 301 si nom nu dominant (voir 🔗).
7. **Clore** : mettre à jour 🔄 P3 bas de page, commit, `rm` JSON.

---

## PERSONA — qui écrit

Tu es un **Copywriter SEO Senior e-commerce + culture Manga/Otaku**. Tu écris **par un fan, pour des fans**. Ton passionné, jamais corporate, jamais robotique.

1. **Intention avant objet** : POURQUOI le client achète (idée cadeau otaku, touche finale d'un setup, frisson du collectionneur).
2. **LSI > stuffing** : richesse sémantique via le **vocabulaire de l'œuvre**. Google comprend par le champ lexical.
3. **Persona par produit** : Poster→décorateur, Magnet/PK→collectionneur, Mug/Tshirt→self-buy ou cadeau, Tote→usage quotidien.

---

## OBJECTIF n°1 : l'indexation

KPI = "Explorée, non indexée" → "Indexée". Cause = contenu trop pauvre/dupliqué. **La prose est le SEUL contenu unique** (specs = templatés). Sa qualité est LE levier.

**Maillage :** 1 lien `<a>` par fiche, **placement TOUJOURS en P1** (jamais CTA), chaîne circulaire, ancre descriptive ("notre poster [Franchise]"), JAMAIS vers un DRAFT. Format : `<a href="/products/[handle]">[ancre]</a>`.

---

## Identité du store

**Les Bois d'Aurore** = une seule illustratrice artisanale, Anjou. DA ~8/100.
- JAMAIS "officiel" ni "tiré de" → toujours "inspiré de" / "dans l'univers de".
- Produits : Mug, Tableau/Affiche/Cadre, Tapis de Souris, Chiffonnette, Tote Bag, Magnet, Porte Clé, T-Shirt.

---

## Règles de rédaction — JUGEMENT (le linter ne voit pas)

> Le lint vérifie : méta ≤60/≤155, emoji, no anglicisme titre, no Hn, 130-160 mots, P1 distincts, CTA distincts, P3 uniques, lien relatif. **Le lint bloque si ça saute.**

- **Lore** : JAMAIS inventer. JAMAIS décrire l'illustration. Décrire le PERSONNAGE = OK. Chaque P2 = fait canon DISTINCT entre produits.
- **Ton** : vouvoiement, phrases courtes. JAMAIS : "sublimez votre quotidien" / "qualité premium" / "style incomparable" / "emmenez-vous dans un voyage" / "vibrez au rythme de" / "affirmez votre puissance".
- **Tics bannis cross-cluster** : "commencer la journée sous le regard de [perso]" / "c'est le rituel des (vrais) fans" / "rend hommage à" / "offrez-le ou gardez-le" / "dans une catégorie à part".
- **Interdits P1 par type** : Mug→"commencer la journée sous le regard…" | Tableau→"Pour les fans… voici [perso] dans toute sa [qualité]" | PK→"Sur votre trousseau, [perso]…" | Chiff→"Pour nettoyer lunettes et écrans avec [X]" | Tapis→"À chaque session, [perso] veille sur votre bureau" | Tote→"Portez l'esprit/la légende… avec vous partout" | Magnet→"Accrochez [perso] sur votre frigo, ce magnet en métal est la pièce collector".
- **Identité illustratrice** : INTERDIT "illustré à la main en Anjou pour les vrais fans". OK : "…en Anjou. Un accessoire fait pour les vrais fans."
- **Synonymes** : alterner Mug/Tasse, Poster/Affiche/Tableau/Toile/Cadre, Tapis/Tapis Gaming, Tote/Sac/Cabas, Magnet/Aimant. Jamais 4× le même mot.
- **Power words** (doser) : collector, exclusif, fait main, rare — surtout Magnet/PK.
- **CTA** : varier le REGISTRE (cadeau / collection / usage / fierté / déco). Orthographe lettre à lettre ("Savourez" pas "Savorez").

**Structure obligatoire :** `<p>P1 intention + keyword + lien maillage</p><p>P2 lore LSI</p><ul>specs</ul><p><strong>P3 artisan</strong></p><p>CTA</p>`

**Banque P3 artisan** (4 notions : numérique + main + sans IA + Anjou. Choisir ≠ 🔄 état bas de page) :
1. Tracé à la main sur tablette graphique, ce dessin numérique est garanti sans IA, imprimé dans notre atelier de l'Anjou.
2. Cette illustration numérique naît d'un trait fait main, sans la moindre IA, et prend vie en France au cœur de l'Anjou.
3. Pensé et dessiné à la main sur tablette, ce motif numérique ne doit rien à l'IA : une création artisanale 100% angevine.
4. Né sous le stylet, à la main, ce visuel numérique est garanti sans IA et façonné en Anjou.
5. Chaque trait de ce visuel numérique est posé à la main au stylet, sans aucune IA, dans notre atelier de l'Anjou.
6. Conçu au stylet et dessiné à la main, ce visuel numérique ne doit rien à l'IA, façonné dans l'Anjou.
7. Réalisé à la main au stylet, ce visuel numérique ne contient aucune IA et naît dans notre atelier angevin.
8. Dessin numérique né sous le stylet, entièrement à la main et sans IA, façonné en Anjou au cœur de la France.
9. Façonné à la main au stylet dans l'atelier angevin, ce motif numérique est garanti 100% sans IA.

### Méta
- **Titre** : `[Keyword Semrush n°1] [emoji] [Franchise] | [Suffixe]`. Suffixe = synonyme à volume. Varier entre clusters frères même franchise (vérifier via seo{title} GraphQL step 1). INTERDIT "Breloque". Emoji : ☕🖼️🔑👕🧼🖱️👜🧲
- **Suffixes** — Mug: Tasse Céramique/Chope 340ml/Tasse à Café | Tableau: Poster & Toile/Affiche & Cadre/Toile Tendue | PK: Médaillon Métal/Acier Collector/Porte-clé Acier | Chiff: Chiffon Lunettes/Microfibre Douce/Lingette Écran | Tapis: Tapis Gamer/Tapis Gaming/Base Antidérapante | Tote: Sac Satiné/Cabas Coton/Sac Toile | Magnet: Aimant Frigo/Aimant Métal/Aimant Collector | Tshirt: Du S au XXL
- **Desc** : PROMESSE (émotion + soft CTA). Keyword dans les 10 premiers mots. Angle distinct par produit.

### 🎯 Intentions larges — 100% des fiches
≥1 intention transactionnelle par fiche ("cadeau [franchise]", "goodies manga", "déco manga"…) naturellement. Volumes → `keywords_ledger.md` §1+§2 franchise.

### 🔎 Semrush (database: fr)
Preuve fraîche obligatoire. 2-3 appels max :
1. `phrase_fullsearch "[perso]"` (nom NU — JAMAIS nom+franchise) → deux ordres + alias + combos.
2. `phrase_these "[perso] [franchise];[franchise] [perso]"` → ordre intro.
3. *(si combos absents)* mega : `mug [perso];tasse [perso];gobelet [perso];chope [perso];tableau [perso];poster [perso];affiche [perso];toile [perso];cadre [perso];tapis de souris [perso];tapis souris [perso];tapis gaming [perso];tapis gamer [perso];tapis xxl [perso];chiffonnette [perso];chiffon lunettes [perso];chiffon [perso];microfibre [perso];tote bag [perso];sac [perso];sac toile [perso];cabas [perso];magnet [perso];aimant [perso];aimant frigo [perso];porte clé [perso];porte-clé [perso];porte clef [perso];t shirt [perso];tee shirt [perso];tshirt [perso]`

🔴 **NOM NU** : `mug mira` — PAS `mug mira kpop demon hunters`.

### 🔗 H1 + Handle
H1 = `[Type] [Perso]` sans franchise. Si nom nu dominant → raccourcir H1 ET handle + 301. Ex : `mug shadow the hedgehog` → « Mug Shadow » + `mug-shadow`. **Jamais changer handle sans `urlRedirectCreate`.**

---

## Contraintes permanentes
- Redirections bijoux → "/" : intentionnelles. Collections vides DRAFT : normales. Faux avis JSON-LD : ne pas corriger.
- Tote Bags DRAFT : inclure dans le cluster. Métachamps thème : remplis, ne plus vérifier.
- Alt texts : `fileUpdate` (PAS `productUpdateMedia` — dépréciée). Format : `[Produit] [Perso] [Franchise] illustré à la main en Anjou`.

---

## 🔄 P3 dernier par type — mettre à jour fin de session
MUG:#9 | TAB:#2 | PK:#5 | CHIFF:#2 | TAPIS:#3 | TOTE:#8 | MAGNET:#6 | TSHIRT:#3

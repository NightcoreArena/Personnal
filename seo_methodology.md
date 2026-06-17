# Méthodologie SEO — Les Bois d'Aurore
*Document de référence interne — à consulter avant chaque rédaction*

---

## 1. Contexte du store

**Les Bois d'Aurore** (lesboisdaurores.fr) vend des produits dérivés manga artisanaux :
- Illustrations 100% faites à la main (sans IA), par un artisan basé en Anjou
- Produits : Mug, Tableau/Poster/Affiche/Cadre, Tapis de Souris, Chiffonnette, Tote Bag, Magnet, Porte Clé
- Personnages : Pokémon, Demon Slayer, Kpop Demon Hunter, et d'autres franchises manga/anime
- Domain Authority très faible (DA ~8/100) → la qualité du contenu et l'intention de recherche précise sont les leviers principaux

**Différenciation store vs concurrence :**
- Dessin artisanal, sans IA
- Fabrication locale (Made in Anjou)
- Ce n'est PAS du merchandising officiel → toujours "inspiré de" ou "dans l'univers de", JAMAIS "officiel" ou "tiré de"

---

## 2. La structure canonique d'une description produit

```html
<p>[Intro : 1 à 2 phrases max — angle spécifique au type de produit]</p>
<ul>
  <li>[Spec 1]</li>
  <li>[Spec 2]</li>
  ...
</ul>
<p>[CTA : 1 phrase — action + bénéfice concret]</p>
```

### Modèle de référence : Mug Pikachu
```html
<p>Ajoutez une touche de dynamisme à votre quotidien avec ce mug Pikachu, l'accessoire indispensable pour tous les dresseurs en quête d'énergie dès le matin.</p>
<ul>
  <li>Format : 340ml (idéal thé/café)</li>
  <li>Matière : Céramique blanche premium</li>
  <li>Entretien : Compatible micro-ondes et lave-vaisselle</li>
  <li>Impression : Sublimation inaltérable</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
<p>Commandez dès maintenant votre mug Pikachu collector et savourez vos boissons préférées en compagnie du plus célèbre des Pokémon.</p>
```

**Ce que ce modèle fait bien :**
- "tous les dresseurs" = parle directement au public cible (pas "tous les fans de Pokémon")
- "en quête d'énergie dès le matin" = situation concrète d'usage
- Aucune description du lore, aucune biographie du personnage
- L'utilisateur sait déjà qui est Pikachu — on lui vend le PRODUIT, pas le personnage

**Ce que ce modèle ne fait PAS :**
- Pas de H1/H2 dans le corps de description (c'est géré par le titre produit Shopify)
- Pas de tiret long (—)
- Pas de "Ce produit X est dédié aux fans de..."
- Pas de répétition de la même intro dans tous les produits du même personnage

---

## 3. Règles de rédaction

### Ton et vocabulaire
- **Vouvoiement obligatoire** : "votre", "vous", jamais "ta", "tu"
- **Français simple et courant** : éviter les termes trop formels, trop littéraires, ou trop techniques
  - Mauvais : "tatooes", "pugilistiques", "l'essence martiale"
  - Bon : "partout avec vous", "votre bureau", "vos affaires"
- **Pas de tiret long (—)** dans le texte narratif — ça fait IA. Les deux points (:) ou la virgule font le travail
- **Pas d'italique ou gras** dans les paragraphes narratifs (uniquement dans les specs si vraiment utile)
- **Phrases courtes** : une idée par phrase maximum
- **Pas de clichés IA** : "emmenez-vous dans un voyage", "l'âme du personnage", "vibrez au rythme de", "affirmez votre puissance", "plongez au cœur de"

### Contenu du texte
- **Ne pas décrire l'illustration** : on ne voit pas l'image en rédigeant → risque d'hallucination. L'image parle d'elle-même sur la page produit
- **Ne pas inventer de lore** : si on ne connaît pas le personnage avec certitude, ne pas s'aventurer dans sa biographie. Utiliser uniquement ce qui est public et connu (ex : Akaza = Upper Moon 3 de Demon Slayer, ça tout le monde le sait)
- **"inspiré de l'univers de"** et jamais **"tiré de l'univers de"** → le premier dit que c'est une création libre, le second suggère une reproduction officielle
- **L'acheteur connaît déjà le personnage** : inutile de lui expliquer qui est Akaza, qui est Pikachu. Il cherche un PRODUIT avec ce personnage, pas une fiche Wikipédia

---

## 4. La règle anti-duplicate content par cluster de personnage

### Le problème
Si 7 pages produit (Mug, Tableau, Tapis, Chiffonnette, Tote Bag, Magnet, Porte Clé) d'un même personnage disent toutes "Akaza, ancien humain du nom de Hakuji, est devenu la Lune Croissante Supérieure de rang 3..." → Google ne sait pas quelle page est l'autorité sur Akaza. Les pages se cannibalisent mutuellement.

### La solution : un angle différent par type de produit

Chaque produit d'un même personnage doit ouvrir depuis un contexte d'usage différent :

| Produit | Angle d'ouverture | Contexte d'usage |
|---|---|---|
| Mug | Rituel du matin, énergie | "dès le matin", "chaque journée" |
| Tableau | Décoration murale, identité d'espace | "votre mur", "votre chambre/bureau" |
| Tapis de souris | Setup bureau/gaming, présence quotidienne | "votre bureau", "à chaque session" |
| Chiffonnette | Utilité pratique, cadeau original | "vos lunettes", "votre écran", "idée cadeau" |
| Tote Bag | Afficher son univers au quotidien, style | "partout où vous allez", "transporter" |
| Magnet | Collectionner, personnaliser un espace | "votre frigo", "votre tableau", "collecter" |
| Porte Clé | Toujours avec soi, everyday carry | "partout avec vous", "dans votre poche" |

**Ce qui reste commun (et c'est normal) :**
- Le bloc de specs : Google comprend que c'est du contenu structuré standardisé, comme les fiches techniques
- La mention "Made in Anjou" et "sans IA" dans les specs

**Ce qui DOIT être différent :**
- Le paragraphe d'ouverture (angle, situation concrète)
- Le CTA final (verbe d'action + bénéfice spécifique au produit)
- La méta description (valeur proposition différente)

---

## 5. Carte des mots-clés : Collections vs Pages Produit

### Règle fondamentale
- **Collection page** = cible le keyword générique `[produit] demon slayer` ou `[produit] manga`
- **Page produit** = cible le keyword spécifique `[produit] [personnage]` ou `[personnage] demon slayer`

Ne jamais mettre un keyword de collection comme cible principale d'une page produit → cannibalisation.

### Mots-clés owned par les pages COLLECTION (NE PAS utiliser dans les méta titres produit)

| Keyword | Volume | Collection |
|---|---|---|
| porte clé demon slayer | 210/mois | Collection Porte Clé Demon Slayer |
| tapis de souris demon slayer | 140/mois | Collection Tapis de Souris Demon Slayer |
| tableau demon slayer | 110/mois | Collection Tableau Demon Slayer |
| mug demon slayer | ~200/mois | Collection Mug Demon Slayer |
| magnet demon slayer | 20/mois | Collection Magnet Demon Slayer |
| tote bag demon slayer | 20/mois | Collection Tote Bag Demon Slayer |
| chiffonnette demon slayer | 0/mois | Collection Chiffonnette Demon Slayer |
| [produit] manga | variable | Collections Manga par produit |

### Mots-clés pour les pages PRODUIT

La réalité Semrush : les combos `[produit] [personnage]` (ex : "tapis de souris akaza", "magnet akaza") ont en général **0 à 10 recherches/mois en France**.

Le seul keyword à volume pour Akaza : **"akaza demon slayer" (2 900/mois)** et **"demon slayer akaza" (1 000/mois)**.

**Conséquence stratégique :**
- Les pages produit Akaza ne visent pas à ranker sur leur propre combinaison produit+personnage
- Elles servent à renforcer l'autorité topique sur "akaza demon slayer" via un cluster
- Leur objectif principal est la **conversion** pour les visiteurs qui arrivent depuis des recherches liées à Akaza
- L'exact phrase "akaza demon slayer" doit apparaître dans le corps du texte de chaque fiche produit Akaza

---

## 6. Règles pour les méta titres

### Format
`[Keyword principal] [emoji optionnel] [Qualifiant] | [Keyword secondaire]`

Exemples :
- `Mug Akaza 👹 Lune Supérieure 3 | Cadeau Kimetsu no Yaiba`
- `Poster Akaza 👹 Demon Slayer | Kimetsu no Yaiba`

### Règles
1. **Jamais "| Les Bois d'Aurore"** → Google le tronque, perte de mots-clés
2. **Choisir le mot-clé avec le plus de volume** même si le H1 Shopify utilise un autre terme
   - Ex : "poster akaza" (30/mois) > "tableau akaza" (0/mois) → méta titre = "Poster Akaza" mais H1 reste "Tableau Akaza"
3. **Longueur** : max 60 caractères (espaces compris)
4. **L'exact match du keyword principal** doit apparaître en début de méta titre
5. **Un emoji** peut être utilisé pour le CTR mais ne pas en abuser (1 par titre max)

### Tableau de référence : méta titres Akaza

| Produit | H1 (titre Shopify) | Méta titre (keyword prioritaire) |
|---|---|---|
| Mug | Mug Akaza | `Mug Akaza 👹 Lune Supérieure 3 \| Cadeau Kimetsu no Yaiba` |
| Tableau | Tableau Akaza | `Poster Akaza 👹 Demon Slayer \| Kimetsu no Yaiba` |
| Tapis de Souris | Tapis de Souris Akaza | `Tapis de Souris Akaza 🖱️ Demon Slayer \| Kimetsu no Yaiba` |
| Chiffonnette | Chiffonnette Akaza | `Chiffonnette Akaza 👹 Demon Slayer \| Cadeau Original` |
| Tote Bag | Tote Bag Akaza | `Tote Bag Akaza 👹 Demon Slayer \| Kimetsu no Yaiba` |
| Magnet | Magnet Akaza | `Magnet Akaza 👹 Demon Slayer \| Kimetsu no Yaiba` |
| Porte Clé | Porte Clé Akaza | `Porte Clé Akaza 👹 Demon Slayer \| Kimetsu no Yaiba` |

---

## 7. Règles pour les méta descriptions

- **Max 155 caractères**
- Chaque méta description doit mettre en avant un élément différent (conversion)
- Inclure : le nom produit + personnage + franchise + au moins 1 spec unique + 1 argument (artisanal/Anjou)
- Ne pas réutiliser la même structure de phrase

### Exemples de différenciation pour Akaza

| Produit | Angle de la méta description |
|---|---|
| Mug | Usage matin + volume 340ml |
| Tableau | Formats disponibles (affiche, toile, cadre) |
| Tapis de Souris | Dimensions + antidérapant |
| Chiffonnette | Usage pratique (lunettes/écran) + lavable |
| Tote Bag | Tissu satin 280g + couleurs durables |
| Magnet | Coque métal + Mylar glossy |
| Porte Clé | Métal robuste + compact quotidien |

---

## 8. Workflow de recherche Semrush avant rédaction

### Étape 1 : rechercher les volumes par personnage

```
phrase_fullsearch → "[personnage] demon slayer" + database: fr
```

Identifier : volume principal, variantes, intention de recherche associée.

### Étape 2 : rechercher les variantes par type de produit

```
phrase_fullsearch → "[produit] [personnage]" + database: fr
```

Si tous à 0 : confirme qu'on vise le cluster du personnage, pas le combo produit+personnage.

```
phrase_fullsearch → "[produit] [franchise]" + database: fr
```

Si > 0 : ce keyword appartient à la collection, PAS à la page produit.

### Étape 3 : chercher des variantes de produit

```
phrase_fullsearch → "poster [personnage]" vs "tableau [personnage]" vs "affiche [personnage]"
```

Identifier quelle variante a le plus de volume → c'est celle qui va dans le méta titre.

### Règle Semrush importante
La base `fr` retourne souvent 0 pour les combos nichés. Ce n'est pas un échec : ça confirme que le volume est sur le keyword de la franchise ("akaza demon slayer") et que le rôle des pages produit est de convertir + renforcer le cluster.

---

## 9. Workflow de sauvegarde avant toute modification

**Avant de modifier un groupe de produits :**

1. Créer un fichier JSON `[personnage]_backup.json` dans `/home/user/Personnal/`
2. Y sauvegarder : id, title, seo_title, seo_description, descriptionHtml
3. Commit + push sur le branch actif
4. SEULEMENT ENSUITE modifier les produits

**En cas d'erreur :**
- Les champs SEO (seo_title, seo_description) sont exacts dans le backup → restauration parfaite
- Le descriptionHtml peut être restauré depuis le backup

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

## 11. Auto-critique : erreurs commises et à ne plus répéter

### Erreur 1 : Répétition du lore du personnage dans chaque produit
**Ce qui s'est passé :** Chaque description Akaza mentionnait "Lune Croissante Supérieure de rang 3", "ancien humain du nom de Hakuji". 7 pages avec le même paragraphe.
**Pourquoi c'est mauvais :** Duplicate content sur le contenu narratif. Google ne sait pas quelle page prioriser.
**La règle :** Chaque produit aborde le personnage depuis l'angle de son USAGE, pas depuis sa biographie.

### Erreur 2 : CTAs structurellement identiques
**Ce qui s'est passé :** Tous les CTAs suivaient "Commandez dès maintenant votre [X] Akaza et [bénéfice générique]".
**Pourquoi c'est mauvais :** Formulaique, signature IA, nul pour la différenciation.
**La règle :** Le CTA doit contenir le verbe d'action adapté au produit :
- Tableau → "Choisissez votre format"
- Tapis → "Équipez votre bureau"
- Chiffonnette → "Offrez ou gardez pour vous"
- Tote Bag → "Portez votre passion"
- Magnet → "Ajoutez à votre collection"
- Porte Clé → "Prenez-le partout avec vous"

### Erreur 3 : "akaza demon slayer" (2 900/mois) absent du texte
**Ce qui s'est passé :** Le mot-clé principal n'apparaissait jamais comme phrase exacte dans le corps du texte.
**La règle :** "akaza demon slayer" ou "demon slayer akaza" doit apparaître en phrase exacte dans le paragraphe d'ouverture de CHAQUE fiche produit Akaza.

### Erreur 4 : Ne pas avoir vérifié toutes les collections
**Ce qui s'est passé :** Annoncé qu'il n'y avait pas de collection pour tapis de souris, magnet, chiffonnette. C'était faux — elles existaient en page 3 et 4 du listing.
**La règle :** Toujours paginer jusqu'au bout avant de conclure qu'une collection n'existe pas.

### Erreur 5 : Modifier des produits sans sauvegarde préalable
**Ce qui s'est passé :** 10 produits écrasés sans backup. Impossible de restaurer exactement les descriptions originales.
**La règle :** JSON backup AVANT toute mutation Shopify. Sans exception.

### Erreur 6 : Inventer du lore sur des personnages inconnus
**Ce qui s'est passé :** Pour Kpop Demon Hunter (personnages Rumi, Mira, Zoey, Huntrix), des éléments biographiques inventés ont été écrits.
**La règle :** Si on ne connaît pas le personnage avec certitude → recherche web AVANT de rédiger. Ou demander à l'utilisateur. Jamais inventer.

### Erreur 7 : H1/H2 dans le corps de description
**Ce qui s'est passé :** Le Tote Bag Akaza original avait des balises `<h1>` et `<h2>` dans le descriptionHtml.
**Pourquoi c'est mauvais :** Le H1 est le titre produit Shopify. Mettre un second H1 dans la description crée une confusion structurelle pour Google.
**La règle :** Uniquement `<p>` et `<ul><li>` dans le corps de description. Jamais de balises H.

### Erreur 8 : "tirée de l'univers Demon Slayer" 
**Ce qui s'est passé :** Cette formulation suggère une reproduction officielle.
**La règle :** Toujours "inspirée de" ou "dans l'univers de" (produit non officiel, création artisanale).

### Erreur 9 : "| Les Bois d'Aurore" dans les méta titres
**Ce qui s'est passé :** Google tronque les titres longs et supprime le nom de la boutique.
**La règle :** Pas de "| Les Bois d'Aurore" dans les méta titres. L'espace est précieux, utiliser "| Kimetsu no Yaiba" ou un autre keyword à valeur.

### Erreur 10 : Méta descriptions avec le même template
**Ce qui s'est passé :** "[Produit] Akaza en [matière] [dimension], illustration artisanale sans IA. [Produit] collector pour fans de Kimetsu no Yaiba, fabriqué en Anjou." — structure identique pour tous.
**La règle :** Chaque méta description doit être construite autour d'une valeur différente.

---

## 12. Descriptions Akaza — Version finale de référence

Mug Akaza : déjà appliqué (voir produit gid://shopify/Product/10146826289482)

### Tableau Akaza (gid://shopify/Product/10183455605066)

**Description :**
```html
<p>Donnez à votre mur le caractère d'Akaza Demon Slayer avec cette illustration faite à la main en Anjou. Format affiche, toile sur châssis ou cadre avec vitre : choisissez l'option qui correspond à votre déco.</p>
<ul>
  <li>Affiche : Impression HD sur papier photo premium 200g (du 10x15 au 50x70cm)</li>
  <li>Tableau : Toile tendue sur châssis bois FSC (21x29cm)</li>
  <li>Cadre : Finition noir ou blanc, avec vitre verre ou plexiglas léger</li>
  <li>Exclusivité : Dessin 100% artisanal, encres anti-UV, sans IA (Made in Anjou)</li>
</ul>
<p>Choisissez votre format et recevez votre tableau Akaza sous quelques jours.</p>
```
**Méta titre :** `Poster Akaza 👹 Demon Slayer | Kimetsu no Yaiba`
**Méta description :** `Tableau Akaza Demon Slayer disponible en affiche, toile ou cadre. Illustration 100% artisanale, encres anti-UV, fabriqué en Anjou.`

---

### Tapis de Souris Akaza (gid://shopify/Product/15372512592202)

**Description :**
```html
<p>Sur votre bureau, Akaza Demon Slayer vous accompagne à chaque session avec ce tapis de souris artisanal. Surface de glisse optimale et dessin exclusif fait à la main en Anjou.</p>
<ul>
  <li>Dimensions : 22x18 cm (épaisseur 2mm)</li>
  <li>Matière : Surface polyester pour glisse optimale</li>
  <li>Maintien : Base en caoutchouc antidérapant</li>
  <li>Impression : Sublimation inaltérable</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
<p>Équipez votre bureau avec ce tapis Akaza et affichez votre passion pour Demon Slayer au quotidien.</p>
```
**Méta titre :** `Tapis de Souris Akaza 🖱️ Demon Slayer | Kimetsu no Yaiba`
**Méta description :** `Tapis de souris Akaza Demon Slayer 22x18cm, base antidérapante, surface polyester glisse optimale. Illustration artisanale sans IA, fabriqué en Anjou.`

---

### Chiffonnette Akaza (gid://shopify/Product/15361801716042)

**Description :**
```html
<p>Pour nettoyer vos lunettes ou votre écran tout en affichant votre passion pour Akaza Demon Slayer, cette chiffonnette microfibre artisanale coche toutes les cases. Simple, pratique, illustrée à la main en Anjou.</p>
<ul>
  <li>Dimensions : 18x15 cm</li>
  <li>Matière : Microfibre ultra-douce</li>
  <li>Usage : Nettoie lunettes et écrans sans rayer</li>
  <li>Entretien : Lavable en machine</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
<p>Offrez ou gardez pour vous cette chiffonnette Akaza : une idée cadeau utile pour les fans de Demon Slayer.</p>
```
**Méta titre :** `Chiffonnette Akaza 👹 Demon Slayer | Cadeau Original`
**Méta description :** `Chiffonnette Akaza Demon Slayer en microfibre 18x15cm. Nettoie lunettes et écrans sans rayer, lavable en machine. Dessin artisanal sans IA, fabriqué en Anjou.`

---

### Tote Bag Akaza (gid://shopify/Product/15380205240650)

**Description :**
```html
<p>Ce tote bag Akaza Demon Slayer en satin épais est fait pour transporter vos affaires sans cacher votre passion. Imprimé par sublimation, les couleurs restent vives lavage après lavage.</p>
<ul>
  <li>Surface : Tissu satiné épais (280g)</li>
  <li>Dimensions : 36x33cm</li>
  <li>Impression : Sublimation brillante inaltérable</li>
  <li>Entretien : Lavage à 30° max</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
<p>Commandez votre tote bag Akaza et portez votre univers manga partout avec vous.</p>
```
**Méta titre :** `Tote Bag Akaza 👹 Demon Slayer | Kimetsu no Yaiba`
**Méta description :** `Tote bag Akaza Demon Slayer satin épais 280g, 36x33cm. Impression sublimation brillante inaltérable. Dessin artisanal sans IA, fabriqué en Anjou.`

---

### Magnet Akaza (gid://shopify/Product/15380962804042)

**Description :**
```html
<p>Ce magnet Akaza Demon Slayer en coque métal rigide est fait pour les collectionneurs qui veulent personnaliser leur espace avec leurs personnages favoris. Compact, solide, illustré à la main en Anjou.</p>
<ul>
  <li>Dimensions : Diamètre 5 cm</li>
  <li>Matière : Coque métal rigide</li>
  <li>Finition : Mylar glossy ultra-brillant et protecteur</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
<p>Ajoutez ce magnet Akaza à votre collection et personnalisez votre frigo ou tableau avec Demon Slayer.</p>
```
**Méta titre :** `Magnet Akaza 👹 Demon Slayer | Kimetsu no Yaiba`
**Méta description :** `Magnet Akaza Demon Slayer coque métal rigide 5cm, finition Mylar glossy. Illustration artisanale sans IA, fabriqué en Anjou. Idée cadeau collector.`

---

### Porte Clé Akaza (gid://shopify/Product/10181095686474)

**Description :**
```html
<p>Ce porte-clé Akaza Demon Slayer en métal robuste part avec vous partout, fabriqué à la main en Anjou. Un accessoire collector pour les fans qui gardent leur passion près d'eux au quotidien.</p>
<ul>
  <li>Dimensions : Médaillon 3x4 cm</li>
  <li>Matière : Métal robuste, anneau solide de 3cm</li>
  <li>Impression : Sublimation haute définition</li>
  <li>Exclusivité : Dessin 100% artisanal, sans IA (Made in Anjou)</li>
</ul>
<p>Prenez ce porte-clé Akaza avec vous et emportez un peu de Kimetsu no Yaiba dans votre quotidien.</p>
```
**Méta titre :** `Porte Clé Akaza 👹 Demon Slayer | Kimetsu no Yaiba`
**Méta description :** `Porte-clé Akaza Demon Slayer en métal robuste, médaillon 3x4cm. Illustration artisanale sans IA, fabriqué en Anjou. Idée cadeau pour fans de Demon Slayer.`

---

## 13. Checklist avant de publier un cluster de descriptions

- [ ] Chaque description a un angle d'ouverture unique (pas de copie entre produits)
- [ ] "akaza demon slayer" (ou "[perso] [franchise]") apparaît en phrase exacte dans chaque intro
- [ ] Aucun lore répété à l'identique entre les descriptions du cluster
- [ ] Tous les CTAs utilisent des verbes différents
- [ ] Aucune balise H dans le descriptionHtml
- [ ] Aucun tiret long (—) dans le texte narratif
- [ ] Vouvoiement respecté
- [ ] Méta titres sans "| Les Bois d'Aurore"
- [ ] Méta titres : keyword le plus cherché en premier (vérifié sur Semrush)
- [ ] Méta descriptions < 155 caractères
- [ ] Méta descriptions avec angles différents entre elles
- [ ] Backup JSON créé et commité avant toute modification
- [ ] Aucune description de l'illustration (risque d'hallucination)
- [ ] "inspiré de" et non "tiré de" pour les oeuvres non officielles

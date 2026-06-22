#!/usr/bin/env python3
"""
seo_lint.py — Vérification mécanique d'un cluster *_seo_new.json AVANT application Shopify.

Usage :
    python3 seo_lint.py <cluster>_seo_new.json

Objectif : transformer la checklist "à cocher mentalement" de CLAUDE.md en
contrôles automatiques impossibles à oublier. Un FAIL bloque l'application.

Le script lit le JSON, vérifie chaque règle vérifiable mécaniquement, et imprime
PASS / WARN / FAIL. Code de sortie 1 s'il reste au moins un FAIL.

Il ne remplace PAS le jugement éditorial (qualité du lore, ton, persona) : il
attrape les fautes structurelles répétitives (placement des liens, longueurs,
tokens interdits, doublons intra-cluster).
"""

import sys
import os
import re
import json
import unicodedata

# ---------- helpers ----------

PRODUCT_EMOJIS = {"☕", "🖼", "🔑", "👕", "🧼", "🖱", "👜", "🧲"}
# emoji attendu par type de produit (anti 🧻/🧼 et autres confusions visuelles).
# Ordre = priorité de match ; on dérive le type du title/handle.
EMOJI_BY_TYPE = [
    (("mug", "tasse"), "☕"),
    (("tableau", "poster", "affiche", "cadre", "toile"), "🖼"),
    (("porte",), "🔑"),
    (("t-shirt", "tshirt", "tee"), "👕"),
    (("chiffonnette",), "🧼"),
    (("tapis",), "🖱"),
    (("tote", "cabas", "sac"), "👜"),
    (("magnet", "aimant"), "🧲"),
]
# mots qui DOIVENT porter un accent dans un méta titre (anti "Porte Cle").
ACCENT_TRAPS = {"cle": "clé"}
# produit -> fragment du titre de section §10 (seo_methodology.md) à matcher.
# Permet de comparer les specs d'une fiche au bloc canonique de son type.
SPEC_TYPE_NEEDLES = [
    (("mug", "tasse"), "mug"),
    (("tableau", "poster", "affiche", "cadre", "toile"), "tableau"),
    (("tapis",), "tapis"),
    (("chiffonnette",), "chiffonnette"),
    (("tote", "cabas", "sac"), "tote"),
    (("magnet", "aimant"), "magnet"),
    (("porte",), "porte"),
]
ANGLICISMES_TITRE = ["mousepad", "keychain", "breloque"]
META_DESC_INTERDITS = ["sans ia", "anjou", "made in"]
BROAD_INTENT_TOKENS = ["cadeau", "goodies", "déco", "decoration", "décoration",
                       "manga", "anime", "idée cadeau", "collection",
                       "gaming", "jeu vidéo", "jeu video", "gamer"]

results = []  # (level, scope, msg)


def add(level, scope, msg):
    results.append((level, scope, msg))


def strip_tags(html):
    return re.sub(r"<[^>]+>", "", html)


def paragraphs(html):
    return re.findall(r"<p>(.*?)</p>", html, flags=re.S)


def first_words(text, n):
    words = strip_tags(text).split()
    return " ".join(words[:n]).lower()


def get_handle(p):
    # tolérance aux variantes de schéma entre clusters (handle / new_handle / handle_new)
    for k in ("handle", "new_handle", "handle_new", "current_handle"):
        if p.get(k):
            return p[k]
    return None


def get_scope(p):
    return p.get("type") or p.get("title") or get_handle(p) or "?"


def get_keyword(data):
    """Mot-clé perso pour le contrôle de densité (anti-stuffing).
    Priorité au champ explicite, sinon dérivé du nom de cluster (avant la parenthèse)."""
    kw = data.get("keyword") or data.get("perso_keyword")
    if kw:
        return kw.strip().lower()
    cluster = data.get("cluster", "")
    cluster = re.sub(r"\(.*?\)", "", cluster)  # retire "(High School DxD)" etc.
    cluster = re.sub(r"[:\-–].*$", "", cluster)  # retire un sous-titre éventuel
    return cluster.strip().lower()


def norm_spec(s):
    """Normalise une ligne de spec pour comparaison : sans balise, sans espace, minuscule.
    'Contenance : 340 ml' et 'contenance:340ml' deviennent identiques ; '330' != '340'."""
    return re.sub(r"\s+", "", strip_tags(s)).lower()


def load_spec_reference():
    """Charge les blocs de specs canoniques depuis seo_specs.md (fichier dédié).
    Source de vérité UNIQUE : empêche toute divergence de spec (ex : 330 vs 340 ml).
    Retourne {titre_section_lower: set(specs normalisées)} ou None si introuvable."""
    here = os.path.dirname(os.path.abspath(__file__))
    md = None
    for path in (os.path.join(here, "seo_specs.md"),
                 os.path.join(os.getcwd(), "seo_specs.md")):
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                md = f.read()
            break
    if md is None:
        return None
    blocks = {}
    for hm in re.finditer(r"###\s*(.+?)\n```html\s*(.*?)```", md, flags=re.S):
        heading = hm.group(1).strip().lower()
        lis = re.findall(r"<li>(.*?)</li>", hm.group(2), flags=re.S)
        blocks[heading] = {norm_spec(x) for x in lis}
    return blocks or None


def canonical_specs_for(ptype, spec_ref):
    """Retourne le set de specs canoniques pour le type de produit, ou None."""
    if not spec_ref:
        return None
    key = next((h for needles, h in SPEC_TYPE_NEEDLES if any(nd in ptype for nd in needles)), None)
    if not key:
        return None
    return next((specs for heading, specs in spec_ref.items() if key in heading), None)


def emoji_in(title):
    found = set()
    for ch in title:
        # on ignore les variation selectors / ZWJ
        if ord(ch) >= 0x2600 and unicodedata.category(ch) in ("So", "Sk"):
            base = ch
            if base in ("️",):
                continue
            found.add(ch)
    # normaliser 🖼️ -> 🖼 etc. (déjà géré : variation selector ignoré)
    return found


# ---------- checks ----------

def lint(data):
    products = data.get("products", [])
    franchise = data.get("franchise", "").strip().lower()
    keyword = get_keyword(data)
    n = len(products)
    if n == 0:
        add("FAIL", "global", "aucun produit dans le JSON")
        return

    p1_openers = {}
    cta_verbs = {}
    emojis = {}
    p3_banks = {}
    link_in_cta = 0
    link_connectors = {}
    title_has_full = []  # (scope, bool) : H1 contient-il le nom complet du perso ?
    handles = {get_handle(p) for p in products if get_handle(p)}
    spec_ref = load_spec_reference()
    if spec_ref is None:
        add("WARN", "global", "seo_specs.md introuvable : specs non vérifiées")

    for p in products:
        scope = get_scope(p)
        # noms de champs JSON : un champ absent = erreur silencieuse coûteuse
        # (le JSON semblait OK mais le lint comptait 0 mot). Message explicite.
        for field in ("descriptionHtml", "seo_title", "seo_description"):
            if field not in p:
                add("FAIL", scope,
                    f"champ '{field}' absent — noms attendus : "
                    f"descriptionHtml / seo_title / seo_description / p3_bank")
        html = p.get("descriptionHtml", "")
        title = p.get("seo_title", "")
        desc = p.get("seo_description", "")
        ps = paragraphs(html)

        # --- méta titre ---
        if len(title) > 60:
            add("FAIL", scope, f"méta titre {len(title)} car (>60) : {title!r}")
        else:
            add("PASS", scope, f"méta titre {len(title)} car")
        if "| les bois" in title.lower():
            add("FAIL", scope, "méta titre contient '| Les Bois d'Aurore' (interdit)")
        for a in ANGLICISMES_TITRE:
            if re.search(rf"\b{a}\b", title.lower()):
                add("FAIL", scope, f"anglicisme interdit dans méta titre : '{a}'")
        if re.search(r"\btee\b", title.lower()):
            add("FAIL", scope, "anglicisme 'tee' seul dans méta titre")
        em = emoji_in(title)
        if not em:
            add("WARN", scope, "aucun emoji dans le méta titre")
        else:
            emojis[scope] = frozenset(em)
        # emoji cohérent avec le type de produit (dérivé du title/handle)
        ptype = (p.get("type") or p.get("title") or get_handle(p) or "").lower()
        expected_emoji = next(
            (emo for needles, emo in EMOJI_BY_TYPE if any(nd in ptype for nd in needles)),
            None)
        if expected_emoji and em and expected_emoji not in em:
            add("FAIL", scope,
                f"emoji {sorted(em)} ne correspond pas au type '{ptype}' "
                f"(attendu : {expected_emoji})")
        # accent manquant (ex : 'Porte Cle' au lieu de 'Porte Clé')
        for bad, good in ACCENT_TRAPS.items():
            if re.search(rf"\b{bad}\b", title.lower()):
                add("FAIL", scope,
                    f"accent manquant dans le méta titre : '{bad}' → '{good}'")

        # --- specs conformes au bloc canonique §10 (anti 330/340 ml) ---
        canon = canonical_specs_for(ptype, spec_ref)
        if canon:
            for li in re.findall(r"<li>(.*?)</li>", html, flags=re.S):
                if norm_spec(li) not in canon:
                    add("FAIL", scope,
                        f"spec hors référence §10 : « {strip_tags(li).strip()} » "
                        f"— copier le bloc §10 verbatim")

        # --- méta description ---
        if len(desc) > 155:
            add("FAIL", scope, f"méta desc {len(desc)} car (>155)")
        else:
            add("PASS", scope, f"méta desc {len(desc)} car")
        for t in META_DESC_INTERDITS:
            if t in desc.lower():
                add("FAIL", scope, f"méta desc contient un terme interdit : '{t}'")
        if re.search(r"\d+\s?(ml|cm|g\b)", desc.lower()):
            add("WARN", scope, "méta desc semble contenir une spec brute (chiffre+unité)")
        if franchise and desc.lower().count(franchise) > 1:
            add("FAIL", scope, f"franchise '{franchise}' répétée {desc.lower().count(franchise)}× en méta desc")

        # --- HTML / tirets / balises ---
        if "—" in html or "–" in html:
            add("FAIL", scope, "tiret long (—/–) présent dans la description")
        if re.search(r"<h[1-6]", html, flags=re.I):
            add("FAIL", scope, "balise Hn présente (interdit)")

        # --- mots de prose (tous les <p>) ---
        prose = " ".join(strip_tags(x) for x in ps)
        wc = len(prose.split())
        if wc < 125 or wc > 175:
            add("FAIL", scope, f"{wc} mots de prose (hors 125-175)")
        elif wc < 130 or wc > 160:
            add("WARN", scope, f"{wc} mots de prose (hors cible 130-160)")
        else:
            add("PASS", scope, f"{wc} mots de prose")

        # --- densité du mot-clé exact (anti-stuffing) ---
        if keyword:
            kw_re = re.compile(r"\b" + re.escape(keyword) + r"\b")
            total_kw = len(kw_re.findall(prose.lower()))
            p1_kw = len(kw_re.findall(strip_tags(ps[0]).lower())) if ps else 0
            # ≥3 en P1 = stuffing (sujet + répétition produit + ancre). Le minimum
            # naturel pour un perso à 1 mot est 2 (sujet + ancre du lien en P1) : toléré.
            if p1_kw >= 3:
                add("FAIL", scope, f"mot-clé '{keyword}' {p1_kw}× dans le P1 (stuffing) : retirer la répétition produit, garder sujet + ancre")
            if total_kw >= 5:
                add("WARN", scope, f"mot-clé '{keyword}' {total_kw}× dans la fiche (densité élevée, varier en pronoms/épithètes)")

        # --- H1 : collecte pour contrôle de cohérence inter-fiches ---
        if keyword:
            h1 = (p.get("title") or "").lower()
            title_has_full.append((scope, keyword in h1))

        # --- P1 opener unique ---
        if ps:
            op = first_words(ps[0], 4)
            p1_openers.setdefault(op, []).append(scope)

        # --- CTA verbe (dernier <p>) ---
        if ps:
            cta = strip_tags(ps[-1]).strip()
            verb = cta.split()[0].lower().rstrip(",.:;") if cta.split() else ""
            cta_verbs.setdefault(verb, []).append(scope)

        # --- P3 artisan : un seul <p><strong> ; P1/P2/CTA sans <strong> ---
        strong_ps = [i for i, x in enumerate(ps) if "<strong>" in x]
        if len(strong_ps) != 1:
            add("WARN", scope, f"{len(strong_ps)} paragraphe(s) en <strong> (attendu : 1 = artisan)")

        # --- p3_bank unique ---
        if "p3_bank" in p:
            p3_banks.setdefault(p["p3_bank"], []).append(scope)

        # --- maillage : liens ---
        links = re.findall(r'<a href="([^"]+)">([^<]+)</a>', html)
        if len(links) == 0:
            add("WARN", scope, "aucun lien de maillage interne")
        elif len(links) > 1:
            add("WARN", scope, f"{len(links)} liens de maillage (attendu : 1)")
        for href, anchor in links:
            if not href.startswith("/products/"):
                add("FAIL", scope, f"lien non relatif ou hors /products/ : {href}")
            target = href.replace("/products/", "")
            if target == get_handle(p):
                add("FAIL", scope, "le lien pointe vers le produit lui-même")
            elif target not in handles:
                add("WARN", scope, f"lien hors cluster (vérifier qu'il n'est pas DRAFT) : {target}")
            if re.match(r"https?://", anchor) or "cliquez ici" in anchor.lower():
                add("FAIL", scope, f"ancre non descriptive : {anchor!r}")
            # placement : le lien est-il dans le dernier <p> (CTA) ?
            if ps and href in ps[-1]:
                # connecteur = 2 mots avant le <a>
                idx = ps[-1].find('<a href')
                before = strip_tags(ps[-1][:idx]).split()
                conn = " ".join(before[-2:]).lower()
                link_connectors.setdefault(conn, []).append(scope)
                # compté plus bas
        # un lien en CTA ?
        if ps and "<a href" in ps[-1]:
            link_in_cta += 1

    # ---------- contrôles inter-produits ----------

    for op, who in p1_openers.items():
        if len(who) > 1:
            add("FAIL", "cluster", f"ouverture P1 identique ({op!r}) sur : {', '.join(who)}")
    for v, who in cta_verbs.items():
        if len(who) > 1 and v:
            add("FAIL", "cluster", f"verbe de CTA '{v}' répété sur : {', '.join(who)}")
    for e, who in {}.items():
        pass
    # emojis dupliqués
    seen = {}
    for scope, e in emojis.items():
        key = tuple(sorted(e))
        seen.setdefault(key, []).append(scope)
    for key, who in seen.items():
        if len(who) > 1:
            add("FAIL", "cluster", f"emoji {' '.join(key)} dupliqué sur : {', '.join(who)}")
    # p3 dupliqués
    for b, who in p3_banks.items():
        if len(who) > 1:
            add("FAIL", "cluster", f"P3 banque #{b} réutilisée dans le cluster : {', '.join(who)}")
    # connecteurs de lien répétés
    for conn, who in link_connectors.items():
        if len(who) >= 3 and conn.strip():
            add("FAIL", "cluster", f"connecteur de lien '{conn}' répété {len(who)}× (CTA formulaïque) : {', '.join(who)}")
    # trop de liens en CTA
    if link_in_cta > (n + 1) // 2:
        add("FAIL", "cluster",
            f"{link_in_cta}/{n} liens en CTA : varier le placement (P1 / transition / CTA)")
    else:
        add("PASS", "cluster", f"placement des liens varié ({link_in_cta}/{n} en CTA)")

    # cohérence des H1 (tous nom complet OU tous nom court, pas un mélange)
    if keyword and title_has_full:
        vals = {v for _, v in title_has_full}
        if len(vals) > 1:
            withk = [s for s, v in title_has_full if v]
            without = [s for s, v in title_has_full if not v]
            add("WARN", "cluster",
                f"H1 incohérent : nom complet '{keyword}' présent sur [{', '.join(withk)}] "
                f"mais absent sur [{', '.join(without)}] — uniformiser")

    # broad intent par fiche
    for p in products:
        scope = get_scope(p)
        txt = strip_tags(p.get("descriptionHtml", "")).lower()
        if not any(t in txt for t in BROAD_INTENT_TOKENS):
            add("WARN", scope, "aucune intention large détectée (cadeau/goodies/déco/manga...)")


# ---------- main ----------

def main():
    if len(sys.argv) != 2:
        print("usage: python3 seo_lint.py <cluster>_seo_new.json")
        sys.exit(2)
    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)

    lint(data)

    fails = [r for r in results if r[0] == "FAIL"]
    warns = [r for r in results if r[0] == "WARN"]

    order = {"FAIL": 0, "WARN": 1, "PASS": 2}
    for level, scope, msg in sorted(results, key=lambda r: (order[r[0]], r[1])):
        if level == "PASS":
            continue
        print(f"[{level}] {scope}: {msg}")

    print("-" * 60)
    print(f"{len(fails)} FAIL, {len(warns)} WARN, "
          f"{sum(1 for r in results if r[0] == 'PASS')} PASS")
    if fails:
        print("=> NE PAS APPLIQUER : corriger les FAIL d'abord.")
        sys.exit(1)
    print("=> OK pour application Shopify (revoir les WARN au jugement).")
    sys.exit(0)


if __name__ == "__main__":
    main()

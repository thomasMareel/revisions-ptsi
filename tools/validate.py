#!/usr/bin/env python3
"""Validation de index.html — Révisions PTSI.

Vérifie, sans navigateur ni dépendance, les erreurs les plus fréquentes
quand on ajoute un chapitre :

  1. Cohérence CHAPTERS <-> DOM (chaque chapitre déclaré a son <div>, et
     inversement).
  2. IDs HTML dupliqués (le type de bug "int-meth").
  3. Flashcards câblées : chaque chapitre listant le panneau 'flash' a bien
     un appel makeFlash(..., '<prefix>', ...).
  4. drawFn : chaque drawFn référencé dans CHAPTERS existe comme fonction.

Usage :
    python tools/validate.py            # valide index.html
    python tools/validate.py fichier.html

Code de sortie : 0 si tout est bon, 1 s'il y a au moins une erreur.
"""

import re
import sys
from pathlib import Path

# Sortie UTF-8 même sur une console Windows (évite UnicodeEncodeError sur les accents)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent


def load(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_chapters_region(html: str) -> str:
    """Isole le contenu du tableau const CHAPTERS = [ ... ];"""
    start = html.find("const CHAPTERS")
    if start == -1:
        return ""
    bracket = html.find("[", start)
    end = html.find("];", bracket)
    return html[bracket : end if end != -1 else len(html)]


def parse_chapters(region: str):
    """Retourne une liste de dicts {id, prefix, drawFn, panels} par chapitre."""
    chapters = []
    # Découpe la région avant chaque "id:'...'"
    chunks = re.split(r"(?=id:'[a-z0-9]+')", region)
    for chunk in chunks:
        m_id = re.match(r"id:'([a-z0-9]+)'", chunk)
        if not m_id:
            continue
        cid = m_id.group(1)
        m_prefix = re.search(r"prefix:'([a-z0-9]+)'", chunk)
        prefix = m_prefix.group(1) if m_prefix else None
        m_draw = re.search(r"drawFn:\s*'([A-Za-z0-9_]+)'", chunk)
        draw = m_draw.group(1) if m_draw else None
        m_panels = re.search(r"panels:\s*\[([^\]]*)\]", chunk)
        panels = []
        if m_panels:
            panels = re.findall(r"'([a-z]+)'", m_panels.group(1))
        chapters.append({"id": cid, "prefix": prefix, "drawFn": draw, "panels": panels})
    return chapters


def dom_chapter_ids(html: str):
    """IDs des <div class="chapter..."> (sans le préfixe chap-)."""
    ids = re.findall(r'<div class="chapter[^"]*"\s+id="chap-([a-z0-9]+)"', html)
    return ids


def all_html_ids(html: str):
    return re.findall(r'\sid="([^"]+)"', html)


def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "index.html"
    if not target.exists():
        print(f"[ERREUR] fichier introuvable : {target}")
        return 1

    html = load(target)
    errors = []
    warnings = []

    # --- Parsing ---
    region = extract_chapters_region(html)
    if not region:
        print("[ERREUR] tableau CHAPTERS introuvable.")
        return 1
    chapters = parse_chapters(region)
    chapter_ids = [c["id"] for c in chapters]
    dom_ids = dom_chapter_ids(html)

    # --- 1. Cohérence CHAPTERS <-> DOM ---
    set_decl, set_dom = set(chapter_ids), set(dom_ids)
    for cid in sorted(set_decl - set_dom):
        errors.append(f"CHAPTERS déclare '{cid}' mais aucun <div id=\"chap-{cid}\"> dans le DOM.")
    for cid in sorted(set_dom - set_decl):
        errors.append(f"<div id=\"chap-{cid}\"> présent dans le DOM mais absent de CHAPTERS.")

    # IDs de chapitre dupliqués dans CHAPTERS
    seen = set()
    for cid in chapter_ids:
        if cid in seen:
            errors.append(f"id de chapitre dupliqué dans CHAPTERS : '{cid}'.")
        seen.add(cid)

    # --- 2. IDs HTML dupliqués ---
    counts = {}
    for hid in all_html_ids(html):
        counts[hid] = counts.get(hid, 0) + 1
    for hid, n in sorted(counts.items()):
        if n > 1:
            if hid == "MathJax-script":
                warnings.append(
                    f"id \"{hid}\" présent {n}× — bénin (2e occurrence dans le template d'impression)."
                )
            else:
                errors.append(f"id HTML dupliqué : \"{hid}\" ({n} occurrences).")

    # --- 3. Flashcards câblées ---
    makeflash_prefixes = set(re.findall(r"makeFlash\([^,]+,\s*'([a-z0-9]+)'", html))
    for c in chapters:
        if "flash" in c["panels"]:
            if not c["prefix"]:
                errors.append(f"chapitre '{c['id']}' : prefix manquant dans CHAPTERS.")
            elif c["prefix"] not in makeflash_prefixes:
                errors.append(
                    f"chapitre '{c['id']}' liste 'flash' mais aucun makeFlash(..., '{c['prefix']}', ...) trouvé."
                )

    # --- 4. drawFn existants ---
    defined_fns = set(re.findall(r"function\s+([A-Za-z0-9_]+)\s*\(", html))
    for c in chapters:
        if c["drawFn"] and c["drawFn"] not in defined_fns:
            errors.append(
                f"chapitre '{c['id']}' : drawFn '{c['drawFn']}' référencé mais fonction non définie."
            )

    # --- Rapport ---
    print(f"Validation de {target.name}")
    print(f"  {len(chapters)} chapitres dans CHAPTERS / {len(dom_ids)} <div class=\"chapter\"> dans le DOM")
    for w in warnings:
        print(f"  [info] {w}")
    if errors:
        print(f"\n{len(errors)} ERREUR(S) :")
        for e in errors:
            print(f"  [X] {e}")
        return 1
    print("\n[OK] Tout est coherent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

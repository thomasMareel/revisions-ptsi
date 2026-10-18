#!/usr/bin/env python3
"""Range le grand <style> d'index.html en RÉGIONS balisées (une par ligne de
travail de la refonte). Chaque règle va dans exactement une région selon son
sélecteur (une liste de sélecteurs à cheval sur plusieurs régions est scindée
en une règle par région, mêmes déclarations) ; les blocs @media sont dupliqués
par région ; l'ordre relatif des règles d'une même région est conservé.

Usage : python3 regions.py index.html [--ecrire] [--json conflits.json]
Sans --ecrire : n'écrit rien, affiche le classement (et les règles non classées).
"""
import re, sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cssparse import parse, split_selectors, strip_comments

REGIONS = ['JETONS', 'BASE', 'COQUILLE', 'PAGE', 'CONTENU', 'SIMU', 'REVISION', 'FENETRES', 'IMPRESSION']

ENTETES = {
    'JETONS': "Jetons de design (tokens.css) : polices, échelle, espacements, couleurs clair/sombre/Auto,\n   rôles dérivés (data-mat), alias des anciens noms. Propriétaire : socle (généré par gen-tokens.py).",
    'BASE': "Reset, typographie de base, icônes, focus, sélection, barres de défilement, mouvement réduit\n   global ; composants de base de composants.css §0 et §1 (.btn, .count, .badge, .chip, kbd,\n   .seg, .field, .menu, .kicker, .stack). Propriétaire : socle.",
    'COQUILLE': "En-tête, navigation (tiroir #mob-drawer, barres de commande invisibles .chap-btn/.sub-btn/\n   .mat-btn), barre du téléphone (#mob-header), menus (Plus, Réviser, ⋯), sélecteur de thème,\n   taille du texte, retour en haut, bandeaux de mise à jour, pied de site. Propriétaire : ligne « coquille ».",
    'PAGE': "Page chapitre : <main>, .chapter, panneaux, intercalaire .chap-title-banner, onglets .tabs,\n   rail .toc (sommaire), pied #chap-pager. Propriétaire : ligne « coquille » (page).",
    'CONTENU': "Contenu des cours : sections, titres, chapô, formules (MathJax), encadrés (.def-box,\n   .prop-box, .method-box, .notice, .reveal), tableaux, listes, schémas SVG, code, exercices\n   (.exo, .solution, .toggle-sol). Propriétaire : ligne « contenu ».",
    'SIMU': "Simulateurs (.sim-wrapper, .sim-controls, .control, .regime-badge, .mode-switch, .sim-info,\n   canvas), Lorentz compris. Propriétaire : ligne « contenu » (simulateurs).",
    'REVISION': "Révision : flashcards (makeFlash), quiz, calcul mental, Aujourd'hui, Bilan (anneau\n   compris), cartes signalées. Propriétaire : ligne « révision ».",
    'FENETRES': "Fenêtres : recherche, formulaire, sauvegarde, raccourcis clavier, toasts et autres\n   overlays. Propriétaire : ligne « thème et fenêtres ».",
    'IMPRESSION': "@media print de la page (le gabarit d'impression printChapter a son propre CSS, dans le\n   script). Propriétaire : ligne « thème et fenêtres » (impression).",
}

# Familles « fortes » : première composante (de gauche à droite) qui en reconnaît une.
FORT = [
    # REVISION / FENETRES / SIMU avant COQUILLE (ex. « .today-chap-btn .mob-filter-tag »)
    (r'^\.mob-ring\b|^\.ring-(bg|fg)\b', 'REVISION'),
    (r'^\.flash-|^#quiz-|^\.quiz-|^\.rate-|^\.score-|^\.fill-|^#drill-|^\.drill-|^\.today-|^#today-|^\.dash-|^#dash-|^\.flag-list\b|^\.flag-empty\b|^\.is-flagged\b|^\[id\$="-stats"\]', 'REVISION'),
    (r'^\.search-|^#search-|^\.formula-|^#formula-|^\.fsheet-|^\.backup-|^#backup-|^#key-help-|^\.key-help-|^\.sr-', 'FENETRES'),
    (r'^\.sim-|^\.control\b|^\.regime-badge\b|^\.mode-switch\b|^#[\w-]+-canvas\b|^\.lor-|^#lor-', 'SIMU'),
    (r'^header\b|^\.header-|^\.hdr-|^#more-|^#study-|^\.rev-badge\b|^#mob-|^\.mob-|^\.matiere-bar\b|^\.mat-btn\b|^\.subdomain-bar\b|^\.sub-btn\b|^\.chapter-bar\b|^\.chap-btn\b|^\.read-size-ctrl\b|^#back-to-top\b|^\.skip-link\b|^\.eyebrow\b|^h1\b|^\.subtitle\b|^footer\b|^\.flag-badge\b|^#sw-update-banner\b', 'COQUILLE'),
    (r'^\.chap-title-banner\b|^\.ctb-|^\.yr2a\b|^nav\.tabs\b|^\.tab\b(?!-)|^\.toc|^#chap-pager\b|^\.chap-pager|^\.cpg-', 'PAGE'),
    (r'^\.course-section\b|^\.sec-num\b|^\.intro\b|^\.formula(?![\w-])|^\.def-box\b|^\.prop-box\b|^\.method-box\b|^\.notice\b|^\.reveal\b|^mjx-container\b|^\.video-resources\b|^\.hors-prog\b|^figure\.schema\b|^\.schema\b|^#sk-arrow|^\.codeblock\b|^\.code-inline\b|^\.exo|^\.solution\b|^\.toggle-sol\b|^\.cine-svg-wrap\b|^\.cours-target-flash\b|^\.step\b', 'CONTENU'),
    (r'^\.ic\b|^\.ic-lbl\b|^\.empty-state\b|^::selection|^::-webkit-scrollbar|^\*', 'BASE'),
]
# Composantes « faibles » : ignorées si une famille forte suit, sinon classées ainsi.
FAIBLE = [
    (r'^:root(\[data-theme="dark"\])?$', None),
    (r'^\.mat-(physique|maths|si|info|anglais)$', None),
    (r'^\.chapter\b|^section\.panel\b|^main\b', 'PAGE'),
    (r'^\.panel\b', 'CONTENU'),
    (r'^(h2|h3|h4|p|li|ul|ol|table|td|th|em|strong)\b', 'CONTENU'),
    (r'^html\b|^body\b|^a\b|^button\b|^input\b|^select\b|^textarea\b|^\[tabindex\]', 'BASE'),
]

# Règles mortes (aucun usage dans le HTML ni le JS, vérifié par grep) : supprimées.
DROP = {
    '.dash-chap .c-mini', '.dash-empty', '.flag-empty', ':root[data-theme="dark"] .flag-empty',
    '.flash-card-inner', '.empty-state.is-ok', '.empty-state.is-ok .ic', '.matiere-bar',
    ':root[data-theme="dark"] .matiere-bar', '.search-empty', '.subtitle', '.fill-hes', '.fill-rev',
}

KEYFRAMES = {
    'mjxIn': 'REVISION', 'modalIn': 'BASE', 'panelIn': 'PAGE', 'panelInLeft': 'PAGE',
    'panelInRight': 'PAGE', 'chapterIn': 'PAGE', 'fadeIn': 'PAGE',
    'coursTargetFlash': 'CONTENU', 'coursTargetFlashDark': 'CONTENU', 'ttsPulse': 'REVISION',
}


def compounds(sel):
    """Composantes d'un sélecteur (séparées par les combinateurs)."""
    s = re.sub(r'\s*([>+~])\s*', r' ', sel.strip())
    out, depth, cur = [], 0, ''
    for c in s:
        if c in '([':
            depth += 1
        elif c in ')]':
            depth -= 1
        if c == ' ' and depth == 0:
            if cur:
                out.append(cur)
            cur = ''
        else:
            cur += c
    if cur:
        out.append(cur)
    return out


def region_selecteur(sel):
    comps = compounds(sel)
    faible = None
    for c in comps:
        for pat, reg in FORT:
            if re.search(pat, c):
                return reg
        for pat, reg in FAIBLE:
            if re.search(pat, c):
                if reg:
                    faible = reg    # la composante la plus à droite (le sujet) l'emporte
                break
    return faible


def est_bloc_variables(rule):
    body = rule['text'][rule['text'].index('{') + 1:rule['text'].rindex('}')]
    decls = [d.strip() for d in strip_comments(body).split(';') if d.strip()]
    return bool(decls) and all(d.startswith('--') for d in decls)


def classer_regle(rule, media):
    """Renvoie une liste [(région, [sélecteurs])] (plusieurs si la liste est scindée)."""
    pre = re.sub(r'\s+', ' ', strip_comments(rule['prelude'])).strip()
    if media and 'print' in media:
        return [('IMPRESSION', None)]
    sels = split_selectors(pre)
    if all(re.fullmatch(r':root(\[data-theme="dark"\])?', s) for s in sels) and est_bloc_variables(rule):
        return [('JETONS', None)]
    if pre == 'html' and 'read-scale' in rule['text']:
        return [('JETONS', None)]
    garder = [x for x in sels if x not in DROP]
    if not garder:
        return [('__DROP__', region_selecteur(sels[0]))]
    retouche = len(garder) != len(sels)
    sels = garder
    groupes = {}
    ordre = []
    for s in sels:
        r = region_selecteur(s)
        if r is None:
            raise SystemExit('Sélecteur non classé : %r (ligne %s)' % (s, rule['line']))
        if r not in groupes:
            groupes[r] = []
            ordre.append(r)
        groupes[r].append(s)
    if len(ordre) == 1:
        return [(ordre[0], groupes[ordre[0]] if retouche else None)]
    return [(r, groupes[r]) for r in ordre]


def texte_regle(rule, sels):
    if sels is None:
        return rule['text']
    corps = rule['text'][rule['text'].index('{'):]
    # garder l'indentation de la 1re ligne du prélude
    return ', '.join(sels) + corps


def lead_propre(lead):
    t = lead.strip('\n')
    # retirer les lignes vides de tête/queue mais garder l'indentation interne
    lignes = t.split('\n')
    while lignes and not lignes[0].strip():
        lignes.pop(0)
    while lignes and not lignes[-1].strip():
        lignes.pop()
    return '\n'.join(lignes)


def ranger(css, base_line):
    items, trailing = parse(css, base_line)
    frags = {r: [] for r in REGIONS}   # région -> liste de (rang, texte)
    meta = []    # pour le contrôle de cascade : une entrée par règle (fragment)
    attente = {}  # commentaire d'une règle supprimée, reporté sur la suivante de sa région

    def ajouter(reg, rang, texte, sep='\n\n'):
        if reg in attente:
            texte = attente.pop(reg) + '\n' + texte
        frags[reg].append((rang, sep, texte))
    rang = 0
    orig = 0
    for it in items:
        rang += 1
        lead = lead_propre(it['lead'])
        blancs = re.match(r'\s*', it['lead']).group(0)
        sep = '\n\n' if (blancs.count('\n') >= 2 or lead) else '\n'
        if it['kind'] == 'at':
            m = re.match(r'@keyframes\s+([\w-]+)', it['prelude'])
            if m:
                reg = KEYFRAMES.get(m.group(1))
                if not reg:
                    raise SystemExit('keyframes non classé : ' + m.group(1))
            else:
                raise SystemExit('at-rule non classée : ' + it['prelude'])
            ajouter(reg, rang, (lead + '\n' if lead else '') + it['text'], sep)
            continue
        if it['kind'] == 'rule':
            orig += 1
            parts = classer_regle(it, None)
            if parts[0][0] == '__DROP__':
                if lead:
                    attente[parts[0][1]] = (attente.get(parts[0][1], '') + '\n' + lead).strip('\n')
                print('supprimée :', re.sub(r'\s+', ' ', it['prelude'])[:80])
                continue
            for k, (reg, sels) in enumerate(parts):
                txt = texte_regle(it, sels)
                ajouter(reg, rang, ((lead + '\n') if (lead and k == 0) else '') + txt, sep)
                meta.append({'orig': orig, 'region': reg, 'rang': rang, 'sub': 0, 'media': None,
                             'prelude': ', '.join(sels) if sels else re.sub(r'\s+', ' ', strip_comments(it['prelude'])).strip(),
                             'body': it['text'][it['text'].index('{') + 1:it['text'].rindex('}')], 'line': it['line']})
            continue
        # groupe @media / @supports
        media = re.sub(r'\s+', ' ', strip_comments(it['prelude'])).strip()
        par_reg = {}
        ordre = []
        sub = 0
        for ch in it['children']:
            sub += 1
            orig += 1
            if ch['kind'] != 'rule':
                raise SystemExit('élément inattendu dans ' + media + ' : ' + ch['prelude'])
            parts = classer_regle(ch, media)
            clead = ch['lead']
            if parts[0][0] == '__DROP__':
                print('supprimée :', media, re.sub(r'\s+', ' ', ch['prelude'])[:80])
                continue
            for k, (reg, sels) in enumerate(parts):
                if reg not in par_reg:
                    par_reg[reg] = []
                    ordre.append(reg)
                txt = texte_regle(ch, sels)
                # indentation : le texte d'une règle commence au sélecteur ; le lead
                # contient les blancs/commentaires qui précèdent (indentation comprise)
                if k == 0:
                    par_reg[reg].append(re.sub(r'^\s*\n', '', clead) + txt)
                else:
                    par_reg[reg].append(_indent(clead) + txt)
                meta.append({'orig': orig, 'region': reg, 'rang': rang, 'sub': sub, 'media': media,
                             'prelude': ', '.join(sels) if sels else re.sub(r'\s+', ' ', strip_comments(ch['prelude'])).strip(),
                             'body': ch['text'][ch['text'].index('{') + 1:ch['text'].rindex('}')], 'line': ch['line']})
        for k, reg in enumerate(ordre):
            corps = '\n'.join(par_reg[reg])
            bloc = it['prelude'].strip() + '{\n' + corps + '\n}'
            ajouter(reg, rang, ((lead + '\n') if (lead and k == 0) else '') + bloc, sep)
    return frags, meta, trailing


def _indent(lead):
    """Indentation de la ligne du sélecteur (fin du lead après le dernier saut)."""
    i = lead.rfind('\n')
    tail = lead[i + 1:] if i >= 0 else lead
    return tail if not tail.strip() else '  '


def assembler(frags, jetons_remplacement=None):
    out = []
    for reg in REGIONS:
        out.append('\n/* ===== RÉGION %s ===== */\n/* %s */\n' % (reg, ENTETES[reg]))
        if reg == 'JETONS' and jetons_remplacement is not None:
            out.append(jetons_remplacement.strip('\n'))
        else:
            liste = sorted(frags[reg], key=lambda x: x[0])
            morceaux = []
            for k, (_, sep, t) in enumerate(liste):
                morceaux.append(('' if k == 0 else sep) + t)
            out.append(''.join(morceaux))
        out.append('\n/* ===== FIN RÉGION %s ===== */\n' % reg)
    return '\n'.join(out) + '\n'


def main():
    chemin = sys.argv[1]
    src = open(chemin, encoding='utf-8').read()
    a = src.index('<style>') + len('<style>')
    b = src.index('</style>', a)
    css = src[a:b]
    base_line = src.count('\n', 0, a) + 1
    frags, meta, trailing = ranger(css, base_line)
    for reg in REGIONS:
        print('%-11s %4d fragments' % (reg, len(frags[reg])))
    if '--json' in sys.argv:
        json.dump(meta, open(sys.argv[sys.argv.index('--json') + 1], 'w'), ensure_ascii=False, indent=0)
    if '--ecrire' in sys.argv:
        neuf = assembler(frags)
        open(chemin, 'w', encoding='utf-8').write(src[:a] + neuf + src[b:])
        print('écrit')
    if '--lister' in sys.argv:
        for m in meta:
            print('%-10s %5s %s %s' % (m['region'], m['line'], ('@' + m['media'] + ' ') if m['media'] else '', m['prelude'][:120]))


if __name__ == '__main__':
    main()

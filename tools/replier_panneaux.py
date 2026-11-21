"""Replie le contenu des onglets Cours, Méthodes et Exercices dans un <template class="pan-tpl">.

Usage : python3 tools/replier_panneaux.py [--verifier]
  (sans option) réécrit index.html : chaque panneau <prefix>-cours|meth|exos dont le contenu n'est pas
                encore replié reçoit <template class="pan-tpl">…</template> AUTOUR de son contenu
                (la balise <section class="panel"> reste en place : onglets, ids, outils inchangés) ;
  --verifier    n'écrit rien : affiche le nombre de panneaux repliés et à replier (code 1 s'il en reste).
Idempotent. Pourquoi : performance au téléphone (≈ 100 000 éléments de moins au démarrage ; le
navigateur lit le contenu d'un <template> sans créer d'éléments ni calculer de styles) ; le site le met
en place à l'ouverture du chapitre (window.__deplierChapitre). Les deux chapitres affichés au départ
(chap-rlc : .chapter.active du <main> principal, visible au démarrage) reste déplié ; chap-ingsys, actif dans le <main>
de SI masqué au départ, est replié depuis le 2026-11-21 (déplié au 1ᵉʳ clic, comme les autres). Un panneau dont les balises
<div>/<section> ne sont pas équilibrées n'est PAS replié (signalé) : le replier changerait l'arbre.
À lancer après toute modification d'un panneau (un panneau réécrit par un outil revient déplié)."""
import re, sys, os
R = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'index.html')
DEPLIES = {'chap-rlc'}
OUV = re.compile(r'<section class="panel(?: active)?" id="([a-z0-9]+)-(cours|meth|exos)">')

def fin_section(s, a):
    """Indice du </section> qui ferme la section ouverte juste avant a (sections imbriquées comptées)."""
    prof = 1
    for m in re.finditer(r'<section\b|</section>', s[a:]):
        prof += 1 if m.group(0) != '</section>' else -1
        if prof == 0: return a + m.start()
    raise ValueError('section non fermée')

def equilibre(t):
    return all(len(re.findall(r'<%s\b' % b, t)) == len(re.findall(r'</%s>' % b, t)) for b in ('div', 'section'))

def main():
    verifier = '--verifier' in sys.argv
    s = open(R, encoding='utf-8').read()
    out, i, faits, deja, refus = [], 0, 0, 0, []
    for m in OUV.finditer(s):
        a = m.end()
        if a < i: continue
        chap = s.rfind('<div class="chapter', 0, m.start())
        cid = re.match(r'<div class="chapter[^"]*" id="([^"]+)"', s[chap:chap + 120]).group(1)
        e = fin_section(s, a)
        corps = s[a:e]
        if corps.startswith('<template class="pan-tpl">'): deja += 1; continue
        if cid in DEPLIES: continue
        if not equilibre(corps): refus.append(m.group(1) + '-' + m.group(2)); continue
        out.append(s[i:a]); out.append('<template class="pan-tpl">' + corps + '</template>'); i = e
        faits += 1
    out.append(s[i:])
    print('repliés : %d déjà, %d maintenant ; non repliés (balises déséquilibrées) : %s' % (deja, faits, ', '.join(refus) or 'aucun'))
    if verifier: sys.exit(1 if faits else 0)
    if faits: open(R, 'w', encoding='utf-8').write(''.join(out))

if __name__ == '__main__': main()

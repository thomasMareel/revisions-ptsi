# Génère ../tokens.css à partir de palette.py (bloc sombre écrit deux fois à l'identique).
# python3 -I gen-tokens.py
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from palette import PAL
OUT = os.path.join(os.path.dirname(__file__), '..', 'tokens.css')
M = ['physique', 'maths', 'si', 'info', 'anglais']
NOMS = {'physique': 'cobalt, h266', 'maths': 'framboise, h350', 'si': 'sarcelle, h177 (sombre h175)',
        'info': 'pétrole, h229 (sombre h221)', 'anglais': 'violet, h304',
        'rouge': 'à revoir, cartes dues, alerte', 'ambre': 'hésitant, « À noter »', 'vert': 'acquis, correction'}
def couleurs(th):
    L = []
    for k in M + ['rouge', 'ambre', 'vert']:
        p = PAL[k][th]
        L.append(f"  --{k}: {p['encre']};{' ' * (9 - len(k))}--{k}-fond: {p['fond']};{' ' * (9 - len(k))}--{k}-vif: {p['vif']};  /* {NOMS[k]} */")
    return '\n'.join(L)

HEAD = r'''/* =========================================================================
   RÉVISIONS PTSI — JETONS DE DESIGN DÉFINITIFS                    tokens.css
   « Cahier de prépa » : base « Livre de science » (P1) + greffes de « Poly &
   fiches » (P3) et « Interface nette » (P2) — voir SPEC.md.
   -------------------------------------------------------------------------
   Fichier GÉNÉRÉ par outils/gen-tokens.py (valeurs de couleur : outils/
   palette.py). Le modifier par le générateur, pas à la main, pour que les deux
   blocs sombres restent identiques (contrôlé par outils/contrastes-jetons.py).

   THÈME — compatible TEL QUEL avec le mécanisme publié (commit 1d2a766) :
   - le script du <head> et le module THÈME posent data-theme="dark" sur <html>
     quand le thème EFFECTIF est sombre (attribut absent = clair) et
     data-theme-pref="light|dark|auto" (la PRÉFÉRENCE) ; window.__setTheme(pref)
     change la préférence, matchMedia la suit en continu en mode Auto ;
   - ce fichier ne lit QUE ces attributs : :root[data-theme="dark"] = sombre ;
     filet de sécurité CSS (avant ou sans JS) : préférence « auto » ou absente
     + système sombre = sombre (même bloc, recopié). Une préférence « light »
     sur un appareil sombre reste claire (aucun sélecteur ne la vise).
   - getCanvasColors()/__CV() continuent de tester data-theme="dark" : rien à
     changer. Les variables qu'ils lisent (--ink, --paper, --accent, --accent2,
     --green, --amber) se résolvent en #rrggbb (exigé par __CVA).

   NOMS EXISTANTS conservés (section 9) : le contenu inline des 160 chapitres
   les emploie (--grid ×1923, --ink ×317, --paper-dark ×205, --accent ×153,
   --muted ×132, --accent2 ×94, --border ×90, --paper ×73, --green ×70,
   --amber ×55, --anglais ×9, --surface ×7, --radius-*, --shadow*, --dom-*,
   --accent-deep, --read-scale). Leurs VALEURS changent, pas leurs noms ;
   --border et --surface (utilisées mais jamais définies) le sont enfin.
   ========================================================================= */

/* ---------- 1. Polices (fichiers locaux : vendor/fonts/polices.css) ------- */
:root{
  /* Texte de cours, titres, questions de cartes. Source Serif 4 : hauteur d'x
     0,475 em, gris à ±2 % des fontes TeX une fois MathJax réglé à
     chtml.scale = 1.07. « Symboles TeX » dessine ⟹ ↔ ∈ ∀… comme les formules ;
     Source Sans 3 fournit ⁺ ⁻ (charges ioniques) absents du serif. */
  --font-text: 'Source Serif 4', 'Symboles TeX', 'Source Sans 3', Georgia, 'Times New Roman', serif;
  /* Interface : boutons, onglets, navigation, badges, compteurs, tableaux,
     simulateurs. Même hauteur d'x que le serif (0,478) : un badge posé dans
     le texte s'aligne. Jamais d'italique. */
  --font-ui: 'Source Sans 3', 'Symboles TeX', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  /* Code Python (85 <pre>), <kbd>, étiquettes des canvas. Plus jamais pour
     des libellés en capitales. Ligatures coupées (« != » reste « != »). */
  --font-code: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, Consolas, monospace;

  --w-regular: 400;
  --w-medium: 500;
  --w-semi: 600;
  --w-strong: 650;   /* gras de lecture dans le serif (<strong> du cours) */
  --w-bold: 700;     /* chiffres-clés, compteurs */

  /* ---------- 2. Échelle typographique fluide (390 px → 1280 px) ---------
     En rem : suit A−/A+ (--read-scale). Commentaire = px téléphone → ordinateur.
     PLANCHER : 13 px pour tout texte ; 12 px seulement pour les compteurs et
     pastilles en gras (--fs-count). Aucune capitale sous 12,5 px.          */
  --fs-count:  0.75rem;                                           /* 12 gras */
  --fs-ui-xs:  0.8125rem;                                         /* 13 */
  --fs-ui-s:   0.875rem;                                          /* 14 */
  --fs-ui:     clamp(0.9375rem, 0.9101rem + 0.1124vw, 1rem);      /* 15 → 16 */
  --fs-ui-l:   1.0625rem;                                         /* 17 grands boutons */
  --fs-kicker: clamp(0.7812rem, 0.7676rem + 0.0562vw, 0.8125rem); /* 12,5 → 13 capitales espacées */
  --fs-small:  clamp(0.9688rem, 0.9414rem + 0.1124vw, 1.0312rem); /* 15,5 → 16,5 notes, légendes, tableaux */
  --fs-sol:    clamp(1.0312rem, 0.9764rem + 0.2247vw, 1.0938rem); /* 16,5 → 17,5 corrections */
  --fs-body:   clamp(1.0938rem, 1.0389rem + 0.2247vw, 1.1875rem); /* 17,5 → 19 corps du cours */
  --fs-lead:   clamp(1.1562rem, 1.0739rem + 0.3371vw, 1.3438rem); /* 18,5 → 21,5 chapô (romain) */
  --fs-h4:     clamp(1.0938rem, 1.0389rem + 0.2247vw, 1.1875rem); /* 17,5 → 19 */
  --fs-h3:     clamp(1.25rem, 1.1677rem + 0.3371vw, 1.4375rem);   /* 20 → 23 */
  --fs-card-q: clamp(1.375rem, 1.2653rem + 0.4494vw, 1.625rem);   /* 22 → 26 question de carte */
  --fs-h2:     clamp(1.5rem, 1.3247rem + 0.7191vw, 2rem);         /* 24 → 32 */
  --fs-h1:     clamp(1.8125rem, 1.4017rem + 1.6854vw, 2.75rem);   /* 29 → 44 titre de chapitre */
  --fs-display: clamp(2.5rem, 2.0618rem + 1.7978vw, 3.5rem);      /* 40 → 56 grands nombres */
  --fs-bar-title: 1.0625rem;                                      /* 17 titre dans la barre téléphone */

  --lh-text: 1.6;    /* corps serif */
  --lh-lead: 1.5;    /* chapô */
  --lh-snug: 1.4;    /* encadrés denses, tableaux, listes de navigation */
  --lh-ui: 1.3;      /* boutons, étiquettes */
  --lh-head: 1.15;   /* titres */
  --track-kicker: 0.075em;    /* capitales espacées (surtitres) */
  --track-h1: -0.018em;       /* titres serif ≥ 32 px */
  --track-head: -0.01em;      /* h2/h3 */

  --measure: 34em;      /* ≈ 66–74 signes par ligne (646 px à 19 px) */
  --measure-ui: 28rem;  /* textes d'interface (dialogues, aides) */

  /* ---------- 3. Espacements (base 4 px, en rem pour suivre A−/A+) ------ */
  --sp-1: 0.25rem;  /*  4 */
  --sp-2: 0.5rem;   /*  8 */
  --sp-3: 0.75rem;  /* 12 */
  --sp-4: 1rem;     /* 16 */
  --sp-5: 1.5rem;   /* 24 */
  --sp-6: 2rem;     /* 32 */
  --sp-7: 3rem;     /* 48 */
  --sp-8: 4rem;     /* 64 */
  /* Rythme du texte (em : proportionnel au corps) */
  --flow-p: 0.8em;        /* entre paragraphes */
  --flow-box: 1.1em;      /* avant/après un encadré ou une formule */
  --flow-h3: 1.9em;       /* avant un h3 */
  --flow-section: 3.2em;  /* entre deux sections § (+ filet) */

  /* ---------- 4. Gabarits ------------------------------------------------ */
  --gutter: 1rem;           /* gouttière téléphone : 16 px */
  --header-h: 3.5rem;       /* 56 px en-tête ordinateur, collant */
  --bar-h: 3.5rem;          /* 56 px barre haute téléphone (2 lignes) */
  --tabs-h: 2.75rem;        /* 44 px onglets collants */
  --sidebar-w: 18rem;       /* 288 px navigation permanente (≥ 1200 px) */
  --rail-w: 15rem;          /* 240 px sommaire + « Mes cartes » (≥ 1360 px) */
  --margin-col: 7rem;       /* 112 px marge « § » de la feuille (≥ 1100 px) */
  --sheet-max: 56rem;       /* 896 px feuille */
  --tap: 2.75rem;           /* 44 px cible tactile minimale (pointer: coarse) */

  /* ---------- 5. Rayons, ombres, mouvement, plans ------------------------ */
  --r-xs: 4px;    /* pastilles, indices */
  --r-s: 6px;     /* badges, puces, kbd */
  --r-m: 10px;    /* boutons, champs, encadrés, formules */
  --r-l: 16px;    /* cartes, feuille, fenêtres */
  --r-xl: 22px;   /* feuilles qui montent du bas (téléphone) */
  --r-full: 999px;

  --ease: cubic-bezier(.2, .7, .2, 1);
  --ease-in-out: cubic-bezier(.6, 0, .3, 1);
  --dur-1: 120ms;   /* survol, appui */
  --dur-2: 200ms;   /* ouverture de menu, repli */
  --dur-3: 320ms;   /* feuille, tiroir, retournement de carte */

  --z-sticky: 20;   /* onglets collants */
  --z-header: 30;   /* en-tête, barre téléphone */
  --z-drawer: 40;   /* tiroir */
  --z-overlay: 50;  /* fenêtres (quiz, Bilan, Aujourd'hui…) */
  --z-menu: 55;     /* menus déroulants, popover Thème */
  --z-toast: 60;    /* bannière de mise à jour, toasts */
}

/* ---------- 6. Couleurs — THÈME CLAIR (valeur par défaut) ---------------- */
:root{
  color-scheme: light;

  /* Fonds : le bureau porte la page, la feuille porte le texte. */
  --desk:  #f3f1ec;   /* fond d'application ; pointillé discret ≥ 1100 px */
  --sheet: #fffdf9;   /* feuille de lecture : blanc chaud, pas crème */
  --sunk:  #f6f3ed;   /* creux : formules, champs, en-têtes de tableau, corrections */
  --raise: #ffffff;   /* menus, fenêtres, cartes de révision */
  --hover: rgba(28, 29, 33, .055);   /* survol des éléments discrets */
  --press: rgba(28, 29, 33, .10);    /* appui */
  --desk-dot: rgba(48, 52, 66, .11); /* pointillé du bureau */
  --scrim: rgba(20, 21, 24, .42);    /* voile sous fenêtres et feuilles */

  /* Encres (rapport sur la feuille) */
  --text:   #1c1d21;  /* 16,6:1 texte courant */
  --text-2: #44464d;  /*  9,3:1 chapô, texte secondaire */
  --text-3: #63656c;  /*  5,7:1 (5,2 sur le bureau) méta, légendes, placeholders */

  /* Filets */
  --line:   #e8e3da;  /* filets décoratifs (séparations de sections, cartes) */
  --line-2: #d6cfc3;  /* séparateurs, bordures de tableau, piste des curseurs */
  --field:  #8b867c;  /* contour des champs et du segment choisi : 3,6:1 (WCAG 1.4.11) */

  /* Action principale : aplat d'encre (Réviser, Afficher la réponse…) */
  --primary: #1c1d21;
  --primary-hover: #34363c;
  --on-primary: #fffdf9;            /* 16,6:1 */
  --focus: #2f62d6;                 /* anneau de focus (≥ 3:1 sur tous les fonds) */
  --link: #3d5db2;                  /* liens du contenu */
  --selection: rgba(61, 93, 178, .16);

  /* Identité « cahier » (décor, sans rôle de texte) */
  --marge: #e9b8ae;                 /* filet rouge de marge (ordinateur) et filet de la fiche bristol */
  --reglure: #dde7f3;               /* réglure bleue de la fiche bristol */
  --bristol: #fffefb;               /* papier de la fiche */
  --mill-a: 10%;                    /* papier millimétré de l'intercalaire : trait fin… */
  --mill-b: 18%;                    /* …et trait du centimètre (part d'encre vive de la matière) */

  /* MATIÈRES — encre (texte ≥ 4,5:1 sur feuille, bureau, menu ET sa teinte),
     teinte de fond, vif (traits, pastilles, barres : ≥ 3:1 sur feuille et teinte).
     SÉMANTIQUE — 3 couleurs seulement, toujours doublées d'une icône et d'un mot. */
@@CLAIR@@
  --rouge-plein: @@ROUGE@@;  --on-rouge-plein: #ffffff;   /* compteur « 37 » */

  /* Ombres (chaudes en clair) */
  --sh-1: 0 1px 2px rgba(40, 34, 24, .07);
  --sh-2: 0 1px 2px rgba(40, 34, 24, .06), 0 8px 24px -8px rgba(40, 34, 24, .16);
  --sh-3: 0 2px 6px rgba(40, 34, 24, .08), 0 24px 56px -16px rgba(40, 34, 24, .28);
  --sh-sheet: 0 0 0 1px var(--line), 0 1px 2px rgba(40, 34, 24, .05), 0 20px 48px -28px rgba(40, 34, 24, .22);
}

/* ---------- 7. Couleurs — THÈME SOMBRE « encre de nuit » ------------------
   Bloc écrit DEUX fois à l'identique (CSS ne sait pas partager un bloc entre un
   sélecteur et une requête média) : thème effectif sombre, puis filet de
   sécurité « Auto + système sombre ». Contrôlé par outils/contrastes-jetons.py. */
:root[data-theme="dark"]{
@@SOMBRE@@
}
@media (prefers-color-scheme: dark){
  :root[data-theme-pref="auto"],
  :root:not([data-theme-pref]):not([data-theme]){
@@SOMBRE2@@
  }
}

/* ---------- 8. Rôles dérivés ---------------------------------------------- */
:root{
  /* Notation des cartes : À revoir / Hésitant / Acquis / jamais vue.
     Hésitant = ambre (l'orange de P1 est supprimé : trop proche du rouge). */
  --note-0: var(--rouge);  --note-0-fond: var(--rouge-fond);  --note-0-vif: var(--rouge-vif);
  --note-1: var(--ambre);  --note-1-fond: var(--ambre-fond);  --note-1-vif: var(--ambre-vif);
  --note-2: var(--vert);   --note-2-fond: var(--vert-fond);   --note-2-vif: var(--vert-vif);
  --note-nv: var(--line-2);
  --formule-fond: var(--sunk);
}
/* Encre du chapitre courant : posée par data-mat="…" sur .chapter (ajout JS à
   côté de data-domain) et sur toute carte, ligne, puce ou badge représentant un
   chapitre ou une matière. Une variable qui en référence une autre est résolue
   là où elle est DÉCLARÉE, d'où le sélecteur double « :root, [data-mat] ». */
:root, [data-mat]{
  --chap: var(--text-2);  --chap-fond: var(--sunk);  --chap-vif: var(--text-3);
  --def-trait: var(--chap-vif);   --def-fond: var(--chap-fond);  --def-titre: var(--chap);
  --prop-trait: var(--chap-vif);  --prop-titre: var(--chap);
  --meth-fond: var(--sunk);       --meth-titre: var(--text);     --meth-pastille: var(--chap-vif);
  --notice-trait: var(--ambre-vif); --notice-fond: var(--ambre-fond); --notice-titre: var(--ambre);
  --reveal-trait: var(--field);
  --sol-trait: var(--vert-vif);   --sol-titre: var(--vert);
  --mill-fin: color-mix(in srgb, var(--chap-vif) var(--mill-a), transparent);
  --mill-cm:  color-mix(in srgb, var(--chap-vif) var(--mill-b), transparent);
}
[data-mat="physique"]{ --chap: var(--physique); --chap-fond: var(--physique-fond); --chap-vif: var(--physique-vif); }
[data-mat="maths"]   { --chap: var(--maths);    --chap-fond: var(--maths-fond);    --chap-vif: var(--maths-vif); }
[data-mat="si"]      { --chap: var(--si);       --chap-fond: var(--si-fond);       --chap-vif: var(--si-vif); }
[data-mat="info"]    { --chap: var(--info);     --chap-fond: var(--info-fond);     --chap-vif: var(--info-vif); }
[data-mat="anglais"] { --chap: var(--anglais);  --chap-fond: var(--anglais-fond);  --chap-vif: var(--anglais-vif); }

/* ---------- 9. COMPATIBILITÉ : noms existants employés par le contenu ------ */
:root{
  --ink: var(--text);
  --paper: var(--sheet);
  --paper-dark: var(--sunk);        /* 158 en-têtes de tableau inline */
  --muted: var(--text-3);
  --grid: var(--line-2);            /* n'est PLUS le quadrillage : filet de tableau */
  --border: var(--line-2);          /* enfin défini (90 bordures jusqu'ici invisibles) */
  --surface: var(--sunk);           /* enfin défini */
  --accent: var(--rouge);           /* « stylo rouge » des schémas et des canvas */
  --accent-deep: var(--rouge);
  --accent2: var(--physique);       /* bleu des schémas */
  --green: var(--vert);
  --amber: var(--ambre);
  /* --anglais : défini avec les matières (section 6/7) */
  --shadow: var(--sh-1);
  --shadow-1: var(--sh-1);
  --shadow-2: var(--sh-2);
  --radius-s: var(--r-s);
  --radius-m: var(--r-m);
  --radius-l: var(--r-l);
  --read-scale: 1;                  /* A−/A+ : 1 / 1.1 / 1.2 (inchangé, posé par le JS) */
  /* Domaines : une seule encre par chapitre, celle de sa MATIÈRE. */
  --dom-ondes: var(--physique);  --dom-thermo: var(--physique);
  --dom-chimie: var(--physique); --dom-meca: var(--physique);
  --dom-elec: var(--si);         --dom-mecasi: var(--si);   --dom-auto: var(--si);
  --dom-maths: var(--maths);
}

/* Zoom de lecture A−/A+ (inchangé : toutes les tailles sont en rem). */
html{ font-size: calc(100% * var(--read-scale)); }

@media (prefers-contrast: more){
  :root{ --text-3: var(--text-2); --line-2: var(--field); --line: var(--line-2); }
}
@media (prefers-reduced-motion: reduce){
  :root{ --dur-1: 0ms; --dur-2: 0ms; --dur-3: 0ms; }
}
'''
SOMBRE = '''  color-scheme: dark;
  --desk:  #111316;  --sheet: #191b20;  --sunk: #20232a;  --raise: #24272e;
  --hover: rgba(232, 230, 225, .06);  --press: rgba(232, 230, 225, .11);
  --desk-dot: rgba(200, 206, 222, .075);  --scrim: rgba(0, 0, 0, .6);
  --text: #e8e6e1;  --text-2: #c2c0ba;  --text-3: #9fa0a6;
  --line: #2b2e35;  --line-2: #3a3e47;  --field: #737885;
  --primary: #e8e6e1;  --primary-hover: #ffffff;  --on-primary: #16181c;
  --focus: #8fb2ff;  --link: #91b2ff;  --selection: rgba(145, 178, 255, .15);
  --marge: #5c3a36;  --reglure: #2a3240;  --bristol: #1d1f25;  --mill-a: 12%;  --mill-b: 22%;
@@C@@
  --rouge-plein: @@RP@@;  --on-rouge-plein: #16181c;
  --sh-1: 0 1px 2px rgba(0, 0, 0, .4);
  --sh-2: 0 1px 2px rgba(0, 0, 0, .35), 0 10px 28px -8px rgba(0, 0, 0, .6);
  --sh-3: 0 0 0 1px rgba(255, 255, 255, .06), 0 24px 60px -12px rgba(0, 0, 0, .75);
  --sh-sheet: 0 0 0 1px var(--line), 0 24px 60px -30px rgba(0, 0, 0, .8);'''
s = SOMBRE.replace('@@C@@', couleurs('sombre')).replace('@@RP@@', PAL['rouge']['sombre']['encre'])
s2 = '\n'.join('  ' + l if l else l for l in s.split('\n'))
css = HEAD.replace('@@CLAIR@@', couleurs('clair')).replace('@@ROUGE@@', PAL['rouge']['clair']['encre']) \
          .replace('@@SOMBRE@@', s).replace('@@SOMBRE2@@', s2)
open(OUT, 'w', encoding='utf-8').write(css)
print('écrit', OUT, len(css), 'octets')

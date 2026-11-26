# enfx (Faux-amis) : revue des cartes, 2026-11-26

## Cartes existantes (16)
Toutes justes ; aucune correction (`enfx-cartes-corr.json` = `[]`).

## Cartes ajoutées (16 → 32), à la fin
- Sciences et technique : physician, petrol, hazard, versatile, to control, a stage.
- Rédaction d'une synthèse : consistent, large, to ignore, to realise, to prevent.
- Vie courante et économie : to pretend, a delay, a lecture, a location (déjà dans le cours, sans carte), a commodity.
- Évité les faux-amis déjà présents dans d'autres paquets : benefit (enec), policy (enpo), experiment (ensc).
- Format du paquet : sens anglais en gras, puis « ≠ mot français piège = traduction anglaise ».

## Lecture audio
Les 32 faces nouvelles sont détectées en français par `__TTS.detectLang` (réponses tournées pour cela).
Neuf faces existantes sont lues avec la voix anglaise alors qu'elles sont en français (cartes 2, 5, 6, 8, 10, 12, 13,
15 : « to wait for », « to ask » pèsent plus que les mots français). Le défaut vient de l'heuristique (chaque lettre
accentuée et « « » » comptent comme un indice), pas des cartes : à corriger dans `__TTS` plutôt que carte par carte.

## Contrôles
`ajouter_cartes.py enfx … --essai` : 16 → 32 cartes ; `corriger_cartes.py … --essai` : 0 correction ; aucun `\(` ni `$`.

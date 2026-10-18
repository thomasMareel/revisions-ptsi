#!/usr/bin/env python3
"""Remplace les mentions nominatives des anciennes polices (Fraunces, Inter Tight)
et les font-family JetBrains Mono du CSS par les jetons --font-text|ui|code ;
noms de familles réels dans les ctx.font et les règles visant du SVG."""
import re, sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
avant = s

# 1) Règles visant du texte SVG : noms réels (les variables n'y sont pas toujours lues)
s = s.replace(".schema text{ font-family:'Inter Tight',system-ui,sans-serif;",
              ".schema text{ font-family:'Source Sans 3',system-ui,sans-serif;")
for cls in ('svg-label', 'svg-label-acc', 'svg-label-vel'):
    s = re.sub(r"(\.%s\{[^}]*?)font-family:'Inter Tight',sans-serif" % re.escape(cls),
               r"\1font-family:'Source Sans 3',sans-serif", s)
# .svg-label-dim garde 'JetBrains Mono' (famille réelle, toujours embarquée)
s = s.replace(".svg-label-dim{fill:var(--accent2);font-family:'JetBrains Mono',monospace;",
              ".svg-label-dim{fill:var(--accent2);font-family:'JetBrains Mono',ui-monospace,monospace;")

# 2) ctx.font des canvas : familles réelles (guillemets : « 3 »/« 4 » ne sont pas des identifiants)
s = s.replace("c.font = 'bold 13px Inter Tight, sans-serif';", "c.font = 'bold 13px \"Source Sans 3\", sans-serif';")
s = s.replace("c.font = 'bold 24px Fraunces, serif';", "c.font = 'bold 24px \"Source Serif 4\", serif';")

# 3) CSS, style="…" et chaînes JS : jetons
s = s.replace("font-family:'Fraunces',serif", "font-family:var(--font-text)")
s = s.replace("font-family:'Inter Tight',system-ui,sans-serif", "font-family:var(--font-ui)")
s = s.replace("font-family:'Inter Tight',sans-serif", "font-family:var(--font-ui)")
s = s.replace("font-family:\\'Inter Tight\\',system-ui,sans-serif", "font-family:var(--font-ui)")
s = s.replace("font-family:'JetBrains Mono',monospace", "font-family:var(--font-code)")
s = s.replace("font-family:\\'JetBrains Mono\\',monospace", "font-family:var(--font-code)")

# 4) <link> des polices (page + gabarit d'impression)
s = s.replace('<link rel="stylesheet" href="vendor/fonts/fonts.css">', '<link rel="stylesheet" href="vendor/fonts/polices.css">')

reste = [l for l in s.split('\n') if 'Fraunces' in l or 'Inter Tight' in l or 'fonts.css' in l]
open(p, 'w', encoding='utf-8').write(s)
print('mentions restantes :', len(reste))
for l in reste:
    print('  ', l.strip()[:160])

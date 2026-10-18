import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cssparse import parse, strip_comments
src = open(sys.argv[1], encoding='utf-8').read()
a = src.index('<style>') + len('<style>')
b = src.index('</style>', a)
css = src[a:b]
base_line = src.count('\n', 0, a) + 1
items, trailing = parse(css, base_line)
def sel(p): return re.sub(r'\s+', ' ', strip_comments(p))
nr = 0
out = []
for it in items:
    if it['kind'] == 'group':
        out.append(f"{it['line']}: @@ {sel(it['prelude'])}")
        for c in it['children']:
            nr += 1
            out.append(f"{c['line']}:    {c['kind'][0]} {sel(c['prelude'])[:170]}")
    else:
        nr += 1
        out.append(f"{it['line']}: {it['kind'][0]} {sel(it['prelude'])[:170]}")
open(sys.argv[2], 'w').write('\n'.join(out) + '\n')
print('TOTAL', len(items), nr, 'trailing', repr(trailing[:80]))
recon = ''.join(it['lead'] + it['text'] for it in items) + trailing
print('recon ok', recon == css)

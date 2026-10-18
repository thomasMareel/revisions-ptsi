(() => {
  const out = [];
  document.querySelectorAll('#rlc-exos .q').forEach((q, i) => {
    if (i > 6) return;
    const s = q.querySelector(':scope > strong');
    const t = s && s.nextSibling;
    const r = document.createRange();
    if (t && t.nodeType === 3) { r.setStart(t, 0); r.setEnd(t, 1); }
    const rs = r.getClientRects();
    const lignes = Array.from(q.getClientRects ? (() => { const rr = document.createRange(); rr.selectNodeContents(q); return rr.getClientRects(); })() : []).map(x => Math.round(x.left));
    out.push({ strongW: s && s.getBoundingClientRect().width, espace: rs.length ? rs[0].width : null, qLeft: q.getBoundingClientRect().left, lignesLeft: Array.from(new Set(lignes)).slice(0, 6) });
  });
  return out;
})()

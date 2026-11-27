"""Replay realizability of Boolean valuations, including both recursive orders."""
from itertools import product, combinations
from collections import Counter

n=4
D=tuple(range(n+2))
inputs=D[2:]
# Every possible Y response table in the shared domain (X precedes Y).
realized=Counter(tuple(f[i]==1 for i in inputs) for f in product(D, repeat=len(D)))
bits=list(product((False,True),repeat=n))
assert set(realized)==set(bits)
assert set(tuple(c==1 for i in inputs) for c in D) <= set(realized)
for assn in bits:
    f={i:int(z) for i,z in zip(inputs,assn)}
    assert tuple(f[i]==1 for i in inputs)==assn
# Exhaust all families of accepted Boolean assignments at dimension four.
# Test Pr(F)=1 by whether any deterministic response-vector witness exists.
for mask in range(1<<len(bits)):
    accepted={z for i,z in enumerate(bits) if (mask>>i)&1}
    assert bool(accepted)==any(z in accepted for z in realized)
# Alternate 3-coloring reduction, all labelled graphs on four vertices.
colors=(0,1,2)
edges=list(combinations(range(n),2))
for mask in range(1<<len(edges)):
    es=[e for j,e in enumerate(edges) if (mask>>j)&1]
    clauses=[(u,v,c) for u,v in es for c in colors]
    witness=any(not any(f[u]==c==f[v] for u,v,c in clauses)
                for f in product(colors,repeat=n))
    assert witness==any(all(f[u]!=f[v] for u,v in es) for f in product(colors,repeat=n))
print('16 valuation types; 65536 Boolean event truth tables, and 64 coloring systems replayed.')

# The illustrated example uses three designated response-table cells.
accepted = set()
for z1, z2, z3 in product((False, True), repeat=3):
    domain = (0, 1, "i1", "i2", "i3")
    response = dict.fromkeys(domain, 0)
    response.update({"i1": int(z1), "i2": int(z2), "i3": int(z3)})
    E1, E2, E3 = (response[i] == 1 for i in domain[2:])
    cross_world = (E1 or not E2) and (E2 or E3) and (not E1 or E3)
    assert cross_world == ((z1 or not z2) and (z2 or z3) and (not z1 or z3))
    if cross_world:
        accepted.add((int(z1), int(z2), int(z3)))
assert accepted == {(0, 0, 1), (1, 0, 1), (1, 1, 1)}
print("All eight worked responses checked; 001, 101 and 111 accepted.")

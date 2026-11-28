# Claims and evidence

| Claim | Evidence |
| --- | --- |
| Two-variable hardness with a supplied finite common domain | [Theorem 1 and §2](paper/manuscript.pdf) |
| Polynomial certificates and the one-variable LP | [§3](paper/manuscript.pdf) |
| Uniform XP equivalence | [§4](paper/manuscript.pdf) |
| Worked truth vectors and other finite checks | [Replay](verification/results/replay.txt) |
| Exact input syntax and prior work | [Primary-source comparison](audits/public_safe_reports/LITERATURE.md) |

## Lean verification

For every Boolean formula over intervention indices and two distinct designated outcomes, satisfiability is equivalent to the existence of a positive-total finite integer-weighted mixture of response tables making the translated event have full mass. Deterministic tables suffice in the forward direction. General finite exogenous probabilities, polynomial bit lengths and membership remain in the paper. [Source and replay](formalization/README.md)

# Lean verification

For every Boolean formula over intervention indices and two distinct designated outcomes, satisfiability is equivalent to the existence of a positive-total finite integer-weighted mixture of response tables making the translated event have full mass. Deterministic tables suffice in the forward direction. General finite exogenous probabilities, polynomial bit lengths and membership remain in the paper.

The checked declaration is `ResponseTable.satisfiable_iff`. [Source](Intervention.lean) · [Pinned CI](../.github/workflows/lean.yml)

```sh
lean -DwarningAsError=true formalization/Intervention.lean
```

CI compares the compiler output with the committed axiom report.

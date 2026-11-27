# Three entries of one response table

Take domain symbols 0, 1, i₁, i₂ and i₃. Each vertex of the cube records the truth values of the three events Eⱼ = [X=iⱼ](Y=1). Every vertex is realized by a deterministic response to the three interventions. An edge flips exactly one response.

The event requires all three clauses.

- E₁ or not E₂
- E₂ or E₃
- Not E₁ or E₃

The accepting responses, written in intervention order, are 001, 101 and 111. For 101, set the three corresponding entries of the function Y=f(X) to 1, 0 and 1. In that deterministic model each clause holds on the unique exogenous draw and the full event has probability one.

A mixture of response tables satisfies the single comparison exactly when it is supported on these three accepting truth vectors. The replay checks all eight cube vertices.

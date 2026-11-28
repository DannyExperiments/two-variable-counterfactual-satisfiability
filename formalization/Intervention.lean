import Std
namespace ResponseTable

/-- Formulas over intervention indices, interpreted by the Boolean events
that the second response equals its designated output at each intervention. -/
inductive Formula (I : Type) where
  | atom (i : I)
  | neg (f : Formula I)
  | conj (f g : Formula I)
  | disj (f g : Formula I)

def eval {I : Type} (x : I → Bool) : Formula I → Bool
  | .atom i => x i
  | .neg f => !(eval x f)
  | .conj f g => eval x f && eval x g
  | .disj f g => eval x f || eval x g

def event {I D : Type} [DecidableEq D] (on : D) (table : I → D) (f : Formula I) :=
  eval (fun i => decide (table i = on)) f

def mass {I D : Type} (rows : List (Nat × (I → D))) : Nat := (rows.map Prod.fst).sum
def accepted {I D : Type} [DecidableEq D] (on : D) (f : Formula I) :
    List (Nat × (I → D)) → Nat
  | [] => 0
  | (w,t)::rs => (if event on t f then w else 0) + accepted on f rs

theorem satisfiable_iff {I D : Type} [DecidableEq D] (off on : D) (different : off ≠ on)
    (f : Formula I) :
    (∃ x : I → Bool, eval x f = true) ↔
    ∃ rows : List (Nat × (I → D)), 0 < mass rows ∧ mass rows ≤ accepted on f rows := by
  constructor
  · rintro ⟨x,h⟩
    let table := fun i => if x i then on else off
    have same : (fun i => decide (table i = on)) = x := by
      funext i; cases he : x i <;> simp [table,he,different]
    have accept : event on table f = true := by simpa [event,same] using h
    exact ⟨[(1,table)],by simp [mass],by simp [mass,accepted,accept]⟩
  · rintro ⟨rows,hp,h⟩
    apply Classical.byContradiction
    intro hn
    have hzero (rs : List (Nat × (I → D))) : accepted on f rs = 0 := by
      induction rs with
      | nil => rfl
      | cons pair tail ih =>
        have bad : event on pair.2 f = false := by
          cases he : event on pair.2 f with
          | false => rfl
          | true => exact False.elim (hn ⟨_,he⟩)
        rcases pair with ⟨w,t⟩
        simp [accepted,bad,ih]
    have := hzero rows
    omega
end ResponseTable
#print axioms ResponseTable.satisfiable_iff

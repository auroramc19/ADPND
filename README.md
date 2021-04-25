# ADPND
Autómata de pila que reconoce el lenguaje -> L1 = {a^n b^n }

Para este autómata de pila no determinista, se tiene que:
Q = {q0, q1, q2, q3}
Ʃ = {a, b}
Γ = {A, B}
z = A
F ={q4}
s = q1
Δ (q0, a, A) = {(q1, BA)}
Δ (q1, a, B) = {(q1, BB)}
Δ (q1, b, B) = {(q2, ε)}
Δ (q2, b, B) = {(q2, ε)}
Δ (q2, ε, A) = {(q3, A)}
Δ (q0, ε, A) = {(q3, ε)}


import sympy as sp
import numpy as np

M = sp.Matrix(sp.var('m0 m1 m2 m3 m4 m5 m6 m7 m8')).reshape(3, 3)
r = sp.Matrix(sp.var('x y z'))
t = sp.Matrix(sp.var('t0 t1 t2'))

eq = M * r - t
sp.pretty_print(eq)

solution = [sp.solve(surface, z) for surface in eq]

vm = np.array(((1.0, 0.1, -0.1), (0.1, 1.0, -0.1), (-0.1, -0.1, 1.0))).reshape(9)
vt = (np.random.random(3) - 0.5) * 0.1

p = sp.Plot()
p[1] = solution[0][0].subs(zip(M[:], vm)).subs(zip(t[:], vt))
p[2] = solution[1][0].subs(zip(M[:], vm)).subs(zip(t[:], vt))
p[3] = solution[2][0].subs(zip(M[:], vm)).subs(zip(t[:], vt))

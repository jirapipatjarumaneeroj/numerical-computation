import math
import numpy as np
fac = math.factorial

def f(x):
    return math.sin(x)

a = 0  # a = the anchor point (a=0 means "Maclaurin series")

def taylor_sin(x, n_terms):
    total = 0
    for n in range(n_terms):
        term = ((-1)**n) * (x**(2*n + 1)) / fac(2*n + 1)
        total += term
    return total

# check against the real answer
x = 0.01
for k in [1, 2, 3, 4]:
    approx = taylor_sin(x, k)
    real = f(x)
    print(f"{k} term(s): approx = {approx:.10f}  real = {real:.10f}  error = {abs(real-approx):.2e}")


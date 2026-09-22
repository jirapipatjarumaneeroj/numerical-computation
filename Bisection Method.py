#bisect
import math

def f(x):
    return x**3 - 2*x - 5#change function here

#the interval right here
a = 2
b = 3

#range = iteration times
for i in range(20):

    c = (a + b) / 2

    print(i, c)

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
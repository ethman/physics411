from math import exp
from random import random,seed

def f(x):
    return (x**(-0.5))/(exp(x) +1)
def w(x):
    return x**(-0.5)

N = 1000000
sum = 0
for i in range(N):
    x = random()
    x *= x
    sum += f(x)/w(x)

I = 2*sum/N
print(I)

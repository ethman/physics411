from banded import banded
from numpy import zeros, arange
from cmath import exp
from visual import curve, rate

# Constants
m = 9.109e-31   # kg
L = 1e-8       # m
x0 = L/2
sig = 1e-10     # m
k = 5e10       # 1/m
hbar = 1.05e-34

h = 1e-18
N = 1000
a = L/N
amp = 1e-9

A = zeros( (3, N+1), complex )
K = h*1j*hbar/(2*m*a*a)
a1 = 1 + K
a2 = -K/2
b1 = 1 - K
b2 = K/2
A[0,:] = A[2,:] = a2
A[1,:] = a1

def psi0(x):
    return exp(- (x-x0)**2 / (2*sig**2) ) * exp(1j*k*x)

xpoints = arange(-L/2,L/2+a, a)
v = zeros(N+1, complex)
for i in range(1,N): 
    v[i] = b1*psi0(i*a)+b2*(psi0((i+1)*a)+psi0((i-1)*a))

c = curve(x=xpoints)


while 1:
   # rate(2000)
    psi = banded(A, v, 1, 1)
    c.y = amp*psi.real
    v[1:N] = b1*psi[1:N] + b2*(psi[2:N+1]+psi[0:N-1])



from visual import curve, rate, color
from math import exp 
from numpy import zeros, arange, copy, array

def psi0(x):
    return C*(x*(x-L)/(L*L))*exp(-(x-d)**2 / (2*sig**2) )

v = 100   # m/s
L = 1.0   # m
d = 0.1   # m
C = 1.0   # m/s
sig = 0.3 # m
N = 100
a = L/N
h = 1e-6
A = 2000

xpoints = arange(0,L+a, a)
phi = zeros(N+1,float)
psi = zeros(N+1, float)
for i,x in enumerate(xpoints): 
    psi[i] = psi0(x)
phi2 = phi.copy()
psi2 = psi.copy()

c = curve(x=xpoints, y=A*phi)

tend = 0.4

t = 0
K = h*v*v/(a*a)
while t<tend:
    rate(1/h)
    c.y = A*phi

    phi2[1:N] = phi[1:N] + h*psi[1:N]
    psi2[1:N] = psi[1:N] + K*(phi[0:N-1]+phi[2:N+1]-2*phi[1:N])
    phi,phi2 = phi2, phi
    psi,psi2 = psi2, psi
    t += h


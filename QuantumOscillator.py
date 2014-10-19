from __future__ import print_function,division
from numpy import array,arange
from gaussxw import gaussxwab
from pylab import show, plot
from math import sqrt

# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
V0 = 50*e
a = 1e-11
L = 10*a
N = 1000
h = L/N
pow = 4

def V(x):
    return V0*(x/a)**pow

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi,fphi],float)

# Function to calculate the wavefunction for a particular energy
def solve(E, phi, doPlot):
    psi = 0.0
    r = array([psi,phi],float)
    xPoints = arange(-L/2, L/2, h)
    yPoints = []

    for x in xPoints:
        yPoints.append(r[0])
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    if(doPlot): plot(xPoints,yPoints)
    return r[0]

def normalizeAndGraph(E):
    n = 100
    x,w = gaussxwab(n,-L/2,0)
    s = 0
    for i in range(n):
        ds = ((hbar**2)/2*m*(V(x[i]-E)))**2
        s += w[i]*ds
    phi = 0.5/sqrt(s)
    solve(E, phi, 1)

# Function to find the energy using the secant method
def findE(Emin, n):
    E1 = Emin*n
    E2 = E1+e
    psi2 = solve(E1, 1.0, 0)
    
    target = e/1000
    while abs(E1-E2)>target:
        psi1,psi2 = psi2,solve(E2, 1.0, 0)
        E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)
    return E2

E0 = findE(0, 0)
E1 = findE(E0,pow)
E2 = findE(E0,2*pow) 
print("E0 =",E0/e,"eV\tE1 = ", E1/e, "eV\tE2 = ", E2/e, "eV")
normalizeAndGraph(E0)
normalizeAndGraph(E1)
normalizeAndGraph(E2)
show()

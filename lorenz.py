from __future__ import print_function,division

from math import cos
from numpy import empty,array,arange,concatenate, zeros
from visual import sphere,rate, curve, color

sig = 10
r   = 28
b   = 8/3

def f(R,t):
    x = R[0]
    y = R[1]
    z = R[2]
    fx = sig *(y-x)
    fy = r*x-y-x*z
    fz = x*y-b*z
    return array([fx,fy,fz], float)

t1 = 0.0
t2 = 100.0
N = 10000
num = 500
h = (t2-t1)/N
R = array([0,1,0],float)
s = sphere(radius=0.1, pos=R)
c = curve( color = color.green)

framerate = int(N/(t2-t1))
tpoints = arange(t1,t2,h)


for t in tpoints:
    rate(framerate)
    s.pos = [R[0], R[1], R[2] ]
    c.append(pos=(R[0],R[1],R[2]) )
    
    k1 = h*f(R,t)
    k2 = h*f(R+0.5*k1,t+0.5*h)
    k3 = h*f(R+0.5*k2,t+0.5*h)
    k4 = h*f(R+k3,t+h)
    R += (k1+2*k2+2*k3+k4)/6



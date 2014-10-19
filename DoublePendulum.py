from __future__ import print_function,division
from math import sin, pi, cos
from numpy import arange, array
from pylab import plot, xlabel, ylabel,show
from visual import sphere,rate,curve

g = 9.81
l = 0.4

def f(r,t):
    t1 = r[0]
    t2 = r[1]
    o1 = r[2]
    o2 = r[3]
    ft1 = o1
    ft2 = o2
    
    fo1 = o1**2 *sin(2*t1-2*t2) + 2*o2**2 *sin(t1 - t2) + (g/l) * (sin(t1-2*t2) + 3*sin(t1) )
    fo1 /= - (3 - cos(2*t1-t2) )

    fo2 = 4*o1**2 *sin(t1-t2) + o2**2 *sin(2*t1-2*t2) + 2*(g/l)*(sin(2*t1-t2)-sin(t2))
    fo2 /= (3- cos(2*t1-t2) )
                        
    return array([ft1,ft2,fo1,fo2],float)

a = 0.0
b = 10.0
N = 100000
h = (b-a)/N
tI1 = tI2 = 90./180.*pi
framerate = int(N/(b-a) )

tpoints = arange(a,b,h)
thetaPoints = []
s1 = sphere(radius=l/10, pos=[l*cos(tI1-pi/2), l*sin(tI1-pi/2)])
s2 = sphere(radius=l/10, pos=[2*l*cos(tI2-pi/2), 2*l*sin(tI2-pi/2)]) 
c1 = curve(pos=[(0,0),(l*cos(tI1-pi/2), l*sin(tI1-pi/2))])
c2 = curve(pos=[(l*cos(tI2-pi/2), l*sin(tI2-pi/2)),(2*l*cos(tI2-pi/2), 2*l*sin(tI2-pi/2))])

r = array([tI1,tI2, 0.0, 0.0],float)
for t in tpoints:
#    thetaPoints.append(r[0])
    rate(framerate)
    c1.visible = c2.visible = False
    del c1, c2

    s1.pos = [l*cos(r[0]-pi/2), l*sin(r[0]-pi/2) ]
    c1 = curve(pos=[(0,0),(l*cos(r[0]-pi/2), l*sin(r[0]-pi/2))])
    s2.pos = s1.pos + [l*cos(r[2]-pi/2), l*sin(r[2]-pi/2)]
    c2 = curve(pos=[s1.pos, s2.pos])
       
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

#plot(tpoints,thetaPoints)
#show()

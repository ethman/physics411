from visual import sphere,rate,display,color
from random import random,seed


seed(1)
display = display(background = color.white)

L = 101
N = 1000000

p = sphere(pos=(L//2,L//2,0), radius=1, make_trail=True, color=color.black)
display.center = p.pos

for i in range(N):
    rate(100)
    badMove = 1
    while badMove:
        move = random()
        if move <= 0.25:
            p.pos += (1,0,0)
        elif move <= 0.5:
            p.pos += (-1,0,0)
        elif move <= 0.75:
            p.pos += (0,1,0)
        else:
            p.pos += (0,-1,0)
        if p.pos[0] < L and p.pos[0] >= 0 and p.pos[1] <  L and p.pos[1] >= 0:
            badMove = 0

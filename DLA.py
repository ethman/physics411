from numpy import empty
from visual import sphere,display
from random import random,seed

#seed(1)
L = 301
grid = empty([L,L], dtype='bool')
grid[::] = False

#N = 1000
#pos = [L//2,L//2]
display(center=[L//2,L//2])

while not grid[L//2,L//2]:
    keepGoing = 1
    pos = [L//2,L//2]
    while keepGoing:
        # Decide which direction to move
        m = random()
        if m < 0.25:
            pos[0] += 1
        elif m < 0.5:
            pos[0] -= 1
        elif m < 0.75:
            pos[1] += 1
        else:
            pos[1] -= 1
            
        # Decide to keep going or stop
        # Have we hit an edge?
        if pos[0]+1 >= L or pos[0]-1 < 0 or pos[1]+1 >=  L or pos[1]-1 < 0:
            keepGoing = 0
            grid[pos[0],pos[1]] = True
        # No? Than are we next to another particle?
        elif(grid[pos[0]+1,pos[1]]-grid[pos[0]-1,pos[1]]-grid[pos[0],pos[1]+1]-grid[pos[0],pos[1]-1]).any():
            keepGoing = 0
            grid[pos[0],pos[1]] = True
        
        
    p = sphere(pos=pos, radius=0.7)
    

#print(grid)

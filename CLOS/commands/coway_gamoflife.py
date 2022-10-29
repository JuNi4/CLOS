from collections import Counter
import os
import time

def life(world, N):
    "Play Conway's game of life for N generations from initial world."
    for g in range(N+1):
        os.system('cls')
        display(world, g)
        counts = Counter(n for c in world for n in offset(neighboring_cells, c))
        world = {c for c in counts 
                if counts[c] == 3 or (counts[c] == 2 and c in world)}
        time.sleep(1)
 
neighboring_cells = [(-1, -1), (-1, 0), (-1, 1), 
                     ( 0, -1),          ( 0, 1), 
                     ( 1, -1), ( 1, 0), ( 1, 1)]
 
def offset(cells, delta):
    "Slide/offset all the cells by delta, a (dx, dy) vector."
    (dx, dy) = delta
    return {(x+dx, y+dy) for (x, y) in cells}

def rgb(r=0,g=255,b=50):
    return '\033[48;2;'+str(r)+';'+str(g)+';'+str(b)+'m'

res = '\033[21m'+'\033[22m'+'\033[24m'+'\033[25m'+'\033[27m'+'\033[28m'+'\033[39m'+'\033[49m'

def display(world, g):
    "Display the world as a grid of characters."
    print('          GENERATION {}:'.format(g))
    Xs, Ys = zip(*world)
    Xrange = range(min(Xs), max(Xs)+1)
    for y in range(min(Ys), max(Ys)+1):
        print(''.join(rgb(200,200,200)+'..'+res if (x, y) in world else rgb(100,100,100)+'..'+res
                      for x in Xrange))
 
blinker = {(1, 0), (1, 1), (1, 2)}
block   = {(0, 0), (1, 1), (0, 1), (1, 0)}
toad    = {(1, 2), (0, 1), (0, 0), (0, 2), (1, 3), (1, 1)}
glider  = {(0, 1), (1, 0), (0, 0), (0, 2), (2, 1)}
world   = (block | offset(blinker, (5, 2)) | offset(glider, (15, 5)) | offset(toad, (25, 5))
           | {(18, 2), (19, 2), (20, 2), (21, 2)} | offset(block, (45, 10)))
 
 
life(world, 50)
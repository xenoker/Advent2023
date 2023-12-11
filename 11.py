from puzzleinput import getlines
from itertools import combinations
L = getlines(11)

M = [(x,y) for y,l in enumerate(L) for x,c in enumerate(l) if c == '#']

YP = [all(x!='#' for x in r) for r in L]
XP = [all(y[c]!='#' for y in L) for c in range(len(L[0]))]

def dist(p): return sum(abs(b-a) for a,b in zip(*p))

def expanded(m): return [(x+m*sum(XP[:x]),y+m*sum(YP[:y])) for x,y in M]

def part(e): return sum(map(dist,combinations(expanded(e),2)))

if __name__ == '__main__':
    assert part(1)==9591768
    assert part(999999)==746962097860

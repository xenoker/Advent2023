from puzzleinput import getlines
from itertools import pairwise

L = [list(map(int,l.split())) for l in getlines(9)]

def part(p2=False):
    S = 0
    for l in L:
        s,j = [l],0
        while any(s[0]): s.insert(0,[b-a for a,b in pairwise(s[0])])
        for si in [x[[-1,0][p2]] for x in s]: j=si+([j,-j][p2])
        S+=j
    return S

if __name__ == '__main__':
    assert part()==1842168671
    assert part(p2=True)==903

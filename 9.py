from puzzleinput import getlines
from itertools import pairwise

L = [list(map(int,l.split())) for l in getlines(9)]

def part(p2=False):
    S = 0
    for l in L:
        s = [l[::[1,-1][p2]]]
        while any(s[0]): s.insert(0,[b-a for a,b in pairwise(s[0])])
        S += sum(x[-1] for x in s)
    return S

if __name__ == '__main__':
    assert part()==1842168671
    assert part(p2=True)==903

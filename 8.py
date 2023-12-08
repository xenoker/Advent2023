from puzzleinput import getlines
from itertools import cycle
from math import lcm

L = getlines(8)
D = dict((x[:3],(x[7:10],x[12:15]))for x in L[1:])

def part1():
    p = 'AAA'
    for i,d in enumerate(cycle(L[0]),1):
        p = D[p]['LR'.index(d)]
        if p == 'ZZZ': return i

def part2():
    A = dict()
    pl = [p for p in D.keys() if p[2]=='A']
    for i,d in enumerate(cycle(L[0]),1):
        pl = [D[p]['LR'.index(d)] for p in pl if p not in A]
        if not pl: return lcm(*A.values())
        A.update((s,i) for s in pl if s[2]=='Z')

if __name__ == '__main__':
    assert part1()==22357
    assert part2()==10371555451871

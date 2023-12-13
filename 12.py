from puzzleinput import getlines
from functools import cache

L = []
for l in getlines(12):
    a,b = l.split()
    L.append((a,tuple(map(int,b.split(',')))))

@cache
def recurse(c, g, cg=0):
    if not c:
        if len(g) == 1 and cg == g[0]: return 1
        if not cg and len(g) == 0:     return 1
        return 0
    if cg and not g: return 0
    if c[0] == '.' and cg and cg != g[0]: return 0
    a = 0
    if c[0] == '.' and cg:      a += recurse(c[1:], g[1:])
    if c[0] == '?' and cg and cg == g[0]: a += recurse(c[1:], g[1:])
    if c[0] in '#?' and cg:     a += recurse(c[1:], g, cg+1)
    if c[0] in '#?' and not cg: a += recurse(c[1:], g, 1)
    if c[0] in '.?' and not cg: a += recurse(c[1:], g)
    return a

def part1():
    return sum(recurse(a,b) for a,b in L)

def part2():
    x5 = lambda a:'?'.join([a]*5)
    return sum(recurse(x5(a),b*5) for a,b in L)

if __name__ == '__main__':
    assert part1()==7260
    assert part2()==1909291258644

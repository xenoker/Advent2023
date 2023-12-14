from puzzleinput import getlines
G = getlines(14)
W,H = len(G[0]), len(G)
M = set((x,y) for y,l in enumerate(G) for x,z in enumerate(l) if z == 'O')
S = set((x,y) for y,l in enumerate(G) for x,z in enumerate(l) if z == '#')

def tilt(L,dx,dy):
    while True:
        m = 0
        for x,y in L:
            x2,y2 = x+dx,y+dy
            if not 0<=x2<W or not 0<=y2<H: continue
            if (x2,y2) in L or (x2,y2) in S: continue
            L.remove((x,y))
            L.add((x2,y2))
            m += 1
        if not m: break
    return L

def load(L):
    return sum(H-y for x,y in L)

def part1():
    return load(tilt(M.copy(),0,-1))

def part2():
    L = M.copy()
    hist = dict()
    for i in range(1,9999):
        hist[frozenset(L)] = i-1
        for x,y in ((0,-1),(-1,0),(0,1),(1,0)): L = tilt(L,x,y)
        s = frozenset(L)
        if s in hist:
            r = i-hist[s]
            if not (1000000000 - i)%r: return load(L)

if __name__ == '__main__':
    assert part1()==105003
    assert part2()==93742

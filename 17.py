from puzzleinput import getlines
from heapq import heappop, heappush
from collections import defaultdict

L = getlines(17)
M = dict(((x,y),int(z)) for y,l in enumerate(L) for x,z in enumerate(l))
T = [len(L[0])-1, len(L)-1]

class Dijkstraish: #reuse a bit of previous years code
    def __init__(self, mapd:dict, end):
        self.MAP = mapd
        self.END = tuple(end)

    def search(self, t1, p2):
        px,py,nd,dr = t1
        for d,dx,dy in [(0,1,0),(1,0,1),(2,-1,0),(3,0,-1)]:
            if abs(dr-d)==2: continue
            if (px+dx,py+dy) not in self.MAP: continue
            if not p2 and nd==3 and d==dr: continue
            if p2 and nd==10 and d==dr: continue
            if p2 and nd<4 and d!=dr: continue
            yield (px+dx,py+dy,[1,nd+1][d==dr],d)
     
    def solve(self, part2=False) -> int: 
        Q = [(0,(0,0,0,0)),(0,(0,0,0,1))]
        self.DIST = defaultdict(lambda:99999)
        self.DIST[Q[0][1]] = 0
        self.DIST[Q[1][1]] = 0
        S = set()
        while Q:
            d1,t1 = heappop(Q)
            if t1 in S: continue
            S.add(t1)
            for t2 in self.search(t1, part2):
                t2d = self.DIST[t1] + self.MAP[tuple(t2[:2])]
                if t2d < (self.DIST[t2]):
                    self.DIST[t2] = t2d
                    heappush(Q, (t2d, t2))
        return min(d for k,d in self.DIST.items() if k[:2]==self.END)

def part1():
    return Dijkstraish(M, T).solve()

def part2():
    return Dijkstraish(M, T).solve(True)

if __name__ == '__main__':
    assert part1()==970
    assert part2()==1149    

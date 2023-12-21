from puzzleinput import getlines
from numpy import array, polyfit, polyval
L = getlines(21)
G = set((x,y) for y,l in enumerate(L) for x,z in enumerate(l) if z in '.S')
S = [(x,y) for y,l in enumerate(L) for x,z in enumerate(l) if z=='S'][0]
H,W = len(L),len(L[0])
assert H==W #not going to deal with this not being the case for part 2

class Steppage:
    def __init__(self, p2=False):
        self.p2 = p2
    def search(self, p1):
        px,py = p1
        L = []
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            p2 = (px+dx),(py+dy)
            p2m = (p2[0]%W,p2[1]%H)
            if [p2,p2m][self.p2] not in G: continue
            yield p2
    def step(self): 
        Q2 = set()
        while self.Q:
            p1 = self.Q.pop()
            for p2 in self.search(p1):
                Q2.add(p2)
        self.Q = Q2
    def solve(self,steps):
        self.Q = set([S])
        for s in range(1,steps+1):
            self.step()
        return len(self.Q)

def part1():
    return Steppage().solve(64)

def part2(step=26501365):
    m,r = divmod(step,W)
    xs = [r,W+r,W*2+r]
    ys = [Steppage(p2=True).solve(x) for x in xs]
    pol = polyfit(xs,ys,2)
    return int(polyval(pol,step))

if __name__ == '__main__':
    assert part1()==3585
    assert part2()==597102953699891

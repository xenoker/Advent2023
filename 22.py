from puzzleinput import getlines
L = [tuple(map(int,l.replace('~',',').split(','))) for l in getlines(22)]

class Brick:
    def __init__(self,pl):
        self.pl = pl
        self.s = self.getset()
        self.s2 = self.getset(True)
        self.on = set()
        self.under = set()
    def getset(self,d=False):
        x0,y0,z0,x1,y1,z1 = self.pl
        if d: z0,z1 = z0-1,z1-1
        return set((x,y,z) for x in range(x0,x1+1) for y in range(y0,y1+1) for z in range(z0,z1+1))
    def couldfall(self,lst,ig=None,dofall=False):
        if self.pl[2] == 0: return False
        for br in lst:
            if br == ig: continue
            if br == self: continue
            if (self.pl[2]-br.pl[5])!=1: continue 
            if self.s2 & br.s: return False
        if dofall: self.fall()
        return True
    def fall(self):
        x0,y0,z0,x1,y1,z1 = self.pl
        z0,z1 = z0-1,z1-1
        self.pl = x0,y0,z0,x1,y1,z1
        self.s = self.getset()
        self.s2 = self.getset(True)
    def setsupport(self,lst):
        if self.pl[2] == 0:
            self.under.add(-1)
            return
        for br in lst:
            if br == self: continue
            if (self.pl[2]-br.pl[5])!=1: continue
            if self.s2 & br.s:
                self.under.add(br.id)
                br.on.add(self.id)
        
B = [Brick(l) for l in L]
B.sort(key=lambda x:x.pl[2])
moved = True
N = 0
while moved:
    moved = False
    for n,br in enumerate(B[N:]):
        fall = br.couldfall(B, dofall=True)
        if not moved and fall:
            N+= n
            moved = True
for i,b in enumerate(B): b.id = i
for b in B: b.setsupport(B)

def wouldfall(n):
    would = set([n])
    could = B[n].on.copy()
    todo = B[n].on.copy()
    while todo:
        t = todo.pop()
        on = B[t].on.copy()
        could.update(on)
        todo.update(on)
    add = True
    while add:
        add = False
        for c in could:
            b = B[c]
            if not b.under-would:
                if c not in would: add = True
                would.add(c)
    return would-{n}

def part1():
    return sum([1 for n in range(len(B)) if len(wouldfall(n))==0])

def part2():
    return sum([len(wouldfall(n)) for n in range(len(B))])   

if __name__ == '__main__':
    assert part1()==488
    assert part2()==79465

from puzzleinput import getlines
from numpy import array, linalg
from itertools import combinations
from z3 import Solver, RealVector, sat

class stone():
    def __init__(self,line):
        L = list(map(int,line.replace('@ ','').replace(',','').split()))
        self.p = array(L[0:3]).T
        self.v = array(L[3:]).T
    def intersect2d(self,s2):
        #vx1*t - vx2*t = x2 - x1
        #vy1*t - vy2*t = y2 - y1
        try: r = linalg.solve(array([self.v[:2], -s2.v[:2]]).T, s2.p[:2]-self.p[:2])
        except linalg.LinAlgError: return (None,None)
        else: return r,self.v[:2]*r[0]+self.p[:2]

S = [stone(l) for l in getlines(24)]    

def part1(mi,mx):
    I = 0
    for a,b in combinations(S,2):
        ts, xy = a.intersect2d(b)
        if ts is None: continue
        if all(x>0 for x in ts) and all(mi<=x<=mx for x in xy): I+=1
    return I

def part2():
    #unsure how to solve this system like p1, so offload to a solver
    #3 stones, 9 equations, 9 unknowns: x0,y0,z0,vx,vy,vz,t1,t2,t3
    vr,pr,tr = [RealVector(x,3) for x in 'vpt']
    Z = Solver()
    Z.add(*[pr[i]+vr[i]*t==s.p[i]+s.v[i]*t for t,s in zip(tr,S) for i in range(3)])
    Z.add(*[t >= 0 for t in tr])
    assert Z.check() == sat
    return Z.model().eval(sum(pr))
    
if __name__ == '__main__':
    assert part1(200000000000000,400000000000000)==26611
    assert part2()==684195328708898

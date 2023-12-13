from puzzleinput import getlines,get
from itertools import groupby

L = [list(g) for k,g in groupby(getlines(13,True),bool) if k]

def part(n):
    S = 0
    diff = lambda a,b:sum(x!=y for x,y in zip(a,b))
    for p0 in L:
        pr = [''.join(y[x] for y in p0) for x in range(len(p0[0]))]
        for p,m in ((p0,100),(pr,1)):        
            for i in range(len(p)):
                c = [diff(a,b) for a,b in zip(p[i::-1],p[i+1:])]
                if c and sum(c)==n: S += m*(i+1)
    return S

if __name__ == '__main__':
    assert part(0)==36015
    assert part(1)==35335

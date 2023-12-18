from puzzleinput import getlines
L =[x.split() for x in getlines(18)]
D = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}

def vert(p2=False):
    P,V,E = (0,0), [], 0
    for l in L:
        a,b,c = l
        if not p2: b=int(b)
        else:
            a = 'RDLU'[int(c[-2])]
            b = int(c[2:7],16)
        P = (P[0]+D[a][0]*b, P[1]+D[a][1]*b)
        E += b
        V.append(P)
    return V,E

def shoelace(pl,v2=False):
    X = [p[not v2] for p in pl]
    Y = [p[v2] for p in pl]
    return sum(x*y for x,y in zip(X,Y[1:]+[Y[0]]))

def part(p2=False):
    V,E = vert(p2)
    return int(abs(shoelace(V)-shoelace(V,True))/2 + E/2 +1)
    
if __name__ == '__main__':
    assert part()==92758
    assert part(p2=True)==62762509300678

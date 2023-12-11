from puzzleinput import getlines
L = getlines(10)
DIR = {'|':((0,-1),(0,1)), '-':((-1,0),(1,0)), 'L':((0,-1),(1,0)),
       'J':((0,-1),(-1,0)), '7':((0,1),(-1,0)), 'F':((0,1),(1,0))}
D = dict(((x,y),z) for y,l in enumerate(L) for x,z in enumerate(l))

def reach(x,y):
    s = D.get((x,y))
    if not s or s=='.' or s=='S': return []
    return [(x+dx,y+dy) for dx,dy in DIR[D[(x,y)]]]

def step(fx,fy,x,y):
    r = reach(x,y)
    if (fx,fy) not in r: return False
    if D.get((x,y)) == 'S': return False
    return r[not r.index((fx,fy))]

def loop():
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        sx,sy = dict((b,a) for a,b in D.items())['S']
        jx,jy = sx+dx, sy+dy
        L = [(jx,jy)]
        while S:=step(sx,sy,jx,jy):
            sx,sy = jx,jy
            jx,jy = S
            L.append((jx,jy))
        if len(L) > 2: return L

def part1():
    return int(len(loop())/2)

def part2():
    LO = loop()
    M = set(D.keys()) - set(LO)
    #S included or not included, too lazy to programmatically determine
    return sum(sum(D.get((x,j)) in 'SJ|L' for x in range(0,i) if (x,j) in LO)%2==1 for i,j in M)

if __name__ == '__main__':
    assert part1()==6846
    assert part2()==325

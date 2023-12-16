from puzzleinput import getlines
L = getlines(16)

H,W = len(L), len(L[0])
D = dict(((x,y),z) for y,l in enumerate(L) for x,z in enumerate(l))

R = {('/',1,0):((0,-1),),      ('/',-1,0):((0,1),),       ('/',0,1):((-1,0),),      ('/',0,-1):((1,0),), 
     ('\\',1,0):((0,1),),      ('\\',-1,0):((0,-1),),     ('\\',0,1):((1,0),),      ('\\',0,-1):((-1,0),), 
     ('-',1,0):((1,0),),       ('-',-1,0):((-1,0),),      ('-',0,1):((1,0),(-1,0)), ('-',0,-1):((1,0),(-1,0)), 
     ('|',1,0):((0,1),(0,-1)), ('|',-1,0):((0,1),(0,-1)), ('|',0,1):((0,1),),       ('|',0,-1):((0,-1),) }

def beam(p0,d0):
    A,B,C = [(p0,d0)],set(),set()
    while A:
        p,d = A.pop()
        if p not in D: continue
        C.add(p)
        if (p,d) in B: continue
        B.add((p,d))
        for r in R.get( (D[p],d[0],d[1]) , (d,) ):
            A.append( ( (p[0]+r[0],p[1]+r[1]) ,r) )
    return len(C)

def part1():
    return beam((0,0),(1,0))

def part2():
    M = 0
    for x in range(W):
        for y,d in [(0,(0,1)),(H-1,(0,-1))]:
            M = max(M, beam( (x,y),d) )
    for y in range(H):
        for x,d in [(0,(1,0)),(H-1,(-1,0))]:
            M = max(M, beam( (x,y),d) )
    return M    

if __name__ == '__main__':
    assert part1()==6622
    assert part2()==7130

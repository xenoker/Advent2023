from puzzleinput import getlines
from collections import deque
from math import lcm
L = getlines(20)

M = dict()
for line in L:
    a,b,c = line.split(maxsplit=2)
    M[a[1:]] = (a[0],c.split(', '))
C = dict((a,[x for x,y in M.items() if a in y[1]]) for a,b in M.items())

def part(p2=False):
    S,p2d = dict(),dict()
    L,H,N = 0,0,0
    while True:
        Q = deque([('button','roadcaster',False)])
        N += 1
        while Q:
            frm, name, state = Q.popleft()
            if state: H += 1
            else: L += 1
            if name not in M: continue
            typ, dest = M[name]
            if typ == 'b':
                for d in dest:
                    Q.append((name,d,state))
            elif typ == '%':
                if state: continue
                ncur = not S.get(name,False)
                S[name] = ncur
                for d in dest:
                    Q.append((name,d,ncur))
            elif typ == '&':
                di = S.get(name,dict((x,False) for x in C[name]))
                di[frm] = state
                S[name] = di
                if p2 and name =='zh' and state: #&zh -> rx
                    if frm not in p2d: p2d[frm] = N
                    if len(p2d) == len(C['zh']): return lcm(*p2d.values())
                snd = not (all(v for v in di.values()))
                for d in dest:
                    Q.append((name,d,snd))
        if not p2 and N == 1000: return L*H

if __name__ == '__main__':
    assert part()==886701120 
    assert part(p2=True)==228134431501037

from puzzleinput import get
from collections import deque
from math import prod

RL,IL = get(19).split('\n\n')
R,I = dict(),[]
for r in RL.split('\n'):
    i = r.find('{')
    name = r[:i]
    rules = r[i+1:-1].split(',')
    rul,els = rules[:-1], rules[-1]
    tl = []
    for ri in rul:
        a,b = ri.split(':')
        tl.append((a[0],a[1],a[2:],b))
    R[name] = (tl, els)

for i in IL.split('\n'):
    I.append(dict(j.split('=') for j in i[1:-1].split(',') ))


def part1():
    S = 0
    for d in I:
        r = 'in'
        while r not in 'AR':
            rules,els = R[r]
            for rule in rules:
                a,b,c,o = rule
                if b=='<' and int(d[a]) < int(c):
                    r = o; break
                if b=='>' and int(d[a]) > int(c):
                    r = o; break
            else:
                r = els
        if r == 'A': S += sum(int(x) for x in d.values())
    return S


def apply(var, op, n, L, eq=False):
    L2 = L.copy()
    i = 'xmas'.index(var)
    lo,hi = L[0+i*2:2+i*2]
    if op=='>': tmp = [max(lo, n+[1,0][eq]), hi]
    elif op =='<': tmp = [lo, min(hi, n-[1,0][eq])]
    L2[0+i*2:2+i*2] = tmp
    return L2

def part2():
    ans = 0
    Q = deque([('in', [1, 4000, 1, 4000, 1, 4000, 1,4000])])
    while Q:
        r, L = Q.pop()
        if any(l>h for l,h in zip(L[0::2],L[1::2])): continue
        if r=='A': ans += prod(h-l+1 for l,h in zip(L[0::2],L[1::2]))
        elif r=='R': continue
        else:
            rules,els = R[r]
            for rule in rules:
                a,b,c,o = rule
                Q.append((o, apply(a,b,int(c),L) ))
                L = apply(a,{'<':'>','>':'<'}[b],int(c),L,eq=True)
            Q.append((els,L))
    return ans

if __name__ == '__main__':
    assert part1()==399284
    assert part2()==121964982771486

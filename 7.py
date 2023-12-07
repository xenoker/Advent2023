from puzzleinput import getlines
L = [x.split() for x in getlines(7)]

R =  dict((b,a) for a,b in enumerate('X23456789TJQKA'))
R2 = dict((b,a) for a,b in enumerate('J23456789TXQKA'))

def score(p, p2=False):
    h = p[0]
    I = tuple(sorted(map(h.count,set(h))))
    V = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)].index(I)
    if p2: return [V]+list(R2[x] for x in p2)
    return [V]+list(R[x] for x in h)

def score2(pi):
    p = pi[0]
    if 'J' not in p: return score(pi)
    S = [score((p.replace('J',c),),p) for c in '23456789TQKA' ]
    return sorted(S)[-1]

def part(p2=False):
    L2 = [(a,int(b)) for a,b in L]
    if p2: L2.sort(key=score2)
    else: L2.sort(key=score)
    return sum(b[1]*(a+1) for a,b in enumerate(L2))

if __name__ == '__main__':
    assert part()==251121738
    assert part(p2=True)==251421071

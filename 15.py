from puzzleinput import get
L = get(15).split(',')

def HASH(w):
    s = 0
    for c in w: s=(s+ord(c))*17%256
    return s

def part1():
    return sum(HASH(w) for w in L)

def part2():
    B = dict()
    for w in L:
        if '=' in w:
            h,n = w.split('=')
            b = HASH(h)
            if b not in B: B[b] = dict()
            B[b][h]=int(n)
        if '-' in w:
            h = w[:-1]
            b = HASH(h)
            if b in B: B[b].pop(h,0)
    return sum((k+1)*(i+1)*f for k,d in B.items() for i,f in enumerate(d.values()))

if __name__ == '__main__':
    assert part1()==504036
    assert part2()==295719

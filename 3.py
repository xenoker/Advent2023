from puzzleinput import getlines

L = getlines(3)
SYM = dict(((x,y),z) for y,l in enumerate(L) for x,z in enumerate(l) if z not in '1234567890.')
GEAR = dict((p,[]) for p,c in SYM.items() if c == '*')

def part1_2():
    S = 0
    for y,line in enumerate(L):
        N = []
        for x,c in enumerate(line+'.'):
            if c.isdigit(): N.append(x)
            elif N:
                b = set([(i,j) for i in range(N[0]-1,N[-1]+2) for j in [y-1,y,y+1]])
                if b & SYM.keys(): S += int(''.join(line[x] for x in N)) #P1
                for g in b & GEAR.keys(): GEAR[g].append(int(''.join(line[x] for x in N))) #P2
                N.clear()
    return S, sum(x[0]*x[1] for x in GEAR.values() if len(x)==2)

if __name__ == '__main__':
    assert part1_2() == (550934, 81997870)

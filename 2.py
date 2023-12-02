from puzzleinput import getlines
from functools import reduce

def getdata():
    L,D = getlines(2),dict()
    for l in L:
        gn,gall = l.split(': ')
        n = int(gn.split()[1])
        rnds = gall.split('; ')
        GL = []
        for rnd in rnds:
            G = dict()
            pairs = rnd.split(', ')
            for pair in pairs:
                cn,c = pair.split()
                G[c] = int(cn)
            GL.append(G)
        D[n]=GL
    return D

DATA = getdata()    
G = {'red':12,'green':13,'blue':14}

def part1():
    return sum(i for i,game in DATA.items() if all(all(n<=G[c] for c,n in rnd.items()) for rnd in game))

def part2():
    return sum(reduce(lambda a,b:a*b,[max(rnd.get(color,0) for rnd in game) for color in G.keys()]) for game in DATA.values())

if __name__ == '__main__':
    assert part1()==2162
    assert part2()==72513

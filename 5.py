from puzzleinput import get

class Alminac:
    def __init__(self):
        sect = get(5).split('\n\n')
        self.seeds = list(map(int,sect[0][6:].split()))
        self.MAPS = []
        for sec in sect:
            self.MAPS.append([])
            for line in sec.split('\n')[1:]:
                a,b,c = map(int,line.split())
                self.MAPS[-1].append(((b,b+c-1,a,a+c-1)))
    def reverse(self):
        self.MAPS = [[(c,d,a,b) for a,b,c,d in sec] for sec in reversed(self.MAPS)]
    def get(self, i):
        for m in self.MAPS:
            for a,b,c,d in m:
                if a<=i<=b:
                    i = c+i-a
                    break
        return i

A = Alminac()
seeds = A.seeds

def part1():
    return min(A.get(s) for s in seeds)

def part2():
    A.reverse()
    valid = [(seeds[x],seeds[x]+seeds[x+1]-1) for x in range(0,len(seeds),2)]
    for x in range(50000000):
        r = A.get(x)
        if any(a<=r<=b for a,b in valid): return x

if __name__ == '__main__':
    assert part1()==331445006
    assert part2()==6472060 #60 sec runtime

    

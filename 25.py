from puzzleinput import getlines
from collections import defaultdict

C = [l.replace(':','').split() for l in getlines(25)]
D = defaultdict(set)
for l in C:
    a = l[0]
    for b in l[1:]:
        D[a].add(b)
        D[b].add(a)

def part1():
    A,B = set(D.keys()),set()
    def links(p): return len(D[p]-A)
    while True:
        if sum(map(links,A)) == 3: return len(A)*len(B)
        v = max(A, key=links)
        A.remove(v)
        B.add(v)

if __name__ == '__main__':
    assert part1()==562978

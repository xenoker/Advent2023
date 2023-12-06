from puzzleinput import getlines
from functools import reduce

P1 = [tuple(map(int,l.split()[1:])) for l in getlines(6)]
P2 = [(int(''.join(map(str,x))),) for x in P1]

def part(TD):
    return reduce(lambda a,b:a*b,[sum((T-t)*t > D for t in range(1,T)) for T,D in zip(*TD)])

if __name__ == '__main__':
    assert part(P1)==393120
    assert part(P2)==36872656

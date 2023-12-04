from puzzleinput import getlines

L = [[list(map(int,y.split())) for y in x.split(':')[1].split(' | ')] for x in getlines(4)]

def score1(n): return n and 2**(n-1) or 0

def part1():
    return sum(score1(len([x for x in m if x in w])) for w,m in L)

def part2():
    S = [1]*len(L)
    for i,wm in enumerate(L):
        wins = len([x for x in wm[1] if x in wm[0]])
        for j in range(i+1,i+wins+1): S[j] += S[i]
    return sum(S)

if __name__ == '__main__':
    assert part1()==26443
    assert part2()==6284877

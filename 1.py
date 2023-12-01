from puzzleinput import getlines
L = getlines(1)

def part1():
    S = 0
    for line in L:
        A = [x for x in line if x.isdigit()]
        S += int(A[0]+A[-1])
    return S

REP = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
       'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

def part2():
    S = 0
    for line in L:
        F = []
        for a,b in REP.items():
            f = (line.find(a),b),(line.rfind(a),b),(line.find(b),b),(line.rfind(b),b)
            F.extend([x for x in f if x[0]!=-1])
        F.sort()
        S += int(F[0][1]+F[-1][1])
    return S

if __name__ == '__main__':
    assert part1()==53974
    assert part2()==52840


    


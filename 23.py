from puzzleinput import getlines
from collections import defaultdict, deque

class MazeGraph:
    def __init__(self):
        L = getlines(23)
        H,W = len(L), len(L[0])
        self.MAP = dict(((x,y),z) for y,l in enumerate(L) for x,z in enumerate(l) if z!='#')
        self.NODES = list(xy for xy in self.MAP if self.is_node(xy))
        self.START = (1,0)
        self.END = (W-2,H-1)
        self.dograph()

    def is_node(self, xy):
        x,y = xy
        if self.MAP.get(xy) == '.' and sum(self.MAP.get((x2,y2),' ') in '><v^' for x2,y2 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)])>1:
            return True
        return False      

    def search(self, xy):
        px,py = xy
        for d,dx,dy in [(0,1,0),(1,-1,0),(2,0,1),(3,0,-1)]:
            xy2 = (px+dx,py+dy)
            if xy2 not in self.MAP: continue
            t = self.MAP[xy]
            if t == '.' or t == '><v^'[d]: walk = True
            else: walk = False
            yield (xy2,walk)
     
    def dograph(self): 
        Q = deque([(0, self.START, self.START)])
        self.GRAPH = defaultdict(set)
        V = set()
        while Q:
            steps, root, node = Q.pop()
            V.add(node)
            if node == self.END:
                self.GRAPH[self.END].add((steps,root,True))
                self.GRAPH[root].add((steps,self.END,True))
                continue
            if node in self.NODES:
                root = node
                steps = 0
            for p2,walk in self.search(node):
                if p2 in self.NODES and p2 != root:
                    self.GRAPH[p2].add((steps+1,root,not walk))
                    self.GRAPH[root].add((steps+1,p2,walk))
                if p2 not in V:
                    Q.append((steps+1,root,p2))

    def longest(self, p2=False):
        S = 0
        Q = deque([(0, self.START, set())])
        while Q:
            steps,node,done = Q.pop()
            if node == self.END:
                S = max(S,steps)
                continue
            for dist,loc,walk in self.GRAPH[node]:
                if loc in done: continue
                if not p2 and not walk: continue
                Q.append((steps+dist,loc,done|{node}))
        return S

Graph = MazeGraph()
def part1(): return Graph.longest()
def part2(): return Graph.longest(p2=True)

if __name__ == '__main__':
    assert part1()==2438
    assert part2()==6658

"""
AStar Search
  https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/
  github.com/laurentluce/python-algorithms/blob/master/algorithms/a_star_path_finding.py
Bruce Wernick
10 October 2017 15:38:10
"""

from heapq import heapify, heappush, heappop


class SimpleSearch():
  def __init__(self, grid):
    self.grid=grid
    self.m=len(grid)-1
    self.n=len(grid[0])-1

  def addnode(self,a,i,j):
    if 0<=i<=self.m and 0<=j<=self.n:
      a.append((i,j))

  def adj(self,i,j):
    a=[]
    self.addnode(a, i+1, j)
    self.addnode(a, i+1, j-1)
    self.addnode(a, i,   j-1)
    self.addnode(a, i-1, j-1)
    self.addnode(a, i-1, j)
    self.addnode(a, i-1, j+1)
    self.addnode(a, i,   j+1)
    self.addnode(a, i+1, j+1)
    return a

  def process(self, x, y, path=[]):
    path = path + [(x,y)]
    if self.grid[x][y] == 2:
      return path
    elif self.grid[x][y] in [1,3]:
      return None
    self.grid[x][y] = 3 # visited
    for i,j in self.adj(x,y):
      newpath = self.process(i,j,path)
      if newpath:
        return newpath
    return None


# ---------------------
# A star implementation
# Node.__lt__ suggested by Jonathan Layman
# https://github.com/laurentluce/python-algorithms/issues/6
# ---------------------

class Node():
  def __init__(self, x, y, isfree):
    self.parent = None
    self.x, self.y = x, y
    self.g, self.h, self.f = 0, 0, 0
    self.isfree = isfree
  def __lt__(self, other):
    return self.f < other.f
  def __str__(self):
    return 'x:{}, y:{}, g={}, h={}, f={}, isfree={}'.format(self.x, self.y, self.g, self.h, self.f, self.isfree)

class AStar():
  def __init__(self):
    self.openlist = []
    heapify(self.openlist)
    self.closedset = set()
    self.nodes = []
    self.m, self.n = 0, 0

  def initgrid(self, grid, x0, y0):
    self.m = len(grid)
    self.n = len(grid[0])
    for x in range(self.m):
      for y in range(self.n):
        if grid[x][y] == 1:
          isfree = False
        else:
          isfree = True
        if grid[x][y] == 2:
          x2,y2 = x,y
        self.nodes.append(Node(x, y, isfree))
    self.start = self.getnode(x0, y0)
    self.end = self.getnode(x2, y2)

  def heuristic(self, node):
    return 10 * (abs(node.x - self.end.x) + abs(node.y - self.end.y))

  def getnode(self, x, y):
    return self.nodes[x * self.n + y]

  def addnode(self, a, x, y, g):
    if (0 <= x < self.m) and (0 <= y < self.n):
      nn = self.getnode(x,y)
      nn.g = g
      a.append(nn)

  def adj(self, node):
    x,y = node.x,node.y
    a=[]
    self.addnode(a, x+1, y, node.g+10)
    self.addnode(a, x+1, y-1, node.g+14)
    self.addnode(a, x,   y-1, node.g+10)
    self.addnode(a, x-1, y-1, node.g+14)
    self.addnode(a, x-1, y, node.g+10)
    self.addnode(a, x-1, y+1, node.g+14)
    self.addnode(a, x,   y+1, node.g+10)
    self.addnode(a, x+1, y+1, node.g+14)
    return a

  def getpath(self):
    path = []
    node = self.end
    path.append((node.x, node.y))
    while node.parent is not self.start:
      node = node.parent
      path.insert(0, (node.x, node.y))
    path.insert(0, (self.start.x, self.start.y))
    return path

  def updatenode(self, n, node):
    n.g = node.g + 10
    n.h = self.heuristic(n)
    n.parent = node
    n.f = n.h + n.g

  def process(self):
    heappush(self.openlist, (self.start.f, self.start))
    while len(self.openlist):
      f, node = heappop(self.openlist)
      self.closedset.add(node)
      if node is self.end:
        return self.getpath()
      nodes = self.adj(node)
      for n in nodes:
        if (n.isfree) and (n not in self.closedset):
          if (n.f, n) in self.openlist:
            if n.g > (node.g + 10):
              self.updatenode(n, node)
          else:
            self.updatenode(n, node)
            heappush(self.openlist, (n.f, n))

# ------------------------------------------------------------------------------

def find_pos(grid, ch):
  for r,row in enumerate(grid):
    for c,val in enumerate(row):
      if val == ch:
        return r,c
  return 0,0

if __name__ == '__main__':

  # start=7, target=2
  grid = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 7, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

  r,c = find_pos(grid, 7)

  search = SimpleSearch(grid)
  L = search.process(r,c)
  print('Simple search')
  print('length: {}'.format(len(L)))
  print(L)
  print()

  astar = AStar()
  astar.initgrid(grid,r,c)
  L = astar.process()
  print('A* search: ')
  print('length: {}'.format(len(L)))
  print(L)


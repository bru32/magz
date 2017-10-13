"""
AStar Search
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
# ---------------------

class Node():
  def __init__(self, x, y, free):
    self.parent = None
    self.x, self.y = x, y
    self.g, self.h, self.f = 0, 0, 0
    self.free = free

class AStar():
  def __init__(self):
    self.open = []
    heapify(self.open)
    self.closed = set()
    self.nodes = []
    self.m, self.n = 0, 0

  def initgrid(self, grid, x0, y0):
    self.m = len(grid)
    self.n = len(grid[0])
    for x in range(self.m):
      for y in range(self.n):
        if grid[x][y] == 1:
          free = False
        else:
          free = True
        if grid[x][y] == 2:
          x2,y2 = x,y
        self.nodes.append(Node(x, y, free))
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
    x,y=node.x,node.y
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
    #n.g = node.g + 10
    n.h = self.heuristic(n)
    n.parent = node
    n.f = n.h + n.g

  def process(self):
    heappush(self.open, (self.start.f, self.start))
    while len(self.open):
      f, node = heappop(self.open)
      self.closed.add(node)
      if node is self.end:
        return self.getpath()
      nodes = self.adj(node)
      for n in nodes:
        if n.free and n not in self.closed:
          if (n.f, n) in self.open:
            if n.g > node.g + 10:
              self.updatenode(n, node)
          else:
            self.updatenode(n, node)
            heappush(self.open, (n.f, n))


def find_start(grid):
  for r,row in enumerate(grid):
    for c,val in enumerate(row):
      if val == 7:
        return r,c
  return 0,0


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  # start at 7, target = 2
  grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
          [0, 1, 0, 0, 7, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


  r,c = find_start(grid)

  search = SimpleSearch(grid)
  print 'Simple search: ',
  print search.process(r,c)
  print

  astar = AStar()
  astar.initgrid(grid,r,c)
  print 'A* search: ',
  print astar.process()


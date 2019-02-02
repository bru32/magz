"""
Graph processing
using Brian Ling's edge triple (inlet,outlet,weight)
with reference to Guido van Russum essay "implementing graphs"
Bruce Wernick
10 October 2017 15:38:10
"""

def has_key(graph, n, c):
  'true if graph has an inlet or outlet node called n but not c'
  for e in graph:
    if c in [e[0],e[1]]: continue
    if n == e[0]: return True
    if n == e[1]: return True
  return False

def adjacent(graph, n):
  'return nodes adjacent to node n (in and out)'
  adj = []
  for e in graph:
    if n==e[0]: adj.append(e[1])
    if n==e[1]: adj.append(e[0])
  return adj

def find_path(graph, a, b, path=[], c=None):
  'from a to b, path starts empty, c is where we came from (for housekeeping)'
  path = path + [a] # we are at node a so add it to path
  if a == b: # reached the end so return the path
    return path
  # if a not an outlet to somewhere (but not where we came from)
  # then we have reaches a dead end
  if not has_key(graph, a, c):
    return None
  for n in adjacent(graph, a): # visit each node leading out of node a
    if n not in path: # if we have not already visited node n, then...
      # build a new path from n (but exclude node a, the one we came from)
      newpath = find_path(graph, n, b, path, a)
      if newpath: # if there is a newpath then return it
        return newpath
  return None

def mst(graph):
  'minimum spanning tree'
  tree=[]
  basic=[]
  graph.sort(key=lambda a: a[2])
  for e in graph:
    if not find_path(tree,e[0],e[1]):
      tree.append(e)
    else:
      basic.append(e)
  return tree,basic

def get_edge(graph, a, b):
  'return edge between a and b'
  for i in range(len(graph)):
    e=graph[i]
    if a==e[0] and b==e[1]: return (i,1.0)
    if a==e[1] and b==e[0]: return (i,-1.0)
  return (None,0)

def edge_list(graph, path):
  'return edge list from node path'
  edge=[]
  for i in range(1,len(path)):
    sgn,e=get_edge(graph, path[i-1], path[i])
    if e:
      edge.append((sgn,e))
  return edge


# ------------------------------------------------------------------------------

if __name__=='__main__':

  ## julie bridge
  graph = [[1, 2, 'a'],
           [1, 4, 'b'],
           [2, 3, 'c'],
           [4, 3, 'd'],
           [2, 5, 'e'],
           [3, 5, 'f'],
           [4, 5, 'g']]


  tree, basic = mst(graph)
  for b in basic:
    path = find_path(tree, b[1], b[0])
    mesh = edge_list(tree, path)
    print (mesh)
  print()



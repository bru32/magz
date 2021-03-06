"""
Graph theory.
Directly from Guido article
Python Patterns - Implementing Graphs
http://www.python.org/doc/essays/graphs/
Bruce Wernick 
10 June 2021
"""

def find_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  if start not in graph:
    return None
  for node in graph[start]:
    if node not in path:
      newpath = find_path(graph, node, end, path)
      if newpath: return newpath
  return None

def find_all_paths(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return [path]
  if start not in graph:
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths

def find_shortest_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  if start not in graph:
    return None
  shortest = None
  for node in graph[start]:
    if node not in path:
      newpath = find_shortest_path(graph, node, end, path)
      if newpath:
        if not shortest or len(newpath) < len(shortest):
          shortest = newpath
  return shortest


# ---------------------------------------------------------------------

if __name__=="__main__":

  ## sample graph
  graph = {'A': ['B', 'C'],
           'B': ['C', 'D'],
           'C': ['D'],
           'D': ['C'],
           'E': ['F'],
           'C': ['F']}

  print(find_path(graph, 'A', 'D'))
  #print(find_all_paths(graph, 'A', 'D'))
  #print(find_shortest_path(graph, 'A', 'D'))

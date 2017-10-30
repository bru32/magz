"""
I/O Utils
Bruce Wernick
10 October 2017 15:38:10
"""

import os


__all__ = ['name_only', 'path_to_list', 'get_minpath']


def name_only(path):
  "return file name only from the full path spec"
  name, ext = os.path.splitext(os.path.basename(path))
  return name

def path_to_list(path='.'):
  return os.path.normpath(os.path.realpath(path)).split(os.sep)

def get_minpath(fn, n=1, add_ext=False):
  """last n paths + name (with optional ext)
  """
  pathlist = splitall(fn) # split full path spec into parts
  namepart, extpart = os.path.splitext(pathlist[-1])
  if (n+1) > len(pathlist): # make sure there are enough folders in list
    res = fn
    if not add_ext:
      res, extpart = os.path.splitext(res)
    return res
  res = namepart # start with the namepart
  if add_ext: # add ext if needed
    res += extpart
  for i in range(2,n+2):
    res = os.path.join(pathlist[-i], res)
  return res


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  path = 'c:/code/python/bwlib/test.py'

  print 'name_only: ',  name_only(path)
  print 'path_to_list: ', path_to_list(path)
  print 'get_minpath: ', get_minpath(path)




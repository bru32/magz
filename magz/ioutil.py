"""
I/O Utils
Bruce Wernick
10 October 2017 15:38:10
"""

import os


__all__ = ['name_only']


def name_only(path):
  "return file name only from the full path spec"
  name, ext = os.path.splitext(os.path.basename(path))
  return name

def path_to_list(path='.'):
  return os.path.normpath(os.path.realpath(path)).split(os.sep)

def get_minpath(fn):
  parts = path_to_list(fn)
  namepart, extpart = os.path.splitext(parts[-1])
  return os.path.join(parts[-2], namepart+extpart)


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  path = 'c:/code/python/bwlib/test.py'

  print 'name_only: ',  name_only(path)
  print 'path_to_list: ', path_to_list(path)
  print 'get_minpath: ', get_minpath(path)




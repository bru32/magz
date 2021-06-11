"""
Dictionary Tools.
Bruce Wernick
10 June 2021
"""

import collections

__all__ = ['getfloat', 'update']

def getfloat(dict, key, default=0.0):
  "return floating point value from dictionary"
  value = dict.get(key, default)
  try:
    return float(value)
  except:
    return default

def update(d, u):
  "nested dictionary update"
  for k, v in list(u.items()):
    if isinstance(v, collections.Mapping):
      r = update(d.get(k, {}), v)
      d[k] = r
    else:
      d[k] = u[k]
  return d

class AttrDict(dict):
  def __init__(self, *args, **kwargs):
    super(AttrDict, self).__init__(*args, **kwargs)
    self.__dict__ = self


# ---------------------------------------------------------------------

if __name__ == '__main__':

  d = {'value': 123.456}
  print(getfloat(d, 'value'))

  update(d, {'editor':{'name':'Bruce', 'company':'TechniSolve'}, 'project':[1,2,3,4,5]})
  print(d)

  a = AttrDict(a=1, b=2, c=3)
  print(a)

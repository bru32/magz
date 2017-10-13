"""
String Utils
Bruce Wernick
10 October 2017 15:38:10
"""

import random
import string
from fuzzywuzzy import fuzz

__all__ = ['fuzzy', 'SameText', 'fsig']


def fuzzy(a, b):
  return fuzz.ratio(a, b)

def rand_str(n = 12):
  "return a random string of length n"
  chars = string.ascii_letters + string.digits
  return ''.join([random.choice(chars) for n in range(n)])

def SameText(a, b, strip=True):
  'case insensive compare'
  if a == b:
    return True
  if type(a) is 'str' and type(b) is 'str':
    a = a.lower()
    b = b.lower()
    if a == b:
      return True
    if strip and (a.strip() == b.strip()):
      return True
  return False


def fsig(x, f='0.6g'):
  "round float with significant digits"
  return float('{:{}}'.format(x,f))


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  print fsig(123.456, '0.3f')

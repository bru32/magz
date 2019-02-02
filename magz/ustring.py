"""
String Utils
Bruce Wernick
10 October 2017 15:38:10
"""

import random
import string

__all__ = ['SameText', 'fsig']


def rand_str(n=12, chars=string.ascii_letters+string.digits):
  "return a random string of length n"
  return ''.join([random.choice(chars) for n in range(n)])

def pword(size=12, chars=string.ascii_letters + string.digits):
  return ''.join(random.choice(chars) for i in range(size))

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

  print((fsig(123.456, '0.3f')))


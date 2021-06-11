"""
String Utils.
Bruce Wernick
10 June 2021
"""

import random
import string
from textdistance import hamming


__all__ = ['rand_str', 'pword', 'SameText', 'fsig']

def rand_str(n=12, chars=string.ascii_letters+string.digits):
  "return a random string of length n"
  return ''.join([random.choice(chars) for n in range(n)])

def pword(size=12, chars=string.ascii_letters + string.digits):
  return ''.join(random.choice(chars) for i in range(size))

def SameText(a, b, strip=True):
  'case insensive compare'

  if a == b:
    return True

  if type(a) == 'str' and type(b) == 'str':
    a = a.lower()
    b = b.lower()

    if a == b:
      return True

    if strip and (a.strip() == b.strip()):
      return True

    if a.casefold() == b.casefold():
      return True

  return False


def fsig(x, f='0.6g'):
  "round float with significant digits"
  return float('{:{}}'.format(x,f))


def TextMatch(str1, str2):
  """return True is there is a close match
  """

  # Exact match
  if str1 == str2:
    return True

  # Match Text (simple) ignore case
  if str1.lower() == str2.lower():
    return True

  # Use Python 3 casefold to (agressive) ignore case
  if str1.casefold() == str2.casefold():
    return True

  # compare the hamming distance to tolerate a close match
  if hamming(str1, str2) < 2:
    return True

  # no match found
  return False


# ---------------------------------------------------------------------

if __name__ == '__main__':

  print(fsig(123.456, '0.3f'))

  a = 'text_sample'
  b = 'text_simple'
  print(SameText(a, b))

  print(TextMatch(a, b))

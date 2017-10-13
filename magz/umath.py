"""
Math tools
Bruce Wernick
10 October 2017 15:38:10
"""

from __future__ import division
import math
import sys


__all__ = ['showvec', 'makemat', 'makevec', 'MAX', 'MIN', 'SIGN', 'SQR',
  'pythag', 'is_number', 'odd', 'sum_inv', 'is_close', 'max2', 'liststat',
  'ave']


# ------------------------------------------------------------------------------

# These functions are not necessary but are defined here
# to be compatible with Numerical Recipes.

def MAX(a, b):
  if b > a:
    return b
  else:
    return a

def MIN(a, b):
  if b < a:
    return b
  else:
    return a

def SIGN(a, b):
  "SIGN function defined in NR2"
  if b >= 0:
    if a >= 0:
      return a
    else:
      return -a
  else:
    if a >= 0:
      return -a
    else:
      return a

def SQR(a):
  b = a
  return b*b

# ------------------------------------------------------------------------------

def showvec(x, f='%0.6f'):
  "string format of vector"
  return '[' + ', '.join(map(lambda v: f % v, x)) + ']'

def makemat(m, n, value=1.0):
  "make 2D array"
  return [[value for j in range(n)] for i in range(m)]

def makevec(m, value=1.0):
  "make 1D array"
  return [value for i in range(m)]

def pythag(x, y):
  "hypot() return the Euclidean norm, sqrt(x*x + y*y)"
  x, y = abs(x), abs(y)
  if x < y:
    x, y = y, x
  if x == 0.:
    return 0.
  else:
    r = y/x
    return x * math.sqrt(1. + r*r)

def is_number(s):
  "True if string s is a number"
  try:
    float(s)
    return True
  except:
    return False

def odd(n):
  "return 1 if n is odd else 0"
  return n % 2

def sum_inv(a):
  "parallel resistance"
  return 1.0/sum(1.0/x for x in a)

def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
  if a == b: return True
  if math.isinf(a) or math.isinf(b): return False
  d = abs(b-a)
  return (((d<=abs(rel_tol*b))|(d<=abs(rel_tol*a)))|(d<=abs_tol))

def max2(L):
  "find 2nd highest in list L"
  n = 0
  m1 = m2 = float('-inf')
  for v in L:
    n += 1
    if v > m2:
      if v >= m1:
        m1, m2 = v, m1
      else:
        m2 = v
  return m2 if n >= 2 else None

def liststat(a):
  "high, low, high-low, high/low, total, average, median"
  t, n = 0.0, 0
  H = L = a[0]
  for v in a:
    t += v
    n += 1
    if v > H: H = v
    if v < L: L = v
  ave = t / n
  if L == 0:
    ratio = float('Inf')
  else:
    ratio = H / L
  return H, L, H-L, ratio, t, ave, a[n//2]

def ave(a):
  "average of list"
  return sum(a) / float(len(a))

# ------------------------------------------------------------------------------

def minfunc(f,*a):
  "return inner function"
  def inner_func(x):
    return f(x,*a)
  return inner_func

def maxfunc(f,*a):
  "return inner function"
  def inner_func(x):
    return 0.0-f(x,*a) # negative for max
  return inner_func

def golden(f, a, b, tol=1e-3):
  "golden section search for minimum"
  G = 0.5*(1.0 + math.sqrt(5.0))
  e = (b-a)/G
  c, d = b-e, a+e
  while abs(c-d) > tol:
    if f(c) < f(d):
      b = d
    else:
      a = c
    e = (b - a)/G
    c, d = b-e, a+e
  return 0.5*(a+b)

# ------------------------------------------------------------------------------

if __name__ == '__main__':

  print max2([3,5,7,8,17,12])

  from utils import linrange
  f = lambda x: (x-2)*(x+3)
  x = golden(f, -10, 10)
  print 'f({}) = {}'.format(x, f(x))
  for x in linrange(-10, 10, 10):
    print 'f({}) = {}'.format(x, f(x))



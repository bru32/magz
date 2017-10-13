"""
Root find tools
Bruce Wernick
10 October 2017 15:38:10
"""

from __future__ import division
import sys
import math

__all__ = ['newt']


TINY = 1e-20
EPS = sys.float_info.epsilon


def newt(f, x, maxi=24, tol=1e-6):
  "Newton-Raphson root find method"
  for i in range(maxi):
    x0 = x
    fx, dfx = f(x) # f(x) and slope
    if abs(fx) <= tol:
      return x,i,0,'fx within tol'
    if abs(dfx) <= TINY:
      return x,i,1,'func too flat'
    x -= fx / dfx
    if abs(x-x0) <= tol:
      return x,i,0,'dx within tol'
  return x,i,2,'max its reached'


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  def func():
    def f(x):
      return (x-2)*(x+3), 2*x+1
    return f
  f = func()
  print newt(f, 7.2)


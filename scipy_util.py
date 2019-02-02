"""
scipy utils
Bruce Wernick
11 October 2017 16:26:20
"""


import numpy as np
import scipy.optimize as sci
import warnings

all = ['fsolve']


def fsolve(f, x0=1.0, args=None):
  "scipy.optimize.fsolve shell"
  [x] = sci.fsolve(f, x0=x0, args=args)
  return x


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  def f(x,a,b,c):
    "find the intersection of two curves"
    curve1 = (x-b)*(x+c)
    curve2 = x-a
    return curve1 - curve2

  a,b,c=1.234,2.345,3.456
  x = fsolve(f, 1.0, args=(a,b,c))
  print(('x={:0.4f} f(x)={:0.6f}'.format(x, f(x,a,b,c))))



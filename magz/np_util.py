"""
Numpy Utils.
Bruce Wernick
10 June 2021
"""

import numpy as np

__all__ = ['polyfit']

def polyfit(x, y, deg):
  "polynomial curvefit using numpy"
  c = np.polyfit(x, y, deg)
  f = np.poly1d(c)
  yh = f(x)
  r2 = np.corrcoef(y, yh)[0,1]**2
  return c, r2


# ---------------------------------------------------------------------

if __name__ == '__main__':

  from random import random
  c = [1.0, 2.0, 3.0, 4.0] # arbirary coefficients
  f = np.poly1d(c) # create a polynomial generator
  x = [float(xi) for xi in range(-5,6,1)] # x-range
  y = [f(xi)+1.2*random() for xi in x] # use f(x)+mu to create y-data
  c,r2 = polyfit(x, y, 3) # do polynomial curve-fit
  print('coeff={}, r2={:0.6f}'.format(c, r2))
  print()
  g = np.poly1d(c)
  yc = g(x)
  for xi,yi,yci in zip(x,y,yc):
    print('{:6.2f} {:6.2f} {:6.2f} {:8.3f}'.format(xi, yi, yci, yci-yi))

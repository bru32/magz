"""
2D Root Finder.
Function f(x,y) must return tuple of 2 error.
Bruce Wernick
10 June 2021
"""

import sys
from const import EPS, TINY

class RootFinder(object):

  maxi = 96
  tol = 1e-6

  def __init__(self, f):
    self.f = f
    self.its = 0

  def djac(self, x, y):
    'jacobian'
    h = 3.44e-4
    xo, yo = x, y
    dx, dy = h*abs(x), h*abs(y)
    if dx == 0.0:
      dx = h
    if dy == 0.0:
      dy = h
    x += dx; y += dy
    fxy, gxy = self.f(xo, yo)
    dx, dy = x-xo, y-yo
    fxyo, gxyo = self.f(x, yo)
    fxoy, gxoy = self.f(xo, y)
    J = (fxyo-fxy)/dx, (fxoy-fxy)/dy, (gxyo-gxy)/dx, (gxoy-gxy)/dy
    D = J[0]*J[3] - J[2]*J[1]
    return fxy, gxy, J, D

class Broyden(RootFinder):

  def __call__(self, xy):
    '2D root by Broyden method'
    x,y = xy
    self.its = 0
    fxy, gxy, J, D = self.djac(x,y)
    if abs(D) < EPS:
      raise ValueError('too flat!')
    B = [J[3]/D, -J[1]/D, -J[2]/D, J[0]/D]
    dx = -(B[0]*fxy+B[1]*gxy); dy = -(B[2]*fxy+B[3]*gxy)
    x += dx; y += dy
    f0, g0 = fxy, gxy
    fxy, gxy = self.f(x, y)
    df, dg = fxy-f0, gxy-g0
    for self.its in range(RootFinder.maxi):
      BdF = B[0]*df+B[1]*dg, B[2]*df+B[3]*dg
      e = dx*BdF[0] + dy*BdF[1]
      if abs(e) < EPS:
        return x,y
      u = dx-BdF[0], dy-BdF[1]
      v = B[0]*dx+B[2]*dy, B[1]*dx+B[3]*dy
      B[0]+=u[0]*v[0]/e; B[1]+=u[0]*v[1]/e; B[2]+=u[1]*v[0]/e; B[3]+=u[1]*v[1]/e
      dx=-(B[0]*fxy+B[1]*gxy); dy=-(B[2]*fxy+B[3]*gxy)
      x += dx; y += dy
      if abs(dx) <= RootFinder.tol and abs(dy) <= RootFinder.tol:
        return x,y
      f0,g0 = fxy,gxy
      fxy,gxy = self.f(x,y)
      df,dg = fxy - f0, gxy - g0
    raise ValueError('max iterations reached!')

class Newton(RootFinder):

  def __call__(self, xy):
    '2D root by Newton method'
    x,y = xy
    self.its = 0
    for self.its in range(RootFinder.maxi):
      fxy,gxy,J,G = self.djac(x,y)
      if abs(G) < EPS:
        raise ValueError('too flat!')
      dx = (gxy*J[1] - fxy*J[3])/G
      dy = (fxy*J[2] - gxy*J[0])/G
      x+=dx; y+=dy
      if abs(dx) < RootFinder.tol and abs(dy) < RootFinder.tol:
        return x,y
    raise ValueError('max iterations reached!')


# ---------------------------------------------------------------------

if __name__=='__main__':

  # Example 1, trivial 2D function
  fxy = lambda x,y:(x-2.0, y-7.0)
  root = Broyden(fxy)
  x = (1.0,1.0)
  z = root(x)
  print(f'roots = {z}')

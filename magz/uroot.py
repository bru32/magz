"""
1D RootFind class
Bruce Wernick
29 October 2017 4:46:20
"""

import sys

EPS = sys.float_info.epsilon
TINY = 2*EPS

import sys
from math import sqrt, log10

def MIN(a, b):
  if a < b:
    return a
  return b

def SQR(x):
  t = x;
  return t*t

def SIGN(a, b):
  if b >= 0.0:
    return abs(a)
  return -abs(a)

def signum(a, b):
  'signed number'
  if b < 0.0:
    return -abs(a)
  return abs(a)


class RootFind(object):
  """Abstract 1D root finder class.
  This is the base class that the actual solve methods must inherit from.
  """
  tol = 1e-6
  maxi = 128

  def __init__(self, f):
    'RootFind class constructor'
    self.f = f
    self.its = 0
    self.kind = type(self).__name__

  def dxdy(self, x):
    'f(x) and slope inverse dx/df'
    e = 0.1
    xo = x; fo = self.f(xo)
    h = e * abs(xo)
    if h <= TINY: h = e
    x = xo + h; fx = self.f(x)
    return fo, (x-xo)/(fx-fo)

  def dydx(self, x):
    'f(x) and df/dx (inverse slope)'
    e = 0.1
    xo = x; fo = self.f(xo)
    h = e * abs(xo)
    if h <= TINY: h = e
    x = xo + h; fx = self.f(x)
    return fo, (fx-fo)/(x-xo)

  def dydx2(self, x):
    'f(x), df/dx and d2f/dx2 (2nd derivative)'
    e = 0.01
    h = e * abs(x)
    if h <= TINY: h = e
    fo, df = self.dydx(x)
    df2 = (self.f(x+h) - 2.0*fo + self.f(x-h)) / h / h
    return fo, df, df2

  def __call__(self, *args):
    raise NotImplementedError('abstract root finder called!')


class Newton(RootFind):

  """Newton-Raphson method (pure slope method).
  Function must return f(x) and slope.
  """

  def __call__(self, x):
    for self.its in range(RootFind.maxi):
      x0 = x
      y, dydx = self.f(x)
      if abs(dydx) <= EPS:
        raise ValueError('curve too flat for Newton method!')
      dx = y / dydx
      x -= dx
      if (abs(dx) <= RootFind.tol) or (abs(x-x0) <= RootFind.tol):
        return x
    raise ValueError('max iterations reached!')


class rtSafe(RootFind):

  """Newton with safe bisection.
  Should have the benefit of Newton with the safety of Bisection.
  """

  def __call__(self, x1, x2):
    fl = self.f(x1)
    fh = self.f(x2)
    if fl*fh>0:
      raise ValueError('Root must be bracketed in rtsafe')

    if abs(fl) <= RootFind.tol:
      return x1

    if abs(fh) <= RootFind.tol:
      return x2

    if fl < 0.0:
      xl = x1; xh = x2
    else:
      xh = x1; xl = x2

    x = 0.5*(x1+x2)
    dx0 = abs(x2-x1)
    dx = dx0
    fx, df = self.dydx(x)

    for self.its in range(RootFind.maxi):

      if ((((x-xh)*df-fx)*((x-xl)*df-fx) > 0.0) or (abs(2.0*fx) > abs(dx0*df))):
        "bisection step"
        dx0 = dx
        dx = 0.5*(xh-xl)
        x = xl + dx
        if xl == x:
          return x
      else:
        "newton step"
        dx0 = dx
        dx = fx / df
        t = x
        x -= dx
      if abs(t-x) <= RootFind.tol:
        return x

      if abs(dx) < RootFind.tol:
        return x

      fx, df = self.dydx(x)
      if fx < 0.0:
        xl = x
      else:
        xh = x

    raise ValueError('max iterations reached!')


class Secant(RootFind):

  """Secant method.
  """

  def __call__(self, a, b):
    fa, fb = self.f(a), self.f(b)
    if abs(fa) > abs(fb):
      a, b = b, a
      fa, fb = fb, fa
    for self.its in range(RootFind.maxi):
      dx = fa*(a-b)/(fa-fb)
      if abs(dx) < RootFind.tol*(1+abs(a)):
        return a-dx
      b, a = a, a-dx
      fb, fa = fa, self.f(a)
    raise ValueError('max iterations reached!')


class Bisect(RootFind):

  """Bisection method.
  Numerical Recipes version.
  """

  def __call__(self, x1, x2):
    f1, f2 = self.f(x1), self.f(x2)
    if f1 * f2 >= 0.0:
      raise ValueError('root must be bracketed!')
    if f1 < 0.0:
      dx = x2-x1
      x = x1
    else:
      dx = x1-x2
      x = x2
    for self.its in range(RootFind.maxi):
      dx *= 0.5
      if abs(dx) < RootFind.tol:
        return x
      x2 = x + dx
      f2 = self.f(x2)
      if abs(f2) <= EPS:
        return x2
      if f2 <= 0.0:
        x = x2
    raise ValueError('max iterations reached!')


class Ridder(RootFind):

  """Ridder's method
  """

  def __call__(self, x1, x2):
    fl, fh = self.f(x1), self.f(x2)
    if fl*fh >= 0.0:
      raise ValueError('root must be bracketed!')
    xl, xh = x1, x2
    x = -1.11e30
    for self.its in range(RootFind.maxi):
      xm = 0.5*(xl + xh)
      fm = self.f(xm)
      s = sqrt(fm*fm - fl*fh)
      if s == 0.0:
        return xm
      if fl >= fh:
        xnew = xm + (xm-xl)*fm/s
      else:
        xnew = xm + (xl-xm)*fm/s
      if (abs(xnew-x) <= RootFind.tol):
        return xnew
      x = xnew
      fx = self.f(x)
      if fx == 0.0:
        return x
      if SIGN(fm,fx) != fm:
        xl = xm; fl = fm; xh = x; fh = fx
      elif (SIGN(fl,fx) != fl):
        xh, fh = x, fx
      elif SIGN(fh,fx) != fh:
        xl, fl = x, fx
      else:
        raise ValueError('undefined error!')
      if abs(xh-xl) <= RootFind.tol:
        return x
    raise ValueError('max iterations reached!')


class Brent(RootFind):

  """Brent's inverse quadratic method.
  This is supposed to be the most reliable method (although, not always the
  fastest). It is the one recommended by Numerical Recipes.
  """

  def __call__(self, a, b):
    fa, fb = self.f(a), self.f(b)
    if fa*fb >= 0.0:
      raise ValueError('root must be bracketed!')
    c,fc = b,fb
    for self.its in range(RootFind.maxi):
      if (fb > 0.0 and fc > 0.0) or (fb < 0.0 and fc < 0.0):
        c, fc = a, fa
        e = d = b-a
      if abs(fc) < abs(fb):
        a = b; b = c; c = a
        fa = fb; fb = fc; fc = fa
      tol1 = 2.0*EPS*abs(b) + 0.5*RootFind.tol
      xm = 0.5*(c-b)
      if abs(xm) <= tol1 or fb == 0.0:
        return b
      if (abs(e) >= tol1 and abs(fa) > abs(fb)):
        s = fb/fa
        if a == c:
          p = 2.0*xm*s
          q = 1.0 - s
        else:
          q = fa/fc
          r = fb/fc
          p = s*(2.0*xm*q*(q-r) - (b-a)*(r-1.0))
          q = (q-1.0)*(r-1.0)*(s-1.0)
        if (p > 0.0):
          q = -q
        p = abs(p)
        min1 = 3.0*xm*q - abs(tol1*q)
        min2 = abs(e*q)
        if (2.0*p < MIN(min1, min2)):
          e = d; d = p/q
        else:
          d = xm; e = d
      else:
        d = xm; e = d
      a, fa = b, fb
      if abs(d) > tol1:
        b += d
      else:
        b += SIGN(tol1, xm)
      fb = self.f(b)
    raise ValueError('max iterations reached!')


class Brent2(RootFind):

  """Brent's inverse quadratic method,
  by Kiusalaas, faster than NR and Wikipedia algorithm.
  """

  def __call__(self, x1, x2):
    f1 = self.f(x1)
    if f1 == 0: return x1
    f2 = self.f(x2)
    if f2 == 0: return x2
    if f1*f2 > 0:
      raise ValueError('root must be bracketed!')
    if x1 > x2:
      x1,x2 = x2,x1
      f1,f2 = f2,f1
    x3 = 0.5*(x1+x2)
    for i in range(RootFind.maxi):
      f3 = self.f(x3)
      if abs(f3) < RootFind.tol: return x3
      if f1*f3 < 0: b = x3
      else: a = x3
      if (x2-x1) < RootFind.tol*max(abs(x2),1): return 0.5*(x1+x2)
      P = x3*(f1-f2)*(f2-f3+f1) + f2*x1*(f2-f3) + f1*x2*(f3-f1)
      Q = (f2-f1)*(f3-f1)*(f2-f3)
      if abs(Q) <= TINY: dx = b-a
      else: dx = f3*P/Q
      x = x3 + dx
      if (x2-x)*(x-x1) < 0:
        dx = 0.5*(x2-x1)
        x = a+dx
      if x < x3: x2,f2 = x3,f3
      else: x1,f1 = x3,f3
      x3 = x
    raise ValueError('max iterations reached!')


class Broyden(RootFind):

  """1D Broyden method ().
  1D coded from Broydens multi-dimensional method. Actually, it's a secant
  method but with slope update. The big advantage is that it only needs 1
  starting guess and has 1 function call per loop. The slope inverse is
  calculated once at the start and simply corrected at each step. I'm surprised
  that it hasn't been used elsewhere because it seems to be fairly rugged and
  performs well in every case.
  """

  def __call__(self, x):
    fo, K = self.dxdy(x)
    if abs(fo) <= RootFind.tol:
      return x
    for self.its in range(RootFind.maxi):
      dx = -K*fo
      x += dx
      fx = self.f(x)
      if abs(fx) <= RootFind.tol:
        return x
      dfx = fx - fo
      if abs(dfx) <= TINY:
        return x
      a = dx*K*dfx
      dK = -K*(a-dx*dx)/a
      K += dK
      fo = fx
    raise ValueError('max iterations reached!')


class Halley(RootFind):

  """Halley method,
  uses 2nd derivative.
  This is supposed to have a higher convergence rate than Newton but the cost
  of the 2nd deriv seems to reduce its value.
  """

  def __call__(self, x):
    for self.its in range(RootFind.maxi):
      fx, f1, f2 = self.dydx2(x)
      d = 2*f1*f1 - fx*f2
      if abs(d) <= EPS:
        return x
      dx = (2*fx*f1) / d
      x -= dx
      if abs(dx) <= RootFind.tol:
        return x
    raise ValueError('max iterations reached!')


class Schroeder(RootFind):

  """Schroeders method, uses 2nd derivative
  """

  def __call__(self, x):
    for self.its in range(RootFind.maxi):
      fx, f1, f2 = self.dydx2(x)
      dxn = fx/f1 # newton correction
      dx = dxn*(1.0 + 0.5*dxn*f2/f1)
      x -= dx
      if abs(dx) <= RootFind.tol:
        return x
    raise ValueError('max iterations reached!')


class Illinois(RootFind):

  """Illionois method - modified secant
  This is a good choice if Broyden doesnt work.
  """

  def __call__(self, x1, x2):
    f1, f2 = self.f(x1), self.f(x2)
    for self.its in range(RootFind.maxi):
      x3 = x2 - f2*(x1-x2)/(f1-f2)
      f3 = self.f(x3)
      if f2*f3 < 0: # x2 and x3 straddle root
        x1, f1 = x2, f2
        if abs(f2) <= RootFind.tol:
          return x2
      else:
        f1 = 0.5*f1 # reduce slope
      x2, f2 = x3, f3
      if abs(f2) <= RootFind.tol:
        return x2
    raise ValueError('max iterations reached!')


class Pegasus(RootFind):

  """Pegasus method - variant of Illinois
  """

  def __call__(self, x1, x2):
    x = 0.5*(x1+x2)
    f1, f2 = self.f(x1), self.f(x2)
    if f1*f2 >= 0.0:
      raise ValueError('root must be bracketed!')
    for self.its in range(RootFind.maxi):
      dx = x2-x1
      dy = f2-f1
      if abs(dy) <= EPS:
        return x
      x3 = x1 - f1*dx/dy
      f3 = self.f(x3)
      x = x3
      if abs(f3) < RootFind.tol:
        return x
      if f2 * f3 <= 0:
        x1, f1 = x2, f2
      else:
        m = f2/(f2+f3)
        f1 = m * f1
      x2, f2 = x3, f3
    raise ValueError('max iterations reached!')


class Anderson(RootFind):

  """Anderson's method - variant of Illinois
  """

  def __call__(self, x1, x2):
    x = 0.5*(x1+x2)
    f1, f2 = self.f(x1), self.f(x2)
    if f1*f2 >= 0.0:
      raise ValueError('root must be bracketed!')
    for self.its in range(RootFind.maxi):
      dx = x2-x1
      dy = f2-f1
      if abs(dy) <= EPS:
        return x
      x3 = x1 - f1*dx/dy
      f3 = self.f(x3)
      x = x3
      if abs(f3) < RootFind.tol:
        return x
      if f2*f3 <= 0:
        x1, f1 = x2, f2
      else:
        m = 1.0 - f3/f2
        if m <= 0:
          m = 0.5
        f1 = m*f1
      x2, f2 = x3, f3
    raise ValueError('max iterations reached!')


class RegulaFalsi(RootFind):

  """standard regula-falsi method.
  Included here for completeness but I wouldn't bother using this one.
  """

  def __call__(self, a, b):
    fa, fb = self.f(a), self.f(b)
    if fa*fb > 0:
      raise ValueError('root must be bracketed!')
    k = 0
    for self.its in range(RootFind.maxi):
      df = fa - fb
      if df <= EPS:
        raise ValueError('too flat!')
      c = (fa*b - fb*a) / df
      if (abs(b-a) < RootFind.tol*abs(b+a)):
        return c
      fc = self.f(c)
      if fc*fb > 0:
        b, fb = c, fc
        if k == -1: fa*=0.5
        k = -1
      elif fa*fc > 0:
        a, fa = c, fc
        if k == 1: fb*=0.5
        k = 1
      else:
        return c
    raise ValueError('max iterations reached!')


class ModRegulaFalsi(RootFind):

  """Modified Regula-Falsi - False Position method
  Better but still not great.
  """

  def __call__(self, a, b):
    fa, fb = self.f(a), self.f(b)
    if fa*fb >= 0.0:
      raise Exception('root must be bracketed!')
    if fb < 0.0:
      a,b = b,a
      fa,fb = fb,fa
    c = a
    fc = fa
    for self.its in range(RootFind.maxi):
      c = (b*fa - a*fb)/(fa - fb)
      fco = fc
      fc = self.f(c)
      if fc > 0.0:
        a = c; fa = fc
        if fc*fco > 0.0:
          fb = 0.5*fb
      else:
        b = c; fb = fc
        if fc*fco > 0.0:
          fa = 0.5*fa
      if abs(fc) < RootFind.tol:
        return c
    raise ValueError('max iterations reached!')


class Trisect(RootFind):

  """Divide range into 3 segments.
  Find the range [a,c1], [c1,c2], [c2,b] where the root exists and call it
  recursively.
  This is just an experiment to see if I could improve on Bisection.
  """

  def __init__(self, f):
    super(Trisect, self).__init__(f)
    RootFind.its = 0

  def __call__(self, a, b):
    if a > b: a,b = b,a

    d = (b-a)/3
    if d <= RootFind.tol:
      return a+d

    fa = self.f(a)
    if abs(fa) < RootFind.tol:
      return a

    fb = self.f(b)
    if abs(fb) < RootFind.tol:
      return b

    if fa*fb > 0:
      raise ValueError("root must be bracketed")

    RootFind.its += 1
    if RootFind.its > RootFind.maxi:
      raise ValueError('maxits reached!')

    # 1st tri-step
    c1 = a+d
    fc1 = self.f(c1)
    if fa*fc1 < 0:
      return self.__call__(a,c1)

    # 2nd tri-step
    c2 = b-d
    fc2 = self.f(c2)
    if fc1*fc2 < 0:
      return self.__call__(c1,c2)

    # 3rd tri-step
    return self.__call__(c2,b)


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  def func(a,b):
    def f(x):
      y = (x+a)*(x+b)
      dydx = a+b+2*x
      return y, dydx
    return f

  fx = func(-2, 3)
  root = Newton(fx)
  y = root(7)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  fx = lambda x: (x-2)*(x+3)

  root = rtSafe(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Secant(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Bisect(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Ridder(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Brent(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Brent2(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))


  root = Broyden(fx)
  y = root(7)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Halley(fx)
  y = root(7)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Schroeder(fx)
  y = root(7)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Illinois(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Pegasus(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Anderson(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = RegulaFalsi(fx)
  y = root(15,0.1)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = ModRegulaFalsi(fx)
  y = root(3,0.5)
  print(('{} root={:0.6g}'.format(root.kind, y)))

  root = Trisect(fx)
  y = root(3,0.5)
  print(('{} root={:0.6g}'.format(root.kind, y)))



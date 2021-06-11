"""
Singular Valued Decomposition.
  - based on Numerical Recipes 2nd ed.
Bruce Wernick
10 June 2021
"""

from math import sqrt
from umath import showvec, makemat, makevec, MAX, MIN, SIGN, SQR, pythag
from regress import cod

__all__ = ['SVDsolve', 'polyfit', 'MLRfit', 'poly2Dfit', 'polyARIfit']

def svdcmp(a, w, v):
  "SVD: Singular Valued Decomposition"
  m = len(a)
  n = len(a[0])
  anorm = c = f = g = h = s = scale = x = y = z = 0.0
  i = its = j = jj = k = l = nm = 0
  flag = 0
  rv1 = list(range(n))
  for i in range(0, n):
    l = i + 2
    rv1[i] = scale*g
    g = s = scale = 0.0
    if i < m:
      for k in range(i, m):
        scale += abs(a[k][i])
      if scale != 0.0:
        for k in range(i, m):
          a[k][i] = a[k][i] / scale
          s += a[k][i]*a[k][i]
        f = a[i][i]
        g = -SIGN(sqrt(s), f)
        h = f*g - s
        a[i][i] = f - g
        for j in range(l-1, n):
          s = 0.0
          for k in range(i, m):
            s += a[k][i]*a[k][j]
          f = s / h
          for k in range(i,m):
            a[k][j] += f*a[k][i]
        for k in range(i,m):
          a[k][i] = a[k][i]*scale
    w[i] = scale*g
    g = s = scale = 0.0
    if i+1 <= m and i != n:
      for k in range(l-1, n):
        scale += abs(a[i][k])
      if scale != 0.0:
        for k in range(l-1, n):
          a[i][k] = a[i][k] / scale
          s += a[i][k]*a[i][k]
        f = a[i][l-1]
        g = -SIGN(sqrt(s), f)
        h = f*g - s
        a[i][l-1] = f - g
        for k in range(l-1, n):
          rv1[k] = a[i][k] / h
        for j in range(l-1, m):
          s = 0.0
          for k in range(l-1, n):
            s += a[j][k]*a[i][k]
          for k in range(l-1, n):
            a[j][k] += s*rv1[k]
        for k in range(l-1, n):
          a[i][k] = a[i][k]*scale
    anorm = MAX(anorm, (abs(w[i]) + abs(rv1[i])))
  i = n-1
  while i >= 0:
    if i < n-1:
      if g != 0.0:
        for j in range(l,n):
          v[j][i] = (a[i][j]/a[i][l])/g
        for j in range(l, n):
          s = 0.0
          for k in range(l, n):
            s += a[i][k]*v[k][j]
          for k in range(l, n):
            v[k][j] += s*v[k][i]
      for j in range(l, n):
        v[i][j] = 0.0
        v[j][i] = 0.0
    v[i][i] = 1.0
    g = rv1[i]
    l = i
    i = i-1
  i = MIN(m,n)-1
  while i >= 0:
    l = i+1
    g = w[i]
    for j in range(l, n):
      a[i][j] = 0.0
    if g != 0.0:
      g = 1.0 / g
      for j in range(l, n):
        s = 0.0
        for k in range(l, m):
          s += a[k][i]*a[k][j]
        f = (s / a[i][i])*g
        for k in range(i, m):
          a[k][j] += f*a[k][i]
      for j in range(i,m):
        a[j][i] = a[j][i]*g
    else:
      for j in range(i, m):
        a[j][i] = 0.0
    a[i][i] = a[i][i] + 1.0
    i = i-1
  k = n-1
  while k >= 0:
    for its in range(0, 30):
      flag = 1
      l = k
      while l >= 0:
        nm = l-1
        if abs(rv1[l])+anorm == anorm:
          flag = 0
          break
        if abs(w[nm])+anorm == anorm:
          break
        l = l - 1
      if flag:
        c = 0.0
        s = 1.0
        for i in range(l-1, k+1):
          f = s*rv1[i]
          rv1[i] = c*rv1[i]
          if abs(f)+anorm == anorm:
            break
          g = w[i]
          h = pythag(f, g)
          w[i] = h
          h = 1.0 / h
          c = g*h
          s = -f*h
          for j in range(0, m):
            y = a[j][nm]
            z = a[j][i]
            a[j][nm] = y*c + z*s
            a[j][i] = z*c - y*s
      z = w[k]

      if l == k:
        if z < 0.0:
          w[k] = -z
          for j in range(0, n):
            v[j][k] = -v[j][k]
        break

      if its == 29:
        raise ValueError('no convergence in 29 svdcmp iterations')

      x = w[l]
      nm = k-1
      y = w[nm]
      g = rv1[nm]
      h = rv1[k]
      f = ((y-z)*(y+z)+(g-h)*(g+h))/(2.0*h*y)
      g = pythag(f,1.0)
      f = ((x-z)*(x+z)+h*((y/(f+SIGN(g,f)))-h))/x
      c = s = 1.0
      for j in range(l, nm+1):
        i = j+1
        g = rv1[i]
        y = w[i]
        h = s*g
        g = c*g
        z = pythag(f,h)
        rv1[j] = z
        c = f/z
        s = h/z
        f = x*c+g*s
        g = g*c-x*s
        h = y*s
        y = y*c
        for jj in range(0, n):
          x = v[jj][j]
          z = v[jj][i]
          v[jj][j] = x*c + z*s
          v[jj][i] = z*c - x*s
        z = pythag(f,h)
        w[j] = z
        if z:
          z = 1.0 / z
          c = f*z
          s = h*z
        f = c*g + s*y
        x = c*y - s*g
        for jj in range(0, m):
          y = a[jj][j]
          z = a[jj][i]
          a[jj][j] = y*c + z*s
          a[jj][i] = z*c - y*s
      rv1[l] = 0.0
      rv1[k] = f
      w[k] = x
    k = k-1

def svbksb(u,w,v,b):
  "back substitution"
  m, n = len(u), len(u[0])
  x, tmp = list(range(n)), list(range(n))
  for j in range(0,n):
    s = 0.0
    if w[j] != 0.0:
      for i in range(0,m):
        s += u[i][j]*b[i]
      s = s/w[j]
    tmp[j] = s
  for j in range(0, n):
    s = 0.0
    for jj in range(0, n):
      s += v[j][jj]*tmp[jj]
      x[j] = s
  return x

def SVDsolve(a,b):
  "solve set of linear equations by singular valued decomposition"
  m, n = len(a), len(a[0])
  u = [[a[i][j] for j in range(n)] for i in range(m)]
  v = [[0.0 for j in range(n)] for i in range(m)]
  w = list(range(n))
  svdcmp(u, w, v)
  wmax = 0.0
  for j in range(0, n):
    if w[j] > wmax:
      wmax = w[j]
  wmin = wmax*1.0e-12
  for j in range(0, n):
    if w[j] < wmin:
      w[j] = 0.0
  x = svbksb(u, w, v, b)
  return x


# ---------------------------------------------------------------------

# --------------------------
# Solve 1D polynomial by SVD
# --------------------------

def polyh(c, x):
  """
  polynomial eval using Horner method (high order)
  Warning: the coefficients are ordered from high powers down to the const.
  """
  n = len(c)
  p = 0.0
  for i in range(0, n-1):
    p = (p + c[i])*x
  p += c[n-1]
  return p

def polyfit(x, y, p):
  """
  Fit polynomial by SVD.
  c[0]x**p + c[1]x**{p-1} + ... + c[p]
  p = len(c)-1
  """
  n = len(x)

  if ((n < p+1) or (n != len(y))):
    raise ValueError("Dimension error in polyfit")

  a = makemat(n, p+1, 1.0)

  # set up columns for a polynomial of order p.
  # actually, MLR with each of the poly terms.
  for i in range(n):
    for j in range(p+1):
      a[i][j] = pow(x[i], 1.0*(p-j))

  w = SVDsolve(a, y)
  yc = [polyh(w, xi) for xi in x]
  R2 = cod(y, yc)
  R2a = 1.0-(1.0-R2)*(n-1.0)/(n-p)
  return w, R2a

# ---------------------------------------------------------------------

# ---------------------------------------
# 2D polynomial curvefit by SVD
# const, x, x2, y, y2, xy, x2y, xy2, x2y2
# ---------------------------------------

def poly2d(c,x,y):
  return c[0]+x*(c[1]+x*c[2])+y*(c[3]+y*c[4])+x*y*(c[5]+x*c[6]+y*c[7]+x*y*c[8])

def MLRfit(x, y, z):
  "poly2d fit"
  p = 8
  n = len(z)
  a = makemat(n, p+1, 0.0)
  m = len(y)
  for i in range(len(x)):
    for j in range(m):
      k = j + i*m
      a[k][0] = 1.0              # const
      a[k][1] = x[i]             # x
      a[k][2] = x[i]*x[i]        # x2
      a[k][3] = y[j]             # y
      a[k][4] = y[j]*y[j]        # y2
      a[k][5] = x[i]*y[j]        # xy
      a[k][6] = a[k][2]*y[j]     # x2y
      a[k][7] = x[i]*a[k][4]     # xy2
      a[k][8] = a[k][2]*a[k][4]  # x2y2
  w = SVDsolve(a, z)
  zc = [poly2d(w,xi,yi) for xi in x for yi in y]
  R2 = cod(z,zc)
  R2a = 1.0-(1.0-R2)*(n-1.0)/(n-p)
  return w, R2a

def poly2Dfit(x, y, z):
  "x, y and z are all the same length"
  p = 8
  n = len(z)
  a = makemat(n, p+1, 0.0)
  for i in range(n):
    a[i][0] = 1.0                # const
    a[i][1] = x[i]               # x
    a[i][2] = x[i]*x[i]          # x2
    a[i][3] = y[i]               # y
    a[i][4] = y[i]*y[i]          # y2
    a[i][5] = x[i]*y[i]          # xy
    a[i][6] = a[i][2]*y[i]       # x2y
    a[i][7] = x[i]*a[i][4]       # xy2
    a[i][8] = a[i][2]*a[i][4]    # x2y2
  w = SVDsolve(a, z)
  zc = [poly2d(w,xi,yi) for xi in x for yi in y]
  R2 = cod(z,zc)
  R2a = 1.0-(1.0-R2)*(n-1.0)/(n-p)
  return w, R2a

# ---------------------------------------------------------------------

# -----------------------------------------
# ARI polynomial curvefit by SVD
# const, x, y, x2, xy, y2, x3, x2y, xy2, y3
# -----------------------------------------

def polyARI(c,x,y):
  return c[0]+x*(x*(x*c[6]+c[3])+c[1])+y*(y*(y*c[9]+c[5])+c[2])+x*y*(c[4]+x*c[7]+y*c[8])

def polyARIfit(x, y, z):
  p = 9
  n = len(z)
  a = makemat(n, p+1, 0.0)
  for i in range(n):
    a[i][0] = 1.0
    a[i][1] = x[i]               # x
    a[i][2] = y[i]               # y
    a[i][3] = x[i]*x[i]          # x2
    a[i][4] = x[i]*y[i]          # xy
    a[i][5] = y[i]*y[i]          # y2
    a[i][6] = a[i][3]*x[i]       # x3
    a[i][7] = a[i][3]*y[i]       # x2y
    a[i][8] = x[i]*a[i][5]       # xy2
    a[i][9] = a[i][5]*y[i]       # y3
  w = SVDsolve(a, z)
  zc = [polyARI(w,xi,yi) for xi in x for yi in y]
  R2 = cod(z,zc)
  R2a = 1.0-(1.0-R2)*(n-1.0)/(n-p)
  return w, R2a


# ---------------------------------------------------------------------

if __name__ == '__main__':

  print('linear equation solution [A][x]=[b]')
  print('sample from Gerald page 78')
  a = [[3,-1,2],[1,2,3],[2,-2,-1]]
  b = [12,11,2]
  x = SVDsolve(a, b) # x=[3,2,1]
  print('b:', showvec(x))
  print()

  print('example with specified polynomial')
  x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  c = [246.78,24.676,2.4678,0.24679]
  for i in range(len(x)):
    y[i] = polyh(c, x[i])
  c, R2a = polyfit(x, y, 3)
  print('C:', showvec(c, '%0.5f'))
  print('R2a %0.6f'%(R2a))
  print()

  print('example from HP-41C STAT PAC manual page 47')
  x = [0.8,1.0,1.2,1.4,1.6]
  y = [24,20,10,13,12]
  c, R2a = polyfit(x, y, 3)
  print('C:',showvec(c, '%0.5f'))
  print('R2a %0.6f' % (R2a)) # R2a=0.74
  print()

  print('poly2D Example')
  x = [float(i) for i in range(10)]
  y = [10.0*float(j) for j in range(4)]
  c = [2.24689,1.8,1.7,1.6,1.5,1.4,1.3,1.2,1.1]
  z = []
  for i in range(len(x)):
    for j in range(len(y)):
      z.append(poly2d(c, x[i], y[j]))
  c, R2a = MLRfit(x, y, z)
  print('C:', showvec(c, '%0.5f'))
  print('R2a %0.6f' % (R2a))
  print()

"""
Lagrange 2D
Stoecker "Design of Thermal Systems", 2nd ed. page 62.
Bruce Wernick
10 October 2017 15:38:10
"""

from __future__ import division

def lagrange2d(X, Y, Z):
  """lagrangian interpolation of 2-D table.
  X[0..m-1] and Y[0..n-1] are the independent variables.
  Z[0..n-1,0..m-1] is the dependent variable
  """
  m, n = len(X), len(Y)
  if len(Z) <> n or len(Z[0]) <> m:
    raise ValueError('Z dimensions must be the same as X by Y!')
  def f(x, y):
    z = 0.0
    for i in range(m):
      for j in range(n):
        p = 1.0
        for k in range(m):
          if i == k: continue
          p *= (x - X[k]) / (X[i] - X[k])
        for k in range(n):
          if j == k: continue
          p *= (y - Y[k]) / (Y[j] - Y[k])
        z += Z[j][i] * p
    return z
  return f


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  # 2D Lagrange example
  x = [1,2,3,4,5]
  y = [2,4,6]
  z = [[1,2,3,4,5],
       [2,3,4,5,6],
       [3,4,5,6,7]]
  f = lagrange2d(x,y,z)
  print f(2,4)




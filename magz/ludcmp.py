"""
LU Decomposition.
Reference: NR3 C++
Bruce Wernick
10 June 2021
"""

from copy import deepcopy
from nrutils import vector

TINY = 1.0e-40

class LUdcmp():
  """LU decomposition class
  """
  def __init__(self, a):
    n = len(a)
    self.n = n
    self.lu = deepcopy(a)
    self.aref = deepcopy(a)
    self.indx = vector(n, 0)
    vv = vector(n)
    self.d = 1
    for i in range(n):
      big = 0
      for j in range(n):
        temp = abs(self.lu[i][j])
        if temp > big:
          big = temp
      if big == 0:
        nrerror("Singular matrix in LUdcmp")
      vv[i] = 1 / big
    for k in range(n):
      big = 0
      imax = k
      for i in range(k, n):
        temp = vv[i] * abs(self.lu[i][k])
        if temp > big:
          big = temp
          imax = i
      if k != imax:
        for j in range(n):
          temp = self.lu[imax][j]
          self.lu[imax][j] = self.lu[k][j]
          self.lu[k][j] = temp
        self.d = -self.d
        vv[imax] = vv[k]
      self.indx[k] = imax
      if self.lu[k][k] == 0:
        self.lu[k][k] = TINY
      for i in range(k+1, n):
        self.lu[i][k] /= self.lu[k][k]
        temp = self.lu[i][k]
        for j in range(k+1, n):
          self.lu[i][j] -= temp*self.lu[k][j]

  def solveVec(self, _b, _x):
    n = self.n
    b = deepcopy(_b)
    x = deepcopy(_x)
    ii = 0
    if (len(b) != n or len(x) != n):
      nrerror("LUdcmp::solve bad sizes")
    for i in range(n):
      x[i] = b[i]
    for i in range(n):
      ip = self.indx[i]
      sum = x[ip]
      x[ip] = x[i]
      if ii != 0:
        for j in range(ii-1, i):
          sum -= self.lu[i][j] * x[j]
      elif sum != 0.0:
        ii = i + 1
      x[i] = sum
    for i in range(n-1, -1, -1):
      sum = x[i]
      for j in range(i+1, n):
        sum -= self.lu[i][j] * x[j]
      x[i] = sum / self.lu[i][i]
    return x

  def solveMat(self, _b, _x):
    """
    b is a matrix
    """
    b = deepcopy(_b)
    x = deepcopy(_x)
    n = self.n
    m = len(b[0])
    if (len(b) != n or len(x) != n or m != len(x[0])):
      nrerror("LUdcmp::solve bad sizes")
    xx = vector(n)
    for j in range(m):
      for i in range(n):
        xx[i] = b[i][j]
      solveVec(xx, xx)
      for i in range(n):
        x[i][j] = xx[i]
    return x

  def inverse(self, ainv):
    ainv = matrix(n, n)
    for i in range(n):
      for j in range(n):
        ainv[i][j] = 0
      ainv[i][i] = 1
    solveMat(ainv, ainv)

  def det(self):
    dd = self.d
    for i in range(self.n):
      dd *= self.lu[i][i]
    return dd

  def mprove(self, b, x):
    n = self.n
    r = vector(n)
    for i in range(n):
      sdp = -b[i]
      for j in range(n):
        sdp += aref[i][j] * x[j]
      r[i] = sdp
    solveVec(r, r)
    for i in range(n):
      x[i] -= r[i]


# ---------------------------------------------------------------------

if __name__=="__main__":

  # LU Decomp example
  A = [[8,1,6],[4,9,2],[0,5,7]]
  lud = LUdcmp(A)
  print(lud.lu)

"""
NRUtils.
based on NR3 C++.
Bruce Wernick
10 June 2021
"""

import sys
from math import fabs

def nrerror(s):
  print(sys.stderr, s)
  sys.exit()

def vector(n, value=0.0):
  return [value for _ in range(n)]

def matrix(n, m, value=0.0):
  return [vector(m,value) for _ in range(n)]

def SQR(a):
  sqrarg=a
  if sqrarg==0: return 0
  return sqrarg*sqrarg

def DSQR(a):
  dsqrarg=a
  if dsqrarg==0: return 0
  return dsqrarg*dsqrarg

def DMAX(a,b):
  dmaxarg1,dmaxarg2=a,b
  if dmaxarg1>dmaxarg2: return dmaxarg1
  return dmaxarg2

def DMIN(a,b):
  dminarg1,dminarg2=a,b
  if dminarg1<dminarg2: return dminarg1
  return dminarg2

def FMAX(a,b):
  maxarg1,maxarg2=a,b
  if maxarg1>maxarg2: return maxarg1
  return maxarg2

def FMIN(a,b):
  minarg1,minarg2=a,b
  if minarg1<minarg2: return minarg1
  return minarg2

def LMAX(a,b):
  lmaxarg1,lmaxarg2=a,b
  if lmaxarg1>lmaxarg2: return lmaxarg1
  return lmaxarg2

def LMIN(a,b):
  lminarg1,lminarg2=a,b
  if lminarg1<lminarg2: return lminarg1
  return lminarg2

def IMAX(a,b):
  imaxarg1,imaxarg2=a,b
  if imaxarg1>imaxarg2: return imaxarg1
  return imaxarg2

def IMIN(a,b):
  iminarg1,iminarg2=a,b
  if iminarg1<iminarg2: return iminarg1
  return iminarg2

def SIGN(a,b):
  if b>= 0.0: return fabs(a)
  return -fabs(a)

def mult_matrix(A, B):
  """Multiply matrices of same dimension M and N"""
  t = list(zip(*B))
  return [[sum(m*n for m,n in zip(i,j)) for j in t] for i in A]

def show_mat(A, ndec=6):
  n=len(A)
  return [[round(A[i][j],ndec) for j in range(n)] for i in range(n)]

def mat_size(A):
  'return rows,cols'
  return len(A), len(A[0])

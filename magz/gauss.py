"""
Gauss Elimination.
Bruce Wernick
10 June 2021
"""

import copy

__all__ = ['gauss', 'gaussj']


def gauss(A):
  A = copy.deepcopy(A)
  m = len(A)
  n = m+1
  for k in range(m):
    piv = [abs(A[i][k]) for i in range(k, m)]
    imax = piv.index(max(piv)) + k
    A[k], A[imax] = A[imax], A[k]
    for i in range(k+1, m):
      f = A[i][k] / A[k][k]
      for j in range(k+1,n):
        A[i][j] -= A[k][j]*f
      A[i][k] = 0
  x = []
  for i in range(m-1,-1,-1):
    x.insert(0, A[i][m] / A[i][i])
    for k in range(i-1,-1,-1):
      A[k][m] -= A[k][i]*x[0]
  return x


def gaussjor(A, b):
  """Gauss-Jordan Elimination Ax=b
  Append b to A and call gauss
  """
  n = len(A)
  for j in range(n):
    A[j].append(b[j])
  return gauss(A)


def gaussj(A, b):
  """
  Solve Ax = b by Gauss-Jordan Elimination (no pivoting)
  returns solution vector x
  """
  A = copy.deepcopy(A)

  # number of rows in A
  n = len(A)

  # append b to A
  for j in range(n):
    A[j].append(b[j])


  # loop through cols
  for i in range(n):

    # Search for max in col
    maxVal = abs(A[i][i])
    maxRow = i

    for j in range(i+1, n):
      if abs(A[j][i]) > maxVal:
        maxVal = abs(A[j][i])
        maxRow = j

    # Swap max row with current row
    for j in range(i, n+1):
      tmp = A[maxRow][j]
      A[maxRow][j] = A[i][j]
      A[i][j] = tmp

    # Make all rows below this one 0 in current column
    for j in range(i+1, n):
      c = -A[j][i] / A[i][i]
      for k in range(i, n+1):
        if i == k:
          A[j][k] = 0
        else:
          A[j][k] += c * A[i][k]

  # Solve equation Ax = b for an upper triangular matrix A
  x = [0 for i in range(n)]
  for i in range(n-1, -1, -1):
    x[i] = A[i][n] / A[i][i]
    for j in range(i-1, -1, -1):
      A[j][n] -= A[j][i] * x[i]

  # return the solution vector x
  return x


# ---------------------------------------------------------------------

if __name__ == "__main__":

  A = [[4,-2,1],[-2,4,-2],[1,-2,4]]
  b = [11,-16,17]

  C = [[4,-2,1,11],[-2,4,-2,-16],[1,-2,4,17]]
  x = gauss(C)
  print(x)

  x = gaussj(A, b)
  print(x)

  x = gaussjor(A, b)
  print(x)


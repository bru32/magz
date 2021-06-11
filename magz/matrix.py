"""
Matrix Multiplication.
Bruce Wernick
10 June 2021
"""

__all__ = ['mult']


def mult1(A, B):
  """long method
  """
  m = len(A)
  n = len(B)
  p = len(B[0])
  C = [[0 for _ in range(p)] for _ in range(n)]
  for i in range(m):
    for j in range(p):
      for k in range(n):
        C[i][j] += A[i][k]*B[k][j]
  return C

def mult2(A, B):
  """list comprehension method
  """
  m = len(A)
  n = len(B)
  q = len(B[0])
  return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(q)] for i in range(m)]

def mult3(A, B):
  """compact list comprehension with zip
  """
  zipB = list(zip(*B))
  return [[sum(a*b for a,b in zip(Ar,Bc)) for Bc in zipB] for Ar in A]

def mult(A, B):
  """matrix multiplication
  """
  zipB = list(zip(*B))
  return [[sum(a*b for a,b in zip(Ar,Bc)) for Bc in zipB] for Ar in A]


# ---------------------------------------------------------------------

if __name__=='__main__':

  A = [[12,7,3],[4,5,6],[7,8,9]]
  B = [[5,8,1,2],[6,7,3,0],[4,5,9,1]]
  # A x B = [[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]]

  C = mult1(A, B)
  print(f'mult1 = {C}')
  
  C = mult2(A, B)
  print(f'mult2 = {C}')

  C = mult3(A, B)
  print(f'mult3 = {C}')

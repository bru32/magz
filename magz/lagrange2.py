"""
Lagrange 2D.
Stoecker "Design of Thermal Systems", 2nd ed. page 62.
Bruce Wernick
10 June 2021
"""

def lagrange2d(X, Y, Z):
  """Lagrangian interpolation of 2-D table.
  X[0..m-1] and Y[0..n-1] are the independent variables.
  Z[0..n-1,0..m-1] is the dependent variable
  """
  m = len(X)
  n = len(Y)
  if not(len(Z) == n) or not(len(Z[0]) == m):
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

def polyARI(coeff,x,y):
  a,b,c,d,e,f,g,h,i,j = coeff
  return a+x*(x*(x*g+d)+b)+y*(y*(y*j+f)+c)+x*y*(e+x*h+y*i)

def frange(a, b, n):
  r = []
  for i in range(n):
    r.append(a + (b-a)*float(i)/(n-1.0))
  return r


# ---------------------------------------------------------------------

if __name__ == '__main__':
  # thermal engineering example
  # te = evap temp [degC]
  # tc = cond temp [degC]
  # qe = cooling duty [kW]
  te = [-5.0, 0.0, 5.0, 6.0, 10.0, 12.5]
  tc = [32.0, 35.0, 45.0, 47.0, 55.0]

  # build some realistic data using ari coefficients
  a = [17.28,8.4e-1,1.09e-1,1.5e-2,-7.0e-3,-5.66e-3,
       1.014e-4,-1.56e-4,2.06e-05,3.72e-05]
  qe = [[polyARI(a, x, y) for x in te] for y in tc]

  # create a lagrangian interpolator
  q = lagrange2d(te,tc,qe)

  # show the differences
  tcRange = frange(tc[0], tc[-1], 7)
  teRange = frange(te[0], te[-1], 9)
  print(' '*8 + 'Difference table')
  print(' '*6,)
  for x in teRange:
    print('{:6.2f}'.format(x),)
  print()
  print('-'*69)
  for y in tcRange:
    print('{:6.2f}'.format(y),)
    for x in teRange:
      q1 = q(x, y)
      q2 = polyARI(a, x, y)
      print('{:6.2f}'.format(q2),)
    print()

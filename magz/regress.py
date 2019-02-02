"""
Simply (pure Python) regression
Bruce Wernick
10 October 2017 15:38:10
"""

__all__ = ['cod', 'linreg']


def cod(X, Y):
  "Coefficient of determination, R2"
  n = len(X)
  sx = sy = sxx = syy = sxy = 0.0
  for x,y in zip(X,Y):
    sx += x
    sy += y
    sxx += x*x
    syy += y*y
    sxy += x*y
  a = n*sxy - sx*sy
  b = n*sxx - sx*sx
  c = n*syy - sy*sy
  return a*a/b/c

def linreg(X, Y):
  "linear regression, based on Wiki"
  n = len(X)
  Sx = Sy = Sxx = Syy = Sxy = 0.0
  for x,y in zip(X,Y):
    Sx += x
    Sy += y
    Sxx += x*x
    Syy += y*y
    Sxy += x*y
  d = n*Sxx - Sx*Sx
  c = n*Sxy - Sx*Sy
  f = n*Syy - Sy*Sy
  g = Sy*Sxx - Sx*Sxy
  a = g/d
  b = c/d
  return a, b, b*c/f


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  x = [1,2,3,4,5]
  y = [1.99,4,6,8.01,10]
  print('linreg')
  a, b, r2 = linreg(x,y)
  print(('coeff = {} {}, r2={}\n'.format(a, b, r2)))


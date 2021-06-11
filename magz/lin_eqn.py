"""
Linear Algebra.
Bruce Wernick
10 June 2021
"""

import gauss

def lin_leastsq(x, y):
  """Linear Least Squares curve fit (manual method).
  """
  n = len(x)
  sx = sy = sx2 = sy2 = sxy = 0.0
  for i in range(0,n):
    sx += x[i]
    sy += y[i]
    sx2 += x[i]*x[i]
    sy2 += y[i]*y[i]
    sxy += x[i]*y[i]

  C = [[n,sx,sy],[sx,sx2,sxy]]
  coeff = gauss.gauss(C)
  a = coeff[0]
  b = coeff[1]
  r = (a*sy + b*sxy - (sy*sy)/n) / (sy2 - (sy*sy)/n)
  return coeff, r


# ---------------------------------------------------------------------

if __name__ == '__main__':

  # (x,y) values of function
  x = [1,2,3,4]
  y = [2,4,6,8]

  # linear least squares curve-fit
  coeff, r = lin_leastsq(x, y)
  print(f'coeff = {coeff}, r = {r:0.6f}')

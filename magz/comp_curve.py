"""
MLR Curve Fitter.
Bruce Wernick
10 June 2021
"""

import numpy as np
from scipy.optimize import leastsq
from scipy.stats import linregress
from scipy import interpolate, array

__all__ = ['poly2D', 'polyARI', 'do_stats', 'get_outlier', 
  'fit2D', 'fitARI', 'prep', 'CurveFit', 
  'poly2ARI', 'ari2Poly', 'Interpolate']


def poly2D(coeff,x,y):
  "2D polynomial evaluation"
  a,b,c,d,e,f,g,h,i = coeff
  return a+x*(b+x*c)+y*(d+y*e)+x*y*(f+x*g+y*h+x*y*i)

def polyARI(coeff,x,y):
  "ARI polynomial evaluation"
  a,b,c,d,e,f,g,h,i,j = coeff
  return a+x*(x*(x*g+d)+b)+y*(y*(y*j+f)+c)+x*y*(e+x*h+y*i)

def resid2D(a,x,y,z):
  "Poly2D error function"
  return poly2D(a,x,y)-z

def residARI(a,x,y,z):
  "ARI error function"
  return polyARI(a,x,y)-z

def do_stats(x,y):
  "calculate the coefficient of determination"
  slope, intercept, r_value, p_value, std_err = linregress(x,y)
  return r_value**2

def get_outlier(a, xList, yList, zList, factor, kind):
  "Find outlier data points"
  x,y,z = prep(xList, yList, zList, factor)
  if kind=='ari':
    zc = polyARI(a, x, y)
  elif kind=='2d':
    zc = poly2D(a, x, y)
  k = None
  for i in range(len(x)):
    e = abs(z[i]-zc[i])
    if not k: k = (i, e)
    if e > k[1]: k = (i, e)
  i = k[0]
  return round(x[i],2), round(y[i],2), round(z[i],4), round(zc[i],4), round(k[1],4)

def fit2D(a, x, y, z):
  "Poly2D Curve fitter"
  a, ier = leastsq(resid2D, a, args=(x,y,z))
  if ier in [1,2,3,4]:
    zc = poly2D(a, x, y)
    cod = do_stats(z, zc)
    return a,cod
  return [],0

def fitARI(a, x, y, z):
  "ARI Curve fitter"
  a, ier = leastsq(residARI, a, args=(x,y,z))
  if ier in [1,2,3,4]:
    zc = polyARI(a, x, y)
    cod = do_stats(z, zc)
    return a,cod
  return [],0

def prep(xRange, yRange, zData, factor):
  """Prepare data vectors for CurveFit
  """
  m = len(xRange)
  n = len(yRange)
  if len(zData)!=n or len(zData[0])!=m:
    raise ValueError('zData has wrong size')
  x,y,z = [],[],[]
  for j in range(n):
    for i in range(m):
      if zData[j][i] > 0:
        x.append(xRange[i])
        y.append(yRange[j])
        z.append(factor*zData[j][i])
  return np.array(x), np.array(y), np.array(z)

def CurveFit(xList, yList, zList, a=None, factor=1.0, kind='ari'):
  """xList and yList are lists of the independent variables.
  zList is a 2-d list of the dependent variable. The dimensions
  of z must be the same as the len(xList) x len(yList).
  """
  x,y,z = prep(xList, yList, zList, factor)
  if kind == 'ari':
    if not a:
      a = [1.0 for i in range(10)]
    a,cod = fitARI(a, x, y, z)
  elif kind == '2d':
    if not a:
      a = [1.0 for i in range(9)]
    a,cod = fit2D(a, x, y, z)
  else:
    a,cod = [],0
  return list(a), cod

def poly2ARI(x0, x1, y0, y1, coeff):
  """convert Poly2D coefficients to ARI
  coeff must have 9 values.
  """
  n = 48 # number of points to generate for each variable
  xList = []
  yList = []
  zList = []
  for j in range(n-1):
    y = y0 + (y1-y0)*j/n
    yList.append(y)
    inner = []
    xList = []
    for i in range(n-1):
      x = x0 + (x1-x0)*i/n
      xList.append(x)
      z = poly2D(coeff, x, y)
      inner.append(z)
    zList.append(inner)
  return CurveFit(xList, yList, zList)

def ari2Poly(x0, x1, y0, y1, coeff):
  """convert ARI coefficients to Poly2D
  coeff must have 10 values.
  """
  n = 48 # number of points to generate for each variable
  xList = []
  yList = []
  zList = []
  for j in range(n-1):
    y = y0 + (y1-y0)*j/n
    yList.append(y)
    inner = []
    xList = []
    for i in range(n-1):
      x = x0 + (x1-x0)*i/n
      xList.append(x)
      z = polyARI(coeff, x, y)
      inner.append(z)
    zList.append(inner)
  return CurveFit(xList, yList, zList, kind='2d')

def Interpolate(x, xValues, y, yValues, z):
  """z is a 2D array of values
  x and y are the co-ordinate values
  """
  if (x < x[0]) or (x > x[-1]) or (y < y[0]) or (y > y[-1]):
    return -1
  f = interpolate.interp2d(xValues, yValues, z, kind='cubic', fill_value=-1)
  for i,y in enumerate(yValues):
    for j,x in enumerate(xValues):
      if z[i][j] != -1:
        return f(x,y)[0]-qe[i][j]
      else:
        return -1


# ---------------------------------------------------------------------

if __name__=='__main__':

  te = [-23.33,-17.78,-12.22,-6.67,-1.11,4.44,7.22,10.00,12.78]
  tc = [65.56,60.00,54.44,48.89,43.33,37.78,32.22,26.67]
  qe = [[0,0,0,0,0,12775,14269,15822,17580],
        [0,0,0,0,10929,13800,15382,17088,18898],
        [0,0,0,9259,11866,14894,16554,18405,20363],
        [0,0,7706,10079,12833,16001,17801,19732,21828],
        [0,6270,8468,10900,13771,17122,19045,21096,23293],
        [4981,6944,9142,11691,14650,18166,20217,22414,24758],
        [5567,7501,9728,12364,15470,19191,21297,23586,26122],
        [5977,7911,10167,12892,16115,20070,22268,24758,27395]]

  kind = 'ari'
  factor = 1e-3
  a0 = [17.2797,0.839686,0.108983,0.0151333,-0.00703109,
        -0.00566044,0.000101379,-0.000156348,2.06388e-05,3.72305e-05]
  a, cod = CurveFit(te, tc, qe, a0, factor, kind)
  print(polyARI(a, 6.0, 47.0))
  print(a)
  
  a = [float('{:0.6g}'.format(x)) for x in a]
  print(kind, list(a), round(cod,5))
  print(get_outlier(a, te, tc, qe, factor, kind))


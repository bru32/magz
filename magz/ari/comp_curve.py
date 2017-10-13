"""
MLR Curve Fitter
Bruce Wernick
10 October 2017 15:38:10
"""

from __future__ import division
import numpy as np
from scipy.optimize import leastsq
from scipy.stats import linregress

__all__ = ['CurveFit', 'get_outlier']


def poly2D((a,b,c,d,e,f,g,h,i),x,y):
  return a+x*(b+x*c)+y*(d+y*e)+x*y*(f+x*g+y*h+x*y*i)

def polyARI((a,b,c,d,e,f,g,h,i,j),x,y):
  return a+x*(x*(x*g+d)+b)+y*(y*(y*j+f)+c)+x*y*(e+x*h+y*i)

def resid2D(a, x, y, z):
  return poly2D(a,x,y)-z

def residARI(a, x, y, z):
  return polyARI(a,x,y)-z

def do_stats(x,y):
  slope, intercept, r_value, p_value, std_err = linregress(x, y)
  return r_value**2

def get_outlier(a, xList, yList, zList, factor, kind):
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
  a, ier = leastsq(resid2D, a, args=(x,y,z))
  if ier in [1,2,3,4]:
    zc = poly2D(a, x, y)
    cod = do_stats(z, zc)
    return a,cod
  return [],0

def fitARI(a, x, y, z):
  a, ier = leastsq(residARI, a, args=(x,y,z))
  if ier in [1,2,3,4]:
    zc = polyARI(a, x, y)
    cod = do_stats(z, zc)
    return a,cod
  return [],0

def prep(xRange, yRange, zData, factor):
  m = len(xRange)
  n = len(yRange)
  if len(zData)<>n or len(zData[0])<>m:
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


# ------------------------------------------------------------------------------

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
  print polyARI(a, 6.0, 47.0)
  print a
  a = [float('{:0.6g}'.format(x)) for x in a]
  print kind, list(a), round(cod,5)
  print get_outlier(a, te, tc, qe, factor, kind)

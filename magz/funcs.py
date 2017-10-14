"""
Math Functions.
For consistency, I have repeated some functions and re-structured the
parameters so that they all have the same format.
Bruce Wernick
10 October 2017 15:38:10
"""

import math

__all__ = ['Quad', 'Cubic', 'PolyEval', 'PolyEvalH', 'poly2D', 'polyARI',
  'ExpFunc', 'ModExpFunc', 'LogFunc', 'RecipLogFunc', 'VaporPressureFunc',
  'PowerFunc', 'ModPowerFunc', 'ShiftPowerFunc', 'GeometricFunc',
  'ModGeometricFunc', 'RootFunc', 'HoerlFunc', 'ModHoerlFunc', 'RecipFunc',
  'RecipQuadFunc', 'BleasdaleFunc', 'HarrisFunc', 'ExpAssocFunc2',
  'ExpAssocFunc3', 'SatGrowthFunc', 'GompertzFunc', 'LogisticFunc',
  'RichardsFunc', 'MMFFunc', 'WeibullFunc', 'SinusoidalFunc', 'GaussianFunc',
  'HyperbolicFunc', 'HeatCapacityFunc', 'RationalFunc']

def Quad(x,(a,b,c)):
  'quadratic (hard coded for speed)'
  return a + x*(b + x*c)

def Cubic(x,(a,b,c,d)):
  'cubic (hard coded for speed)'
  return a + x*(b + x*(c + x*d))

def PolyEval(x,a):
  'polynomial, a[0] + x*(a[1] + x*(a[2] ... +  x*a[n-1]))'
  p = 0.0
  for c in reversed(a):
    p = c + p * x
  return p

def PolyEvalH(x,a):
  'reversed polynomial, ((a[0]*x + a[1])*x + a[2])*x + ... + a[n-1]'
  n = len(a)
  p = 0.0
  for i in range(0, n-1):
    p = (p + a[i])*x
  p += a[n-1]
  return p

def poly2D(x,y,(a,b,c,d,e,f,g,h,i)):
  '2D quadratic with cross-terms'
  return a + x*(b + x*c) + y*(d + y*e) + x*y*(f + x*g + y*h + x*y*i)

def polyARI(x,y,(a,b,c,d,e,f,g,h,i,j)):
  'ARI compressor polynomial (upper right corner)'
  return a + x*(x*(x*g + d) + b) + y*(y*(y*j + f) + c) + x*y*(e + x*h + y*i)

def ExpFunc(x,(a,b)):
  'exponential function'
  return a * math.exp(b*x)

def ModExpFunc(x,(a,b)):
  'modified exponential function'
  return a * math.exp(b / x)

def LogFunc(x,(a,b)):
  'natural log function'
  return a + b * math.log(x)

def RecipLogFunc(x,(a,b)):
  'reciprocal log function'
  return 1.0 / (a + b * math.log(x))

def VaporPressureFunc(x,(a,b,c)):
  'vapor pressure function'
  return math.exp(a + b / x + c * math.log(x))

def PowerFunc(x,(a,b)):
  'power function'
  return a * x**b

def ModPowerFunc(x,(a,b)):
  'modified power function'
  return a * b**x

def ShiftPowerFunc(x,(a,b,c)):
  'shifted power function'
  return a * (x - b)**c

def GeometricFunc(x,(a,b)):
  'geometric function'
  return a * x**(b*x)

def ModGeometricFunc(x,(a,b)):
  'modified geometric function'
  return a * x**(b / x)

def RootFunc(x,a):
  'root function'
  return a**(1.0 / x)

def HoerlFunc(x,(a,b,c)):
  'hoerl function'
  return a * (b**x) * (x**c)

def ModHoerlFunc(x,(a,b,c)):
  'modified hoerl function'
  return a * (b**(1.0 / x)) * (x**c)

def RecipFunc(x,(a,b)):
  'reciprocal linear function'
  return 1.0 / (a + b*x)

def RecipQuadFunc(x,(a,b,c)):
  'reciprocal quadratic function'
  return 1.0 / (a + x*(b + x*c))

def BleasdaleFunc(x,(a,b,c)):
  'bleasdale function'
  return (a + b*x)**(-1.0 / c)

def HarrisFunc(x,(a,b,c)):
  'harris function'
  return 1.0 / (a + (b*x)**c)

def ExpAssocFunc2(x,(a,b)):
  'exponential associative function (2 coeff)'
  return a * (1.0 - math.exp(-b*x))

def ExpAssocFunc3(x,(a,b,c)):
  'exponential associative function (3 coeff)'
  return a * (b - math.exp(-c*x))

def SatGrowthFunc(x,(a,b)):
  'saturation growth model'
  return a * x / (b + x)

def GompertzFunc(x,(a,b,c)):
  'gompertz function'
  return a * math.exp(-math.exp(b - c*x))

def LogisticFunc(x,(a,b,c)):
  'logistic function'
  return a / (1.0 + math.exp(b - c*x))

def RichardsFunc(x,(a,b,c,d)):
  'richards function'
  return a / ((1.0 + math.exp(b - c*x))**(1.0/d))

def MMFFunc(x,(a,b,c,d)):
  'mmf function'
  xa3 = x**d
  return (a*b + c*xa3) / (b + xa3)

def WeibullFunc(x,(a,b,c,d)):
  'weibull function'
  return a - b * math.exp(-c * x**d)

def SinusoidalFunc(x,(a,b,c,d)):
  'sinusoidal function'
  return a + b * math.cos(c*x + d)

def GaussianFunc(x,(a,b,c)):
  'gaussian function'
  return a * math.exp((-(x - b)**2) / (2.0*(c**2)))

def HyperbolicFunc(x,(a,b)):
  'hyperbolic function'
  return a + b / x

def HeatCapacityFunc(x,(a,b,c)):
  'heat capacity function (inverse quadratic)'
  return a + b*x + c/x**2

def RationalFunc(x,(a,b,c,d)):
  'rational function'
  return (a + b*x) / (1.0 + x*(c + x*d))


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  print 'start...'
  x,y = 1.7, 3.4
  a,b,c,d,e = 0.1,0.2,0.3,0.4,0.5
  f,g,h,i,j = 0.15,0.25,0.35,0.45,0.55
  print 'Quadratic     : {:0.4g}'.format(Quad(x,(a,b,c)))
  print 'Cubic         : {:0.4g}'.format(Cubic(x,(a,b,c,d)))
  print 'Polynomial    : {:0.4g}'.format(PolyEval(x,[a,b,c,d]))
  print 'Poly (rev)    : {:0.4g}'.format(PolyEvalH(x,[d,c,b,a]))
  print 'poly (2D)     : {:0.4g}'.format(poly2D(x,y,(a,b,c,d,e,f,g,h,i)))
  print 'poly (ARI)    : {:0.4g}'.format(polyARI(x,y,(a,b,c,d,e,f,g,h,i,j)))
  print 'Exponential   : {:0.4g}'.format(ExpFunc(x,(a,b)))
  print 'Modified Exp  : {:0.4g}'.format(ModExpFunc(x,(a,b)))
  print 'Logarithmic   : {:0.4g}'.format(LogFunc(x,(a,b)))
  print 'Recip Log     : {:0.4g}'.format(RecipLogFunc(x,(a,b)))
  print 'Vap Pressure  : {:0.4g}'.format(VaporPressureFunc(x,(a,b,c)))
  print 'Power         : {:0.4g}'.format(PowerFunc(x,(a,b)))
  print 'Mod Power     : {:0.4g}'.format(ModPowerFunc(x,(a,b)))
  print 'Shifted Power : {:0.4g}'.format(ShiftPowerFunc(x,(a,b,c)))
  print 'Geometric     : {:0.4g}'.format(GeometricFunc(x,(a,b)))
  print 'Mod Geom      : {:0.4g}'.format(ModGeometricFunc(x,(a,b)))
  print 'Root          : {:0.4g}'.format(RootFunc(x,a))
  print 'Hoerl         : {:0.4g}'.format(HoerlFunc(x,(a,b,c)))
  print 'Mod Hoerl     : {:0.4g}'.format(ModHoerlFunc(x,(a,b,c)))
  print 'Reciprocal    : {:0.4g}'.format(RecipFunc(x,(a,b)))
  print 'Recip Quad    : {:0.4g}'.format(RecipQuadFunc(x,(a,b,c)))
  print 'Bleasdale     : {:0.4g}'.format(BleasdaleFunc(x,(a,b,c)))
  print 'Harris        : {:0.4g}'.format(HarrisFunc(x,(a,b,c)))
  print 'Exp Assoc 2   : {:0.4g}'.format(ExpAssocFunc2(x,(a,b)))
  print 'Exp Assoc 3   : {:0.4g}'.format(ExpAssocFunc3(x,(a,b,c)))
  print 'Sat Growth    : {:0.4g}'.format(SatGrowthFunc(x,(a,b)))
  print 'Gompertz      : {:0.4g}'.format(GompertzFunc(x,(a,b,c)))
  print 'Logistic      : {:0.4g}'.format(LogisticFunc(x,(a,b,c)))
  print 'Richards      : {:0.4g}'.format(RichardsFunc(x,(a,b,c,d)))
  print 'MMF           : {:0.4g}'.format(MMFFunc(x,(a,b,c,d)))
  print 'Weibull       : {:0.4g}'.format(WeibullFunc(x,(a,b,c,d)))
  print 'Sinusoidal    : {:0.4g}'.format(SinusoidalFunc(x,(a,b,c,d)))
  print 'Gaussian      : {:0.4g}'.format(GaussianFunc(x,(a,b,c)))
  print 'Hyperbolic    : {:0.4g}'.format(HyperbolicFunc(x,(a,b)))
  print 'Heat Capacity : {:0.4g}'.format(HeatCapacityFunc(x,(a,b,c)))
  print 'Rational      : {:0.4g}'.format(RationalFunc(x,(a,b,c,d)))
  print 'end...'

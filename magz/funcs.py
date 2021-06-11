"""
1D Math Functions.
Bruce Wernick
10 June 2021
"""

import math

__all__ = ['Quad', 'Cubic', 'PolyEval', 'PolyEvalH', 'ExpFunc', 
  'ModExpFunc', 'LogFunc', 'RecipLogFunc', 'VaporPressureFunc', 
  'PowerFunc', 'ModPowerFunc', 'ShiftPowerFunc', 'GeometricFunc', 
  'ModGeometricFunc', 'RootFunc', 'HoerlFunc', 'ModHoerlFunc', 
  'RecipFunc', 'RecipQuadFunc', 'BleasdaleFunc', 'HarrisFunc', 
  'ExpAssocFunc2', 'ExpAssocFunc3', 'SatGrowthFunc', 
  'GompertzFunc', 'LogisticFunc', 'RichardsFunc', 'MMFFunc', 
  'WeibullFunc', 'SinusoidalFunc', 'GaussianFunc', 
  'HyperbolicFunc', 'HeatCapacityFunc', 'RationalFunc']

def Quad(x,coeff):
  'quadratic (hard coded for speed)'
  a,b,c = coeff
  return a + x*(b + x*c)

def Cubic(x,coeff):
  'cubic (hard coded for speed)'
  a,b,c,d = coeff
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

def ExpFunc(x,coeff):
  'exponential function'
  a,b = coeff
  return a * math.exp(b*x)

def ModExpFunc(x,coeff):
  'modified exponential function'
  a,b = coeff
  return a * math.exp(b / x)

def LogFunc(x,coeff):
  'natural log function'
  a,b = coeff
  return a + b * math.log(x)

def RecipLogFunc(x,coeff):
  'reciprocal log function'
  a,b = coeff
  return 1.0 / (a + b * math.log(x))

def VaporPressureFunc(x,coeff):
  'vapor pressure function'
  a,b,c = coeff
  return math.exp(a + b / x + c * math.log(x))

def PowerFunc(x,coeff):
  'power function'
  a,b = coeff
  return a * x**b

def ModPowerFunc(x,coeff):
  'modified power function'
  a,b = coeff
  return a * b**x

def ShiftPowerFunc(x,coeff):
  'shifted power function'
  a,b,c = coeff
  return a * (x - b)**c

def GeometricFunc(x,coeff):
  'geometric function'
  a,b = coeff
  return a * x**(b*x)

def ModGeometricFunc(x,coeff):
  'modified geometric function'
  a,b = coeff
  return a * x**(b / x)

def RootFunc(x,a):
  'root function'
  return a**(1.0 / x)

def HoerlFunc(x,coeff):
  'hoerl function'
  a,b,c = coeff
  return a * (b**x) * (x**c)

def ModHoerlFunc(x,coeff):
  'modified hoerl function'
  a,b,c = coeff
  return a * (b**(1.0 / x)) * (x**c)

def RecipFunc(x,coeff):
  'reciprocal linear function'
  a,b = coeff
  return 1.0 / (a + b*x)

def RecipQuadFunc(x,coeff):
  'reciprocal quadratic function'
  a,b,c = coeff
  return 1.0 / (a + x*(b + x*c))

def BleasdaleFunc(x,coeff):
  'bleasdale function'
  a,b,c = coeff
  return (a + b*x)**(-1.0 / c)

def HarrisFunc(x,coeff):
  'harris function'
  a,b,c = coeff
  return 1.0 / (a + (b*x)**c)

def ExpAssocFunc2(x,coeff):
  'exponential associative function (2 coeff)'
  a,b = coeff
  return a * (1.0 - math.exp(-b*x))

def ExpAssocFunc3(x,coeff):
  'exponential associative function (3 coeff)'
  a,b,c = coeff
  return a * (b - math.exp(-c*x))

def SatGrowthFunc(x,coeff):
  'saturation growth model'
  a,b = coeff
  return a * x / (b + x)

def GompertzFunc(x,coeff):
  'gompertz function'
  a,b,c = coeff
  return a * math.exp(-math.exp(b - c*x))

def LogisticFunc(x,coeff):
  'logistic function'
  a,b,c = coeff
  return a / (1.0 + math.exp(b - c*x))

def RichardsFunc(x,coeff):
  'richards function'
  a,b,c,d = coeff
  return a / ((1.0 + math.exp(b - c*x))**(1.0/d))

def MMFFunc(x,coeff):
  'mmf function'
  a,b,c,d = coeff
  xa3 = x**d
  return (a*b + c*xa3) / (b + xa3)

def WeibullFunc(x,coeff):
  'weibull function'
  a,b,c,d = coeff
  return a - b * math.exp(-c * x**d)

def SinusoidalFunc(x,coeff):
  'sinusoidal function'
  a,b,c,d = coeff
  return a + b * math.cos(c*x + d)

def GaussianFunc(x,coeff):
  'gaussian function'
  a,b,c = coeff
  return a * math.exp((-(x - b)**2) / (2.0*(c**2)))

def HyperbolicFunc(x,coeff):
  'hyperbolic function'
  a,b = coeff
  return a + b / x

def HeatCapacityFunc(x,coeff):
  'heat capacity function (inverse quadratic)'
  a,b,c = coeff
  return a + b*x + c/x**2

def RationalFunc(x,coeff):
  'rational function'
  a,b,c,d = coeff
  return (a + b*x) / (1.0 + x*(c + x*d))


# ---------------------------------------------------------------------

if __name__ == '__main__':

  x,y = 1.7, 3.4
  a,b,c,d = 0.1,0.2,0.3,0.4

  z = Quad(x,(a,b,c))
  print(f'Quadratic     : {z:0.4g}')

  z = Cubic(x,(a,b,c,d))
  print(f'Cubic         : {z:0.4g}')

  z = PolyEval(x,[a,b,c,d])
  print(f'Polynomial    : {z:0.4g}')

  z = PolyEvalH(x,[d,c,b,a])
  print(f'Poly (rev)    : {z:0.4g}')

  z = ExpFunc(x,(a,b))
  print(f'Exponential   : {z:0.4g}')

  z = ModExpFunc(x,(a,b))
  print(f'Modified Exp  : {z:0.4g}')

  z = LogFunc(x,(a,b))
  print(f'Logarithmic   : {z:0.4g}')

  z = RecipLogFunc(x,(a,b))
  print(f'Recip Log     : {z:0.4g}')

  z = VaporPressureFunc(x,(a,b,c))
  print(f'Vap Pressure  : {z:0.4g}')

  z = PowerFunc(x,(a,b))
  print(f'Power         : {z:0.4g}')

  z = ModPowerFunc(x,(a,b))
  print(f'Mod Power     : {z:0.4g}')

  z = ShiftPowerFunc(x,(a,b,c))
  print(f'Shifted Power : {z:0.4g}')

  z = GeometricFunc(x,(a,b))
  print(f'Geometric     : {z:0.4g}')

  z = ModGeometricFunc(x,(a,b))
  print(f'Mod Geom      : {z:0.4g}')

  z = RootFunc(x,a)
  print(f'Root          : {z:0.4g}')

  z = HoerlFunc(x,(a,b,c))
  print(f'Hoerl         : {z:0.4g}')

  z = ModHoerlFunc(x,(a,b,c))
  print(f'Mod Hoerl     : {z:0.4g}')

  z = RecipFunc(x,(a,b))
  print(f'Reciprocal    : {z:0.4g}')

  z = RecipQuadFunc(x,(a,b,c))
  print(f'Recip Quad    : {z:0.4g}')

  z = BleasdaleFunc(x,(a,b,c))
  print(f'Bleasdale     : {z:0.4g}')

  z = HarrisFunc(x,(a,b,c))
  print(f'Harris        : {z:0.4g}')

  z = ExpAssocFunc2(x,(a,b))
  print(f'Exp Assoc 2   : {z:0.4g}')

  z = ExpAssocFunc3(x,(a,b,c))
  print(f'Exp Assoc 3   : {z:0.4g}')

  z = SatGrowthFunc(x,(a,b))
  print(f'Sat Growth    : {z:0.4g}')

  z = GompertzFunc(x,(a,b,c))
  print(f'Gompertz      : {z:0.4g}')

  z = LogisticFunc(x,(a,b,c))
  print(f'Logistic      : {z:0.4g}')

  z = RichardsFunc(x,(a,b,c,d))
  print(f'Richards      : {z:0.4g}')

  z = MMFFunc(x,(a,b,c,d))
  print(f'MMF           : {z:0.4g}')

  z = WeibullFunc(x,(d,c,b,a))
  print(f'Weibull       : {z:0.4g}')

  z = SinusoidalFunc(x,(a,b,c,d))
  print(f'Sinusoidal    : {z:0.4g}')

  z = GaussianFunc(x,(a,b,c))
  print(f'Gaussian      : {z:0.4g}')

  z = HyperbolicFunc(x,(a,b))
  print(f'Hyperbolic    : {z:0.4g}')

  z = HeatCapacityFunc(x,(a,b,c))
  print(f'Heat Capacity : {z:0.4g}')

  z = RationalFunc(x,(a,b,c,d))
  print(f'Rational      : {z:0.4g}')


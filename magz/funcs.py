"""
Math Functions
Bruce Wernick
10 October 2017 15:38:10
"""

import math

def ExpFunc(x,*a):
  return a[0] * math.exp(a[1]*x)

def ModExpFunc(x,*a):
  return a[0] * math.exp(a[1] / x)

def LogFunc(x,*a):
  return a[0] + a[1]*math.ln(x)

def RecipLogFunc(x,*a):
  return 1.0 / (a[0] + a[1]*math.ln(x))

def VaporressureFunc(x,*a):
  return exp(a[0] + a[1] / x + a[2]*math.ln(x))

def PowerFunc(x,*a):
  return a[0] * x**a[1]

def ModPowerFunc(x,*a):
  return a[0] * a[1]**x

def ShiftPowerFunc(x,*a):
  return a[0] * (x-a[1])**a[2]

def GeometricFunc(x,*a):
  return a[0]*x**(a[1]*x)

def ModGeometricFunc(x,*a):
  return a[0]*x**(a[1]/x)

def RootFunc(x,*a):
  return a[0]**(1.0/x)

def HoerlFunc(x,*a):
  return a[0]*(a[1]**x)*(x**a[2])

def ModHoerlFunc(x,*a):
  return a[0]*(a[1]**(1.0/x))*(x**a[2])

def RecipFunc(x,*a):
  return 1.0/(a[0]+a[1]*x)

def RecipQuadFunc(x,*a):
  return 1.0/(a[0] + x*(a[1] + x*a[2]))

def BleasdaleFunc(x,*a):
  return (a[0] + a[1]*x)**(-1.0/a[2])

def HarrisFunc(x,*a):
  return 1.0/(a[0] + (a[1]*x)**a[2])

def ExpAssocFunc2(x,*a):
  return a[0]*(1.0 - math.exp(-a[1]*x))

def ExpAssocFunc3(x,*a):
  return a[0]*(a[1] - math.exp(-a[2]*x))

def SatGrowthFunc(x,*a):
  return a[0]*x/(a[1] + x)

def GompertzFunc(x,*a):
  return a[0]*math.exp(-math.exp(a[1] - a[2]*x))

def LogisticFunc(x,*a):
  return a[0]/(1.0 + math.exp(a[1] - a[2]*x))

def RichardsFunc(x,*a):
  return a[0]/((1.0 + math.exp(a[1] - a[2]*x))**(1.0/a[3]))

def MMFFunc(x,*a):
  xa3 = x**a[3]
  return (a[0]*a[1] + a[2]*xa3)/(a[1] + xa3)

def WeibullFunc(x,*a):
  return a[0] - a[1]*math.exp(-a[2]*x**a[3])

def SinusoidalFunc(x,*a):
  return a[0] + a[1]*math.cos(a[2]*x + a[3])

def GaussianFunc(x,*a):
  return a[0]*math.exp((-(x - a[1])**2)/(2.0*(a[2]**2)))

def HyperbolicFunc(x,*a):
  return a[0] + a[1]/x

def HeatCapacityFunc(x,*a):
  return a[0] + a[1]*x + a[2]/x**2

def RationalFunc(x,*a):
  return (a[0] + a[1]*x)/(1.0 + x*(a[2] + x*a[3]))


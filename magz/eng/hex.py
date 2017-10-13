"""
Heat Exchanger Tools
Bruce Wernick
10 October 2017 15:38:10
"""

import math

__all__ = ['ePhase', 'eCounter', 'lmtd']


def ePhase(ntu):
  "Phase change effectiveness"
  return 1.0 - math.exp(-ntu)

def eCounter(cr, ntu):
  "counterflow effectiveness"
  n = math.exp(-ntu*(1.0-cr))
  return (1.0-n)/(1.0-cr*n)

def lmtd(itd, otd):
  "log mean difference"
  TINY = 1.0e-12
  if abs(itd)<=TINY and abs(otd)<=TINY: return TINY
  if abs(itd)<=TINY: return otd
  if abs(otd)<=TINY: return itd
  if abs(itd-otd)<=TINY: return itd
  return (itd-otd)/math.log(itd/otd)


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  print ePhase(3.0)
  print eCounter(0.7, 3.0)
  print lmtd(22.0, 24.0)

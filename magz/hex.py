"""
Heat Exchanger Tools.
Bruce Wernick
10 June 2021
"""

import math
from const import EPS

__all__ = ['ePhase', 'eCounter', 'lmtd']

def ePhase(ntu):
  "Phase change effectiveness"
  return 1.0 - math.exp(-ntu)

def eCounter(cr, ntu):
  "counterflow effectiveness"
  n = math.exp(-ntu*(1.0-cr))
  return (1.0-n)/(1.0-cr*n)

def eParallel(cr, ntu):
  "parallel flow effectiveness"
  c = 1.0 + cr
  return (1.0-exp(-ntu*c))/c

def lmd(itd, otd):
  """log mean difference
     itd = inlet difference
     otd = outlet difference
  """
  if abs(itd) <= EPS and abs(otd) <= EPS:
    return EPS
  if abs(itd) <= EPS:
    return otd
  if abs(otd) <= EPS:
    return itd
  if abs(itd-otd) <= EPS:
    return itd
  return (itd - otd) / math.log(itd / otd)

def lmtd(tci, tco, thi, tho, counterflow=True):
  """log mean temperature difference
     tci = cold inlet
     tco = cold outlet
     thi = hot inlet
     tho = hot outlet
  """
  if counterflow:
    itd = thi - tco
    otd = tho - tci
  else:
    itd = thi - tci
    otd = tho - tco
  return lmd(itd, otd)


# ---------------------------------------------------------------------

if __name__ == '__main__':

  e = ePhase(3.0)
  print(f"ePhase = {e:0.4g}")

  e = eCounter(0.7, 3.0)
  print(f"eCounter = {e:0.4g}")

  tci, tco, thi, tho = 6, 12, 32, 13
  dt = lmtd(tci, tco, thi, tho, True)
  print(f"lmtd({tci},{tco},{thi},{tho}) = {dt:0.2f} degC")


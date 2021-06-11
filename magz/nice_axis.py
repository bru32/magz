"""
Nice Axis Intervals.
Extracted from Heckbert, Graphic Gems
Bruce Wernick
10 June 2021
"""

import math

nice_intervals = [1.0, 2.0, 2.5, 3.0, 5.0, 10.0, 20.0, 50.0]

def nice_ceil(x):
  if x==0:
    return 0
  if x<0:
    return -1*nice_floor(-1*x)
  z = 10.0 ** math.floor(math.log10(x))
  for i in range(len(nice_intervals) - 1):
    result = z*nice_intervals[i]
    if x<=result:
      return result
  return z*nice_intervals[-1]

def nice_floor(x):
  if x==0:
    return 0
  if x<0:
    return -1*nice_ceil(-1*x)
  z = 10.0 ** (math.ceil(math.log10(x)) - 1.0)
  #r = x / z
  for i in range(len(nice_intervals)-1, 1, -1):
    result = nice_intervals[i] * z
    if x>=result:
      return result
  return z*nice_intervals[0]

def nice_round(x):
  if x==0:
    return 0
  z = 10.0 ** (math.ceil(math.log10(x)) - 1.0)
  #r = x / z
  for i in range(len(nice_intervals) - 1):
    result = z*nice_intervals[i]
    cutoff = 0.5*(result + z*nice_intervals[i+1])
    if x<=cutoff:
      return result
  return z*nice_intervals[-1]

def nice_ticks(lo, hi, ticks=5, inside=False):
  """
  Find nice places to put *ticks* tick marks for numeric data
  spanning from *lo* to *hi*.  If *inside* is True, then the
  nice range will be contained within the input range.  If *inside*
  is False, then the nice range will contain the input range.
  To find nice numbers for time data, use :nice_time_ticks.

  The result is a tuple containing the minimum value of the nice
  range, the maximum value of the nice range, and an iterator over
  the tick marks.

  See also: nice_ticks_seq.
  """
  delta_x = hi - lo
  if delta_x==0:
    if lo == 0:
      return nice_ticks(-1, 1, ticks, inside)
    else:
      return nice_ticks(nice_floor(lo), nice_ceil(hi), ticks, inside)
  #nice_delta_x = nice_ceil(delta_x)
  delta_t = nice_round(delta_x / (ticks - 1))
  if inside:
    lo_t = delta_t * math.ceil(lo / delta_t)
    hi_t = delta_t * math.floor(hi / delta_t)
  else:
    lo_t = delta_t * math.floor(lo / delta_t)
    hi_t = delta_t * math.ceil(hi / delta_t)

  def t_iter():
    t = lo_t
    while t <= hi_t:
      yield t
      t = t + delta_t
  return (lo_t, hi_t, t_iter())

def nice_ticks_seq(lo, hi, ticks=5, inside=False):
  'A convenience wrapper of nice_ticks to return the nice range as a sequence'
  return tuple(nice_ticks(lo, hi, ticks, inside)[2])


# ---------------------------------------------------------------------

if __name__=='__main__':
  for tick in nice_ticks(5.5, 119.0, ticks=10, inside=True)[2]:
    print(tick, end=' ')
  print()

  print(nice_ticks_seq(5.5, 119, ticks=10, inside=True))
  print()

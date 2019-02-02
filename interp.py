"""
Interpolation tools
Bruce Wernick
10 October 2017 15:38:10
"""

__all__ = ['binary_search', 'interp']


def binary_search(dat, key, x):
  """binary search for array of dict.
  x is a ascii text + digits + spaces representing a model name.
  Assumes that the dat is sorted and ascending.
  """
  L = 0
  H = len(dat)-1
  while H-L > 1:
    M = (H+L)//2
    p = dat[M][key]
    if p == x: return M
    if p < x: L = M
    else: H = M
  return M

def interp(a, v):
  "find index of value v in list a"
  if v <= a[0]:
    return 0
  n = len(a)
  if v >= a[n-1]:
    return n-1
  for i in range(1,n):
    if v <= a[i]:
      return i
  return -1



def vector(n, default=0.0):
  return [default for x in range(n)]

def locate(x, p, n):
  'bracketing index of p in list x'
  L = 0
  H = n-1
  ascend = x[H] > x[L]
  while H-L > 1:
    m = (H+L)//2
    if (p >= x[m]) == ascend:
      L = m
    else:
      H = m
  return L, H

def spline(x, y, yp1=1e99, ypn=1e99):

  def interp(p):
    'spline interpolation function'
    L,H = locate(x, p, n)
    dx = x[H]-x[L]
    if dx==0.0:
      raise Exception('interpolation not possible!')
    a = (x[H]-p)/dx
    b = (p-x[L])/dx
    return a*y[L]+b*y[H]+((a*a*a-a)*y2[L]+(b*b*b-b)*y2[H])*(dx*dx)/6.0

  n = len(x)
  u = vector(n)
  y2 = vector(n)
  if yp1 > 0.99e99:
    y2[0] = u[0] = 0.0
  else:
    y2[0] = -0.5
    u[0] = (3.0/(x[2]-x[1]))*((y[2]-y[1])/(x[2]-x[1])-yp1)
  for i in range(1, n-1):
    sig = (x[i]-x[i-1])/(x[i+1]-x[i-1])
    p = sig*y2[i-1]+2.0
    y2[i] = (sig-1.0)/p
    u[i] = (y[i+1]-y[i])/(x[i+1]-x[i])-(y[i]-y[i-1])/(x[i]-x[i-1])
    u[i] = (6.0*u[i]/(x[i+1]-x[i-1])-sig*u[i-1])/p
  if ypn > 0.99e99:
    qn = un = 0.0
  else:
    qn = 0.5
    un = (3.0/(x[n-1]-x[n-2]))*(ypn-(y[n-1]-y[n-2])/(x[n-1]-x[n-2]))
  y2[n-1] = (un-qn*u[n-2])/(qn*y2[n-2]+1.0)
  for k in range(n-2,-1,-1):
    y2[k] = y2[k]*y2[k+1]+u[k]

  return interp


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  print((interp([1,2,3,4,5], 2.25)))

  # create a spline and interpolate
  x = [1.0, 2.0, 3.0, 4.0, 5.0]
  y = [2.0, 8.0, 32.0, 8.0, 2.0]
  fx = spline(x, y)
  print((fx(2.5)))

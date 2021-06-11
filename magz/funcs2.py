"""
2D Math Functions.
Bruce Wernick
10 June 2021
"""

import math

__all__ = ['poly2D', 'polyARI', 'polyXY2', 'polyXY3']


def poly2D(x,y,coeff):
  """2D quadratic with cross-terms
        | - | x | x2|
     ---+---+---+---+
      - | a | b | c |
      y | d | f | g |
      y2| e | h | i |
  """
  a,b,c,d,e,f,g,h,i = coeff
  return a + x*(b + x*c) + y*(d + y*e) + x*y*(f + x*g + y*h + x*y*i)

def polyARI(x,y,coeff):
  """ARI compressor polynomial (upper right corner)
        | - | x | x2| x3|
     ---+---+---+---+---+
      - | a | b | d | g |
      y | c | e | h | - |
      y2| f | i | - | - |
      y3| j | - | - | - |
  """
  a,b,c,d,e,f,g,h,i,j = coeff
  return a + x*(x*(x*g + d) + b) + y*(y*(y*j + f) + c) + x*y*(e + x*h + y*i)

def polyXY2(x,y,coeff):
  """XY quadratic with cross-terms
        | - | x | x2|
     ---+---+---+---+
      - | a | b | d |
      y | c | e | g |
      y2| f | h | i |
  """
  a,b,c,d,e,f,g,h,i = coeff
  return a + x*(b + x*d) + y*(c + y*f) + x*y*(e + x*g + y*h + x*y*i)

def polyXY3(x,y,coeff):
  """XY cubic with cross-terms
        | - | x | x2| x3|
     ---+---+---+---+---+
      - | a | b | d | g |
      y | c | e | h | k |
      y2| f | i | l | n |
      y3| j | m | o | p |
  """
  a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = coeff
  xy = x*y
  z = a
  z += x*(b + x*(d + x*g))
  z += y*(c + y*(f + y*j))
  z += xy*(e + x*(h + x*k) + y*(i + y*m) + xy*(l + x*n + y*o + xy*p))
  return z


# ---------------------------------------------------------------------

if __name__ == '__main__':

  x,y = 1.7, 3.4
  a,b,c,d,e,f,g,h,i,j = 0.1,0.2,0.3,0.4,0.5,0.15,0.25,0.35,0.45,0.55

  z = poly2D(x,y,(a,b,c,d,e,f,g,h,i))
  print(f'poly (2D)     : {z:0.4g}')

  z = polyARI(x,y,(a,b,c,d,e,f,g,h,i,j))
  print(f'poly (ARI)    : {z:0.4g}')

  z = polyXY2(1,1,[1,1,1,1,1,1,1,1,1])
  print(f'polyXY2       : {z:0.4g}')

  z = polyXY3(1,1,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
  print(f'polyXY3       : {z:0.4g}')

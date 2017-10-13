"""
Polynomial tools
Bruce Wernick
10 October 2017 15:38:10
"""

__all__ = ['poly2D', 'polyARI', 'polyeval', 'polydval']


# quadratic
quad = lambda x,*a: a[0] + x*(a[1] + x*a[2])

# cubic
cubic = lambda x,*a: a[0] + x*(a[1] + x*(a[2] + x*a[3]))

def polyMLR3(coeff,x,y):
  "upper triangular coeff"
  a,b,c,d,e,f,g,h,i,j=coeff
  return a+x*(b+x*(d+x*g))+y*(c+y*(f+y*j))+x*y*(e+x*h+y*i)

def poly2DU(a,x,y):
  "ARI type polynomial"
  b=a[1]+x*(a[3]+x*a[6])
  c=a[2]+x*(a[4]+x*a[7])
  d=(a[5]+x*a[8])+y*a[9]
  return a[0] + x*b + y*(c + y*d)

def poly2D(((a,b,c,d,e,f,g,h,i)), x, y):
  "Quadratic in 2D with cross-terms"
  return a + x*(b + x*c) + y*(d + y*e) + x*y*(f + x*g + y*h + x*y*i)

def polyARI((a,b,c,d,e,f,g,h,i,j), x, y):
  "ARI compressor polynomial"
  return a + x*(x*(x*g + d) + b) + y*(y*(y*j + f) + c) + x*y*(e + x*h + y*i)

def polyeval(a, x):
  "polynomial eval using Horner method"
  p = 0.0
  for c in reversed(a):
    p = c + p * x
  return p

def polydval(a, x):
  "polynomial eval, returns f(x) and derivative (df/dx)"
  a.reverse()
  p = a[0]
  q = 0.0
  for c in a[1:]:
    q = p + x*q
    p = c + x*p
  a.reverse()
  return p, q


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  print polyeval([1,2,3],2)
  print polydval([-6,1,1],2) # f=(x-2)(x+3)=-6+x+x2  df=1+2x (at x=2 r=(0,5))



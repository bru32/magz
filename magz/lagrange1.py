"""
1d interpolation by lagrange method
Bruce Wernick
22 September 2017 20:59:31
"""



def lagrange1d(X, Y):
  n = len(X)
  def f(x):
    s = 0.0
    for i in range(n):
      q = 1.0
      for j in range(n):
        if i == j: continue
        q *= (x - X[j]) / (X[i] - X[j])
      s += Y[i] * q
    return s
  return f


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  x = [1,2,3,4,5]
  y = [2,4,6,8,10]
  fx = lagrange1d(x, y)
  print((fx(2.5)))


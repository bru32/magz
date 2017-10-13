"""
Linear Algebra
Bruce Wernick
11 October 2017
"""


def scale_row(A, k, a):
    n = len(A[k])
    for i in range(n): A[k][i]*=a

def scale_vec(b, k, a):
    b[k]*=a

def scale_equations(A, b):
    'to get a maximum magnitude of 1.0'
    r, c = len(A), len(A[0])
    for i in range(r):
        x = abs(A[i][0])
        for j in range(c):
            x = max(x, abs(A[i][j]))
        scale_row(A, i, 1.0/x)
        scale_vec(b, i, 1.0/x)

def locate_pivot_row(A, k):
    'find pivot'
    pivot = abs(A[k][k]); pk = k
    for i in range(k+1, len(A)):
        mag = abs(A[i][k])
        if mag > pivot: pk = i; pivot = mag
    return pk

def madd_rows(A, k, i, a):
    'A[k] = a x A[i]'
    c = len(A[k])
    for j in range(c):
        A[k][j]+=a*A[i][j]

def madd_vec(b, k, i, a):
    b[k]+=a*b[i]

def gauss_jordan(A, b):
    'solve Ax = b by Gauss-Jordan elimination'
    r,c = len(A),len(A[0])
    if r != c: raise IndexError, "A must be square"
    scale_equations(A, b)
    for j in range(r):
        # Select pivot row and make diagonal element unity.
        jpivot = locate_pivot_row(A, j)
        if jpivot > j:
            interchange_rows(A, j, jpivot); interchange_rows(b, j, jpivot)
        pivot = A[j][j]
        if abs(pivot) < 1.0e-15:
            print "Warning: pivot too small:", pivot
        scale_row(A, j, 1.0/pivot); scale_vec(b, j, 1.0/pivot)
        # Now, eliminate all off diagonal elements in the j-th column.
        for i in range(r):
            if i == j: continue
            a = -A[i][j]
            madd_rows(A, i, j, a); madd_vec(b, i, j, a)
    return b

def lin_leastsq(x, y):
    n = len(x)
    sx=sy=sx2=sy2=sxy=0.0
    for i in range(0,n):
        sx += x[i]
        sy += y[i]
        sx2 += x[i]*x[i]
        sy2 += y[i]*y[i]
        sxy += x[i]*y[i]
    A = [[n,sx],[sx,sx2]]
    b = [sy,sxy]
    x = gauss_jordan(A, b)
    a = x[0]
    b = x[1]
    r = (a*sy + b*sxy - (sy*sy)/n) / (sy2 - (sy*sy)/n)
    return x, r


# ------------------------------------------------------------------------------

if __name__ == '__main__':

  x = [1,2,3,4]
  y = [2,4,6.2,8]
  print lin_leastsq(x, y)

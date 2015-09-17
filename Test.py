from scipy import *
def N(i, k):
    gp = array(range(10))
    if (k == 0):
        return (lambda u: 1 if (gp[i-1] <= u < gp[i]) else 0) 
    else:
        return (lambda u: (u - gp[i-1])/(gp[i+k-1]-gp[i-1]) * N(i, k - 1)(u) + 
                (gp[i+k] - u)/(gp[i+k] - gp[i]) * N(i + 1, k - 1)(u))

a = N(2, 1)
print(a(2.5))

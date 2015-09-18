from scipy import *

class Spline(object):
    def __init__(self, gridpoints, coeff):
        self.gp = gridpoints
        self.coeff = coeff

    def __call__(self, u):
        #Find the hot interval
        a = array([gp])
        i = (a > u).argmax()
        
        #Call recursive blossom algorithm
        return blossoms(i, u, 3)

    @classmethod
    def by_points(cls, x, y, gridpoints):
        #PUT UP MATRIX SYSTEM USING HAX0R N FUNC
        #SOLVE DAT SHIT
        return cls(gridpoints, coeff)

    def blossoms(self, i, u, depth):
        if (depth == 0):
            #Base case
            return coeff[i]
        else:
            #Get current alpha
            a = alpha(i, u)
            #Call recursion according to alpha*d[...] + (1 - alpha)*d[...]
            return a * blossoms(i - 1, depth - 1) + (1 - a) * blossoms(i, depth - 1)

    def get_N(self, i, k):
        if (k == 0):
            #N(i, 0)(u), lowest recursive depth
            return (lambda u: 1 if (gp[i-1] <= u < gp[i]) else 0) 
        else:
            #Recursion for N(i, k)(u) according to formula
            return (lambda u: (u - gp[i-1])/(gp[i+k-1]-gp[i-1]) * get_N(i, k - 1)(u) + 
                    (gp[i+k] - u)/(gp[i+k] - gp[i]) * get_N(i + 1, k - 1)(u))

    def alpha(self, i, u):
        #Return alpha according to formula
        return (gp[i+1] - u)/(gp[i+1]-gp[i-2])

from scipy import *
from scipy.linalg import *
import numpy as np

import matplotlib.pyplot as plt

class Spline(object):
    def __init__(self, gridpoints, coeff):
        self.gp = gridpoints
        self.coeff = coeff

    def __call__(self, u):
        #Find the hot interval
        a = array(self.gp)
        i = (a > u).argmax()
        
        #Call recursive blossom algorithm
        return self.blossoms(i, u, 3)

    @classmethod
    def by_points(cls, x, y, gridpoints):
        gp = gridpoints

        xLen = len(x)
        yLen = len(y)
        assert(xLen == yLen) #x and y need to be same size
        assert (gp[0] == gp[1] and gp[1] == gp[2] and gp[-1] == gp[-2] and gp[-2] == gp[-3]) #multiplicity 3 on gridpoints
        m = np.zeros((xLen, yLen)) #initialize matrix
        xi = []
        for j in range(yLen):
            xi.append((gp[j] + gp[j+1] + gp[j+2])/3) #store values for faster access
        for i in range(xLen):

            N = cls.get_N(i, 3, gp)
            for j in range(yLen):
                if (i == 0):
                    xi.append((gp[j] + gp[j+1] + gp[j+2])/3) #store values for faster access
                m[j][i] = N(xi[j])

        #Solve banded needs matrix ab to be in this form
        mbs = np.zeros((7, xLen)) #7 = 3 + 3 + 1 = u + l + 1
        for i in range(7):
            for j in range(xLen):
                if ((i - 3 + j) < 0) or ((i - 3 + j) >= 7):
                    mbs[i, j] = 0
                else:
                    mbs[i, j] = m[i - 3 + j, j]

        #dx = solve_banded((3, 3), mbs, x) #m is banded with bandwidth 4
        #dy = solve_banded((3, 3), mbs, y)
        dx = solve(m, x)
        dy = solve(m, y)
        
        return cls(gridpoints, list(zip(dx, dy)))

    def blossoms(self, i, u, depth):
        if (depth == 0):
            #Base case
            return self.coeff[i]
        else:
            #Get current alpha
            a = self.alpha(i, u)
            #Call recursion according to alpha*d[...] + (1 - alpha)*d[...]
            return tuple(t1 + t2 for t1, t2 in zip(tuple(a * x for x in self.blossoms(i - 1, u, depth - 1)), tuple((1 - a) * x for x in self.blossoms(i, u, depth - 1)))) #Add and multiply don't work on tuples, thus creating new tuples is required
    
    @classmethod
    def get_N(cls, i, k, gridpoints):
        gp = gridpoints
        print(k)
        if (k == 0):
            #N(i, 0)(u), lowest recursive depth
            if (i == 0):
                return (lambda u: 0)
            return (lambda u: 1 if (gp[i-1] <= u <= gp[i]) else 0)
        else:
            #Recursion for N(i, k)(u) according to formula
            iminus1 = i - 1
            if (iminus1 < 0):
                iminus1 = 0
            iplusk = i + k
            if (i + k >= len(gp)):
                iplusk = len(gp) - 1
            d1 = (gp[iplusk-1] == gp[iminus1])
            d2 = (gp[iplusk] == gp[i])
            if d1:
                if d2:
                    return (lambda u: 0)
                else:
                    return (lambda u: (gp[iplusk] - u)/(gp[iplusk] - gp[i]) * cls.get_N(i + 1, k - 1, gp)(u))
            else:    
                if d2:
                    return (lambda u: (u - gp[iminus1])/(gp[iplusk-1]-gp[iminus1]) * cls.get_N(i, k - 1, gp)(u))
                else:
                    return (lambda u: (u - gp[iminus1])/(gp[iplusk-1]-gp[iminus1]) * cls.get_N(i, k - 1, gp)(u) + 
                            (gp[iplusk] - u)/(gp[iplusk] - gp[i]) * cls.get_N(i + 1, k - 1, gp)(u))

    def alpha(self, i, u):
        gp = self.gp
        #Return alpha according to formula

        if (gp[i+2]-gp[i-1]) == 0:
            return 0
        else:
            return (gp[i+2] - u)/(gp[i+2]-gp[i-1])

    def f_range(self,start, stop, step):
        # implementing range() for float type numbers
        i = start
        while i <= stop:
            yield i
            i += step

    def plot(self, h=0.1, dbp = 1): #h is step size, dbp check if you want de Boor points and Control Polygon
        gp = self.gp
        # Generating a list of all evaluation points
        gph = list(self.f_range(gp[0],gp[-1],h))
        evalugph=list(zip(*[self(u) for u in gph]))
       
        if dbp == 1:
            zipcoeff=list(zip(*self.coeff))
            plt.plot(list(zipcoeff[0]),list(zipcoeff[1]))
        plt.plot(list(evalugph[0]),list(evalugph[1]))
        plt.show()  
       
        

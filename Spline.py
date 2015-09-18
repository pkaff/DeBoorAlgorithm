from scipy import *

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

    #@classmethod
    def by_points(cls, x, y, gridpoints):
        gp = self.gp
        assert(x.size == y.size) #x and y need to be same size
        assert(gp[0] == gp[1] and gp[1] == gp[2] and gp[-1] == gp[-2] and gp[-2] == gp[-3]) #multiplicity 3 on gridpoints
        m = zeros((x.size, y.size)) #initialize matrix
        for i in range(x.size):
            N = get_N(i, 3)
            for j in range(y.size):
                if (i == 0):
                    xi.append((gp[i] + gp[i+1] + gp[i+2])/3) #store values for faster access
                m[j][i] = N(xi[j])

        dx = solve_banded((3, 0), m, x) #m is lower triangular with bandwidth 4 (main diagonal + 3 lower diagonals)
        dy = solve_banded((3, 0), m, y)
        
        return cls(gridpoints, list(zip(dx, dy)))

    #@classmethod
    #def get_spline_basis_function(cls, gridpoints)

    def blossoms(self, i, u, depth):
        if (depth == 0):
            #Base case
            if i < 2:
                print(i)
            return self.coeff[i]
        else:
            #Get current alpha
            a = self.alpha(i, u)
            #Call recursion according to alpha*d[...] + (1 - alpha)*d[...]
            return tuple(t1 + t2 for t1, t2 in zip(tuple(a * x for x in self.blossoms(i - 1, u, depth - 1)), tuple((1 - a) * x for x in self.blossoms(i, u, depth - 1)))) #Add and multiply don't work on tuples, thus creating new tuples is requried

    def get_N(self, i, k):
        gp = self.gp
        if (k == 0):
            #N(i, 0)(u), lowest recursive depth
            return (lambda u: 1 if (gp[i-1] <= u < gp[i]) else 0) 
        else:
            #Recursion for N(i, k)(u) according to formula
            return (lambda u: (u - gp[i-1])/(gp[i+k-1]-gp[i-1]) * self.get_N(i, k - 1)(u) + 
                    (gp[i+k] - u)/(gp[i+k] - gp[i]) * self.get_N(i + 1, k - 1)(u))

    def alpha(self, i, u):
        gp = self.gp
        #Return alpha according to formula
        if gp[i+1]-gp[max(i-2,0)] == 0:
            return 0
        else:
            return (gp[i+1] - u)/(gp[i+1]-gp[max(i-2,0)])

    def f_range(self,start, stop, step):
        # implementing range() for float type numbers
        i = start
        while i < stop:
            yield i
            i += step

    def plot(self, h=0.1, dbp = 1): #h is step size, dbp check if you want de Boor points and Control Polygon
        gp = self.gp
        # Generating a list of all evaluation point
        gph = list(self.f_range(gp[0],gp[-1],h))
        evalugph=list(zip(*[self(u) for u in gph]))
       
        if dbp == 1:
            zipcoeff=list(zip(*self.coeff))
            plt.plot(list(zipcoeff[0]),list(zipcoeff[1]))
        plt.plot(list(evalugph[0]),list(evalugph[1]))
        plt.show()  
       
        

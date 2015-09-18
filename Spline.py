import matplotlib.pyplot as plt

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

    def N(self, i, k):
        if (k == 0):
            #N(i, 0)(u), lowest recursive depth
            return (lambda u: 1 if (gp[i-1] <= u < gp[i]) else 0) 
        else:
            #Recursion for N(i, k)(u) according to formula
            return (lambda u: (u - gp[i-1])/(gp[i+k-1]-gp[i-1]) * N(i, k - 1)(u) + 
                    (gp[i+k] - u)/(gp[i+k] - gp[i]) * N(i + 1, k - 1)(u))

    def alpha(self, i, u):
        #Return alpha according to formula
        return (gp[i+1] - u)/(gp[i+1]-gp[i-2])

    def frange(start, stop, step):
        # implementing range() for float type numbers
        i = start
        while i < stop:
        yield i
        i += step

    def plot(self,h,dbp = 0): #h is step size, dbp check if you want de Boor points and Control Polygon
        # Generating a list of all evaluation point
        gph = [lambda i: i for i in frange(self.gp[0],self.gp[len(self.gp)],h]
        #Plotting evaluated list
        plt.plot(self(gph))
        if dbp == true:
            plt.Polygon(coeff)
            plt.plot(coeff)
            
        
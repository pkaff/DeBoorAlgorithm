import unittest
from scipy import *
from Spline import *
#tests
class TestSpline(unittest.TestCase):
        
    #-assert that s(u) = sum(d(u(i)N(i,3)) on the "x" value for a random spline
    def test_equalityX(self):
        #create the test spline
        grid = self.genX(20)
        gp = list(grid)
        coeff = [0.0]*len(gp)
        k = 0
        for i in gp:
            coeff[k] = (i, round(random.random()*15, 2))
            k += 1
        spline = Spline(gp, coeff)
        #test equality
        u = round(random.random()*10, 2)
        s_u = spline(u)
        dN = (0.0, 0.0)
        hi = self.find(spline.gp,round(u, 1))
        for i in range(hi - 2, hi + 1):
            coeff = spline.coeff[i]
            N_u = Spline.get_N(i, 3, spline.gp)(u)
            dN = (dN[0] + coeff[0]*N_u, dN[1] + coeff[1]*N_u)
        
        result = s_u[0]
        expected = dN[0]
        self.assertAlmostEqual(result, expected, 0)
        
    #-same test, but for the "y" value
    def test_equalityY(self):
        #create the test spline
        grid = self.genX(20)
        gp = list(grid)
        coeff = [0.0]*len(gp)
        k = 0
        for i in gp:
            coeff[k] = (i, round(random.random()*15, 2))
            k += 1
        spline = Spline(gp, coeff)
        #test equality
        u = round(random.random()*10, 2)
        s_u = spline(u)
        dN = (0.0, 0.0)
        hi = self.find(spline.gp,round(u, 1))
        for i in range(hi - 2, hi + 1):
            coeff = spline.coeff[i]
            N_u = Spline.get_N(i, 3, spline.gp)(u)
            dN = (dN[0] + coeff[0]*N_u, dN[1] + coeff[1]*N_u)
        
        result = s_u[1]
        expected = dN[1]
        
        self.assertAlmostEqual(result, expected, 0)
        
    def test_polynom(self):
        x_values = [x for x in self.f_range(-10,10,0.1)]
        y_values = [x*x*x + 10*x*x+x+5 for x in self.f_range(-10,10,0.1)]
        print(len(x_values))
        temp = list(x*20-10 for x in random.random(197))
        temp.sort()
        gp_polynomial = [-10,-10, -10]+ temp + [10,10,10]
        s = Spline.by_points(x_values, y_values, gp_polynomial)
        plt.plot(x_values,y_values)        
        (x1,y1) = s.plot() 
        for i in range(len(x_values)):
            self.AssertAlmostEqual(y1[i],y_values[i])
        
    def genX(self, n):
        k = 0.0
        while(k < n):
            yield k
            k += 0.1
    
    def find(self, lst, u):
        k = 0;
        while(lst[k] < u):
            k += 1
        return k
        
    def f_range(self,start, stop, step):
        # implementing range() for float type numbers
        i = start
        while i <= stop:
            yield i
            i += step

    if __name__ == '__main__':
        unittest.main()
        
    

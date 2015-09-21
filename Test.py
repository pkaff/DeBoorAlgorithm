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

    if __name__ == '__main__':
        unittest.main()

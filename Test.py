import unittest
from scipy import *
from Spline import *
#tests
class TestSpline(unittest.TestCase):
    #creates a spline with points 0..9 and corresponding d values randomly distributed in [0,20) 
    def __init__(self):
        gp = array(range(20))
        coeff = [0.0]*10
        for i in range(10):
            coeff[i] = (i, random.random()*20)
        self.spline = Spline(gp, coeff)
        
    #-assert that s(u) = sum(d(u(i)N(i,3))
    def test_equality(self):
        u = 4.7
        s_u = self.spline(u)[1]
        dN = 0.0
        hi = int(floor(u))
        for i in range(hi - 2, hi + 1):
            coeff = self.spline.coeff[i][1]
            N_u = self.spline.get_N(i,3)(u)
            dN += coeff*N_u
        
        result = s_u - dN
        expected = 0.0
        self.assertAlmostEqual(result, expected)
        

    if __name__ == '__main__':
        unittest.main()

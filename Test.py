import unittest
from scipy import *
from Spline import *
#tests
class TestSpline(unittest.TestCase):
    #creates a spline with points 0..9 and d values conforming to 5 - x for testing
    def __init__(self):
        gp = array(range(20))
        coeff = [0.0]*10
        for i in range(10):
            coeff[i] = (i, 5 - i)
        self.spline = Spline(gp, coeff)
        
    #-assert that s(u) = sum(d(u(i)N(i,3))
    def test_equality(self):
        u = 5.0
        s_u = array(self.spline(u))
        dN = array((u, 0.0))
        for i in range(2, len(self.spline.coeff) - 3):
            coeff = self.spline.coeff[i][1]
            N_u = self.spline.get_N(i,3)(u)
            dN[1] += coeff*N_u
        
        print(dN)
        print(s_u)
        result = (0, 0)
        expected = (0, 0)
        self.assertAlmostEqual(result, expected)
            
    #-assert that the extremities of the spline and the extremities of the graph overlap

    if __name__ == '__main__':
        unittest.main()

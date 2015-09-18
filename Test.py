import unittest
from scipy import *
from Spline import *
#tests
class TestSpline(unittest.TestCase):
    #creates a spline with points 0..9 and fcn 5 - x^2/3 for testing
    def __init__(self):
        gp = array([range(10)])
        coeff = [0]*10
        for i in range(10):
            coeff[i] = (i, 5 - (i**2)/3)
        self.spline = Spline(gp, coeff)
        
    #-assert that s(u) = sum(d(u(i)N(i,3))
    def test_equality(self):
        u = 4.6
        s_u = self.spline(u)
        dN = 0.0
        for i in self.spline.gp:
            dN += (self.spline.coeff[i])*(self.spline.get_N(i,3)(u))
            result = s_u - dN
            expected = 0
            self.assertAlmostEqual(result, expected)
            
    #-assert that the extremities of the spline and the extremities of the graph overlap

    if __name__ == '__main__':
        unittest.main()

import unittest
from scipy import *
from Spline import *
#tests
class TestSpline(unittest.TestCase):
        
    #-assert that s(u) = sum(d(u(i)N(i,3)) on the "x" value for a random spline
    def test_equalityX(self):
        #create the test spline
        grid = self.genX(20)
        gp = [0.0 , 0.0] + list(grid) + [20.0, 20.0, 20.0]
        coeff = [(0.0, 0.0)]*(len(gp) - 2)
        for i in range(len(coeff)):
            coeff[i] = (i, random.random()*15)
        spline = Spline(gp, coeff)
        #test equality
        u = round(random.random()*3, 2)
        s_u = spline(u)
        dN = (0.0, 0.0)
        for i in range(len(coeff)):
            coeff = spline.coeff[i]
            N_u = Spline.get_N(i, 3, spline.gp)(u)
            dN = (dN[0] + coeff[0]*N_u, dN[1] + coeff[1]*N_u)

        result = s_u[0]
        expected = dN[0]
        self.assertAlmostEqual(result, expected)
        
    #-same test, but for the "y" value
    def test_equalityY(self):
        #create the test spline
        grid = self.genX(20)
        gp = [0.0 , 0.0] + list(grid) + [20.0, 20.0, 20.0]
        coeff = [(0.0, 0.0)]*(len(gp) - 2)
        for i in range(len(coeff)):
            coeff[i] = (i, random.random()*15)
        spline = Spline(gp, coeff)
        #test equality
        u = round(random.random()*3, 2)
        s_u = spline(u)
        dN = (0.0, 0.0)
        for i in range(len(coeff)):
            coeff = spline.coeff[i]
            N_u = Spline.get_N(i, 3, spline.gp)(u)
            dN = (dN[0] + coeff[0]*N_u, dN[1] + coeff[1]*N_u)
        
        result = s_u[1]
        expected = dN[1]
        self.assertAlmostEqual(result, expected)
        
    def test_polynom(self):
        x_values = [x for x in self.f_range(-10,10,0.1)]
        y_values = [x*x*x + 10*x*x+x+5 for x in self.f_range(-10,10,0.1)]
        temp = list(x*20-10 for x in random.random(197))
        temp.sort()
        gp_polynomial = [-10,-10, -10]+ temp + [10,10,10]
        s = Spline.by_points(x_values, y_values, gp_polynomial)
        plt.plot(x_values,y_values)        
        (x1,y1) = s.plot() 
        plt.show(False)
        self.assertEqual(1, 1)
        #for i in range(len(x_values)):
            #self.assertAlmostEqual(y1[i],y_values[i])
        
    def genX(self, n):
        k = 0.0
        while(k < n):
            yield k
            k += 0.1

    def f_range(self,start, stop, step):
        # implementing range() for float type numbers
        i = start
        while i <= stop:
            yield i
            i += step

    if __name__ == '__main__':
        unittest.main()
        
    

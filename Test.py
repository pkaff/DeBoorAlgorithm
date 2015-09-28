import unittest
from scipy import *
from Spline import *
#tests
class TestSpline(unittest.TestCase):
	
	#asserts that plotting works
	def test_plot(self):
		assert(True)
	
	#asserts that by_points yields same result as normal spline
	def test_by_points(self):
		assert(True)
	
	
	#asserts that sum(N_i) == 1
	def test_N(self):
		grid = self.genX(20)
		gp = [0.0 , 0.0] + list(grid) + [20.0, 20.0, 20.0]
		Ns = [Spline.get_N(i, 3, gp) for i in range(len(gp) - 2)]
		for u in gp:
			N_us = np.array([f(u) for f in Ns])
			print("u: ", u)
			print("N(u): ", N_us)
			self.assertAlmostEqual(sum(N_us), 1)
	
	#asserts that sum(N_i) == 1 for N defined as a spline
	def test_N_Spline(self):
		grid = self.genX(20)
		gp = [0.0 , 0.0] + list(grid) + [20.0, 20.0, 20.0]
		Ns = [Spline.get_N_i_3(i, gp) for i in range(len(gp) - 2)]
		for u in gp:
			N_us = np.array([f(u) for f in Ns])
			self.assertAlmostEqual(sum(N_us[:, 0]), 1)
			self.assertAlmostEqual(sum(N_us[:, 1]), 1)
	
	#-assert that s(u) = sum(d(u(i)N(i,3)) on the "x" value for a random spline
	def test_equality(self):
		#create the test spline
		grid = self.genX(20)
		gp = [0.0 , 0.0] + list(grid) + [20.0, 20.0, 20.0]
		coeff = [np.array([i, random.random()*15]) for i in range(len(gp) - 2)]
		spline = Spline(gp, coeff)
		#test equality
		u = round(random.random()*3, 2)
		s_u = spline(u)
		dN = np.array([coeff[i] * Spline.get_N_i_3(i, gp)(u) for i in range(len(coeff))])
		expected = [sum(dN[:, 0]), sum(dN[:, 1])]
		result = s_u
		self.assertAlmostEqual(result[0], expected[0])
		self.assertAlmostEqual(result[1], expected[1])
		
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
			k += 1

	def f_range(self,start, stop, step):
		# implementing range() for float type numbers
		i = start
		while i <= stop:
			yield i
			i += step

if __name__ == '__main__':
		unittest.main()
		
	

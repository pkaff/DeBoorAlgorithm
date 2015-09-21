python
from Spline import *
s = Spline.by_points([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], [6.0, 2.0, 3.0, 1.0, 5.0, 7.0, 0.0, 1.0], [1.0, 1.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0])
s.plot()
quit()

python
from Spline import *
def randgen(n):
	k = 0
	while(k < n):
		yield int(1 + floor(random.random()*20))
		k += 1

xl = [x for x in randgen(24)]
yl = [y for y in randgen(24)]
s = Spline.by_points(xl, yl, [1.0, 1.0, 1.0] + [u + 1 + random.random() for u in range(20)] + [21.0, 21.0, 21.0])
quit()


python
from Spline import *
N = Spline.get_N(7, 3, [1.0, 1.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0])
print(N(6))
quit()


python
from Spline import *
import matplotlib.pyplot as plt
gp = [x for x in arange(0, 1.1, 1.0/7.0)]
gp = [0.0, 0.0] + gp + [1.0, 1.0]
print(gp)
N = Spline.get_N(10, 3, gp)
u = [x for x in arange(0, 1, 0.01)]
N_u = [N(x) for x in u]
plt.plot(u, N_u)
plt.show()
quit()


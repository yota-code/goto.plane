#!/ur/bin/env python3

import math
import random

class Wind() :
	def __init__(self, spd_average, spd_amplitude, spd_period, way_average, way_amplitude, way_period) :
		# spd in knot
		# way in degrees, as direction from which the wind come
		self.spd_average, self.spd_amplitude, self.spd_period, self.spd_phase = spd_average, spd_amplitude, spd_period, math.tau * random.random()
		self.way_average, self.way_amplitude, self.way_period, self.way_phase = way_average, way_amplitude, way_period, math.tau * random.random()

		self.t_ms = 0

	def step(self, inc_ms) :
		t = self.t_ms / 1000.0

		spd = self.spd_average + self.spd_amplitude * math.sin((t - self.spd_phase) * math.tau / self.spd_period)
		way = self.way_average + self.way_amplitude * math.sin((t - self.way_phase) * math.tau / self.way_period)

		vel = - spd * 1852 / 3600 # in m/s
		psi = math.radians(way) # psi in radian

		y = vel * math.cos(psi) # north
		x = vel * math.sin(psi) # east

		self.t_ms += inc_ms

		return x, y

if __name__ == '__main__' :
	import matplotlib.pyplot as plt

	u = Wind(20, 2.0, 0.0371, 0, 5.0, 0.0713)
	
	x_lst, y_lst = list(), list()
	for i in range(10000) :
		x, y = u.step(1)
		x_lst.append(x)
		y_lst.append(y)

	plt.subplot(3,1,1)
	plt.plot(x_lst)
	plt.subplot(3,1,2)
	plt.plot(y_lst)
	plt.subplot(3,1,3)
	plt.plot(x_lst, y_lst)
	plt.show()
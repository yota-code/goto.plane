#!/usr/bin/env python3

g_earth = 9.807

class Integrator() :
	def __init__(self, x0_prev, y0_init, period_ms) :
		self.x0_prev = x0_prev
		self.y0 = y0_init
		self.period_ms = period_ms

	def step(self, x0_curr) :
		self.y0 += self.period_ms * (x0_curr + self.x0_prev) * 0.5 * 0.001
		self.x0_prev = x0_curr
		return self.y0

class TrajFilt2Sat() :
	def __init__(self, epsilon, omega_zero, sat0, sat1, period_ms) :
		self.epsilon = epsilon
		self.omega_zero = omega_zero

		self.x_ref0 = 0.0
		self.x_ref1 = 0.0
		self.x_ref2 = 0.0

		self.int0 = Integrator(0.0, 0.0, period_ms)
		self.int1 = Integrator(0.0, 0.0, period_ms)

	def step(self, x_com) :

		self.x_ref2 = x_com - self.x_ref1




class Ariplane() :

	def __init__(self, x, y, psi, tas) :
		self.x, self.y, self.psi, self.tas = x, y, psi, tas
	
	def step_psi(self, psi_cmd) :
		pass

	def step_phi(self, phi_cmd) :
		pass

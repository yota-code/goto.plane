#!/usr/bin/env python3

class Ariplane() :

	def __init__(self, x, y, psi, tas) :
		self.x, self.y, self.psi, self.tas = x, y, psi, tas
	
	def step_psi(self, psi_cmd) :
		pass

	def step_phi(self, phi_cmd) :
		pass

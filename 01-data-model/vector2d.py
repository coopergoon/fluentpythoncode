from math import hypot

class Vector(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Vetor(%r, %r)' %(self.x, self.y)

	def __abs__(self):
		return hypo(self.x, self.y)

	def __bool__(self):
		return bool(abs(self))

	def __add__(self):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)
#coding=utf8
from math import hypot


class Vector(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

    def __repr__(self):
        return 'Vetor(%r, %r)' %(self.x, self.y)

    def __abs__(self):
        """
		返回欧几里德范数 sqrt(x*x + y*y)。
		"""
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, num):
        """
		带参数形式
		"""
        x = self.x + num
        y = self.y + num

        # 不带参数形式
		# x = self.x + other.x
		# y = self.y + other.y
		return Vector(x, y)

    def __mul__(self, scalar):
        """
		scalar只是形参
		"""
        return Vector(self.x*scalar, self.y*scalar)

v = Vector(1, 2)
# Vetor(1, 2)
print(v)   # print创建的实例对象，输出的是在__repr__方法下的return内容

# 2.23606797749979
print(abs(v)) # 输出的是__abs__方法下的内容

# True
print(bool(v)) # 返回的是True或者False

# Vetor(5, 6)
print(v+4) # 调用__add__方法，只需使用+，做加法运算

# Vetor(10, 20)
print(v*10) # 调用后__mul__方法，只需使用*,做乘法运算 

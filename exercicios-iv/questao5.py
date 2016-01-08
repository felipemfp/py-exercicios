# Implemente um módulo com:
# - Uma classe Ponto, com coordenadas x, y e z.
# - Uma classe Linha, com dois pontos A e B, e que calcule o comprimento da linha.
# - Uma classe Triangulo, com três pontos A, B e C, que calcule o comprimento dos lados e a área.

class Point(object):
	def __init__(self, x, y, z):
		self.__x = float(x)
		self.__y = float(y)
		self.__z = float(z)
	
	@property
	def x(self):
		return self.__x
	
	@property
	def y(self):
		return self.__y
	
	@property
	def z(self):
		return self.__z
	
	def __repr__(self):
		return "({0:.1f}, {1:.1f}, {2:.1f})".format(self.x, self.y, self.z)
	

class Line(object):
	def __init__(self, a, b):
		self.__a = a
		self.__b = b
	
	@property
	def a(self):
		return self.__a
	
	@property
	def b(self):
		return self.__b
	
	def length(self):
		x = self.b.x - self.a.x
		y = self.b.y - self.a.y
		z = self.b.z - self.a.z		
		return round((x ** 2 + y ** 2 + z ** 2) ** 0.5, 1)
	
	def __repr__(self):
		return "{0} => {1}".format(self.a, self.b)


class Triangle(object):
	def __init__(self, a, b, c):
		self.__a = a
		self.__b = b
		self.__c = c
		
		self.__ab = Line(a, b)
		self.__bc = Line(b, c)
		self.__ca = Line(c, a)
	
	
	def area(self):
		ab = self.__ab.length()
		bc = self.__bc.length()
		ca = self.__ca.length()
		
		# semiperimeter
		sp = (ab + bc + ca) / 2.0
		
		# heron's
		return round((sp * (sp - ab) * (sp - bc) * (sp - ca)) ** 0.5, 1)
	
	def __repr__(self):
		return "{0} => {1} => {2}".format(self.__a, self.__b, self.__c)


if __name__ == "__main__":
	a = Point(2, 3, 1)
	b = Point(5, 1, 4)
	c = Point(4, 2, 5)
	l = Line(a, b)
	t = Triangle(a, b, c)

	print('Ponto A:', a)
	print('Ponto B:', b)
	print('Ponto C:', c)
	print('Linha:', l)
	print('Comprimento:', l.length())
	print('Triangulo:', t)
	print('Area:', t.area())


# Ponto A: (2.0, 3.0, 1.0)
# Ponto B: (5.0, 1.0, 4.0)
# Ponto C: (4.0, 2.0, 5.0)
# Linha: (2.0, 3.0, 1.0) => (5.0, 1.0, 4.0)
# Comprimento: 4.7
# Triangulo: (2.0, 3.0, 1.0) => (5.0, 1.0, 4.0) => (4.0, 2.0, 5.0)
# Area: 3.9
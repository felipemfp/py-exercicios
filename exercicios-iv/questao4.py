# Implementar uma classe Vetor:
# - Com coordenadas x, y e z.
# - Que suporte soma, subtração, produto escalar e produto vetorial.
# - Que calcule o módulo (valor absoluto) do vetor.

class Vector(object):
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
		return "Vector(x={0:.1f}, y={1:.1f}, z={2:.1f})".format(self.x, self.y, self.z)
	
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		z = self.z + other.z
		return Vector(x, y, z)
	
	def __sub__(self, other):
		x = self.x - other.x
		y = self.y - other.y
		z = self.z - other.z
		return Vector(x, y, z)
	
	def __abs__(self):
		return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
	
	def __mul__(self, it):
		if isinstance(it, Vector):
			x = self.y * it.z - it.y * self.z
			y = self.z * it.x - it.z * self.x
			z = self.x * it.y - it.x * self.y
		else:
			x = self.x * float(it)
			y = self.y * float(it)
			z = self.z * float(it)
		return Vector(x, y, z)


if __name__ == "__main__":
	vector = Vector(1, 2, 3)

	print (abs(vector))
	print (Vector(4.5, 5, 6) + vector)
	print (Vector(4.5, 5, 6) - vector)
	print (Vector(4.5, 5, 6) * vector)
	print (Vector(4.5, 5, 6) * 5)


# 3.7416573867739413
# Vector(x=5.5, y=7.0, z=9.0)
# Vector(x=3.5, y=3.0, z=3.0)
# Vector(x=3.0, y=-7.5, z=4.0)
# Vector(x=22.5, y=25.0, z=30.0)
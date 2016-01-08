# Crie uma classe que modele um quadrado, com um atributo lado e os
# métodos: mudar valor do lado, retornar valor do lado e calcular área.

class Square(object):
	def __init__(self, side = 1):
		self.__side = side
	
	@property	
	def side(self):
		return self.__side

	@side.setter
	def side(self, value):
		self.__side = value
	
	@property
	def area(self):
		return self.side ** 2


if __name__ == "__main__":
	square = Square(2)
	print("Valor do lado =>", square.side)
	square.side += square.side
	print("Novo valor do lado =>", square.side)
	print("Aréa do quadrado =>", square.area)


# Valor do lado => 2
# Novo valor do lado => 4
# Aréa do quadrado => 16
# Implemente uma classe Carro com as seguintes propriedades:
# - Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
# - O consumo é especificado no construtor e o nível de combustível inicial é 0.
# - Forneça um método mover(km) que receba a distância em quilômetros e reduza o nível de combustível no tanque de gasolina.
# - Forneça um método gasolina(), que retorna o nível atual de combustível.
# - Forneça um método abastecer(litros), para abastecer o tanque.

class Car(object):
	def __init__(self, fuel_economy, fuel = 0.0):
		self.__fuel_economy = fuel_economy
		self.__fuel = float(fuel)
	
	def move(self, distance):
		quantity = distance / self.__fuel_economy
		if quantity <= self.fuel:
			self.__fuel -= quantity
		else:
			print("You need more fuel")
	
	@property
	def fuel(self):
		return self.__fuel
	
	def supply(self, quantity):
		self.__fuel += quantity


if __name__ == "__main__":
	car = Car(10)
	car.supply(50)
	car.move(40)
	print(car.fuel)


# 46.0
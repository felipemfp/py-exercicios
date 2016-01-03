# Implementar duas funções:
# - Uma que converta temperatura em graus Celsius para Fahrenheit
# - Outra que converta temperatura em graus Fahrenheit para Celsius

def celsius_to_fahrenheit(degrees):
	return 9 / 5 * degrees + 32


def fahrenheit_to_celsius(degrees):
	return (degrees - 32) * 5 / 9


print("Celsius para Fahrenheit (32° C) =>", "{0}° F".format(celsius_to_fahrenheit(32)))
print("Fahrenheit para Celsius (89,6° F) =>", "{0}° C".format(fahrenheit_to_celsius(89.6)))

# Celsius para Fahrenheit (32° C) => 89.6° F
# Fahrenheit para Celsius (89,6° F) => 32.0° C

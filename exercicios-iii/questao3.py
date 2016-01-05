# Implementar um gerador que produza tuplas com as cores do padrão RGB
# (R, G e B variam de 0 a 255) usando xrange() e uma função que produza uma
# lista com as tuplas RGB usando range(). Compare a performance.


def rgb_generator():
	for r in range(256): # equivalente a xrange() no python 2.x
		for g in range(256):
			for b in range(256):
				yield (r, g, b)


def rgb_funtion():
	lst_rgb = []
	for r in list(range(256)): # equivalente a range() no python 2.x
		for g in list(range(256)):
			for b in list(range(256)):
				lst_rgb.append((r, g, b))
	return lst_rgb


if __name__ == "__main__":
	import time
	
	start = time.time()
	lst_rgb = rgb_funtion()
	end = time.time()
	
	print("rgb_funtion() =>", end - start)
	
	start = time.time()
	for color in rgb_generator(): pass
	end = time.time()
	
	print("rgb_generator() =>", end - start)


# rgb_funtion() => 4.183000326156616
# rgb_generator() => 2.8069963455200195
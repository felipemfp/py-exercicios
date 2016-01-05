# Implementar um gerador que leia um arquivo e retorne uma lista de tuplas
# com os dados (o separador de campo do arquivo é vírgula), eliminando as
# linhas vazias. Caso ocorra algum problema, imprima uma mensagem de
# aviso e encerre o programa.


import random


def create_file(filename):
	csv = open(filename, 'w')
	for i in range(5):
		r = []
		for i in range(5):
			r.append('%04d' % random.randrange(1000))
		csv.write(','.join(r) + '\n')
	csv.close()


def read_file(filename):
	try:
		for	line in open(filename):
			line_ = line.strip()
			if line_:
				yield tuple(line_.split(","))
	except:
		print("Sinto muito, mas algo deu errado e não tenho nada a ver com isso.")
		raise SystemExit


if __name__ == "__main__":
	# create_file("data.csv")
	for line in read_file("data.csv"):
		print(line)


# ('0228', '0309', '0166', '0246', '0351')
# ('0206', '0995', '0840', '0798', '0002')
# ('0911', '0735', '0842', '0547', '0589')
# ('0365', '0827', '0529', '0877', '0942')
# ('0344', '0207', '0735', '0186', '0577')
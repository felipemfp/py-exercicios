# Implementar uma função que leia um arquivo e retorne uma 
# lista de tuplas com os dados (o separador de campo do arquivo 
# é vírgula), eliminando as linhas vazias. Caso ocorra algum 
# problema, imprima uma mensagem de aviso e encerre o programa.

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
		lst = []
		for	line in open(filename):
			line_ = line.strip()
			if line_:
				lst.append(tuple(line_.split(",")))
		return lst
	except:
		print("Sinto muito, mas algo deu errado e não tenho nada a ver com isso.")
		raise SystemExit


# create_file("data.csv")
print(read_file("data.csv"))

# [('0101', '0275', '0725', '0200', '0687'), 
#  ('0310', '0837', '0246', '0129', '0970'), 
#  ('0204', '0235', '0646', '0729', '0640'), 
#  ('0950', '0404', '0538', '0014', '0119'), 
#  ('0850', '0552', '0972', '0849', '0287')]
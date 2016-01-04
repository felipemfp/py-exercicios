# Crie um script que:
# - Compare a lista de arquivos em duas pastas distintas.
# - Mostre os nomes dos arquivos que tem conteúdos diferentes e/ou que existem em apenas uma das pastas.

import os


def compare(folder_a, folder_b):

	lst_a = os.listdir(folder_a)
	lst_b = os.listdir(folder_b)
	
	for file in lst_a:
		if file in lst_b:
			if not open(os.path.join(folder_a, file)).read() != open(os.path.join(folder_b, file)).read():
				print(file, "diferente")
		else:
			print(file, "apenas em", folder_a)
	
	for file in lst_b:
		if not file in lst_a:
			print(file, "apenas em", folder_b)


compare("folder1", "folder2")

# target1.txt diferente
# target2.txt apenas em folder1
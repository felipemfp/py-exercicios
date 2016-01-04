# Faça um script que:
# - Leia um arquivo texto
# - Conte as ocorrências de cada palavra
# - Mostre os resultados ordenados pelo número de ocorrências

import re


def read_file(fn):
	target_file = open(fn)
	
	content = target_file.read()
	
	dic_words = {}	
	
	words = set(re.findall("\w+", content))
	
	for word in words:
		dic_words[word] = len(re.findall("(%s)" % word, content))
	
	return sorted(dic_words.items(), key = lambda x: x[1], reverse = True)


for word, count in read_file("target.txt"):
	print(word, "=>", count, "repetição(ões)")

# felipe => 8 repetição(ões)
# freire => 6 repetição(ões)
# pontes => 4 repetição(ões)
# mateus => 2 repetição(ões)

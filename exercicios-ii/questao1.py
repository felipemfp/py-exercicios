# Implementar um programa que receba um nome de arquivo e
# gere estatísticas sobre o arquivo (número de caracteres,
# número de linhas e número de palavras)


def read_file(fn):
	count_chars, count_lines, count_words = 0, 0, 0
	for	line in open(fn).readlines():
		count_lines += 1
		if line:
			count_chars += len(line)
			count_words += len(line.split())
	print("Número de caracteres =>", count_chars)
	print("Número de linhas =>", count_lines)
	print("Número de palavras =>", count_words)


read_file("target.txt")

# Número de caracteres => 139
# Número de linhas => 2
# Número de palavras => 20
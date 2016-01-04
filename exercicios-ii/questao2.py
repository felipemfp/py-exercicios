# Implementar um módulo com duas funções:
# - matrix_sum(*matrices), que retorna a matriz soma de matrizes de duas dimensões.
# - camel_case(s), que converte nomes para CamelCase.

def matrix_sum(*matrices):
	matrix = matrices[0]
	for matrix_ in matrices[1:]:
		for x, row in enumerate(matrix_):
			for y, column in enumerate(row):
				matrix[x][y] += column
	return matrix


def camel_case(text):
	return "".join(text.title().split())


if __name__ == "__main__":
	print(matrix_sum([[1, 2], [3, 4]], [[1, 2], [3, 4]], [[0, 1], [1, 0]]))
	print(camel_case("Nível máximo de respeito"))

# [[2, 5], [7, 8]]
# NívelMáximoDeRespeito
	
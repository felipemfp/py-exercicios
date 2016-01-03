# Implementar uma função que receba uma lista de listas de comprimentos
# quaisquer e retorne uma lista de uma dimensão.

def flatten_list(it):
	if isinstance(it, list):
		union = []
		for list_ in it:
			union += flatten_list(list_)
		return union
	else:
		return [it]


list_a = ["a", "b", "c"]
list_b = ["d", "e"]
list_c = ["f", "g", "h", "i"]
list_d = [list_b, list_c]

print(flatten_list([list_a, list_d]))

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
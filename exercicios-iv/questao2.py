# Crie uma classe derivada de lista com um método retorne os elementos da
# lista sem repetição

class List(list):
	def unique(self):
		return list(set(self))


if __name__ == "__main__":
	old_list = [0, 5, 6, 5]
	new_list = List(old_list)
	print(old_list, new_list.unique())


# [0, 5, 6, 5] [0, 5, 6]
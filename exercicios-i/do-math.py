# Implementar uma função que receba um dicionário e
# retorne a soma, a média e a variação dos valores

def do_math(dic):
	sum_ = sum(dic.values())
	average_ = sum_ / len(dic.values())
	variation_ = max(dic.values()) - min(dic.values())
	return {"Soma": sum_, "Média": average_, "Variação": variation_}


dic = {"a": 20, "b": 10, "c": 30}

print(do_math(dic))

# {'Soma': 60, 'Média': 20.0, 'Variação': 20}
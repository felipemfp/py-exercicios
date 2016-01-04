# Escreva uma função que:
# - Receba uma frase como parâmetro
# - Retorne uma nova frase com cada palavra com as letras invertidas

def reverse_words(phrase):
	new_phrase = ""
	words = phrase.split(" ")
	for	word in words:
		new_phrase += word[::-1] + " "
	return new_phrase.strip()


print(reverse_words("hello world"))

# olleh dlrow
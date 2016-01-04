# Crie uma função que:
# - Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão
#   igual) e um booleano (reverso, falso por padrão)
# - Retorne dados ordenados pelo item indicado pela chave e em ordem
#   decrescente se reverso for verdadeiro

def order_list(tuples, key_ = 0, reverse_ = False):	
	return sorted(tuples, key = lambda x: x[key_], reverse = reverse_)

tuples = [(4, 3), (5, 1), (7, 2), (9, 0)]

print(order_list(tuples))
print(order_list(tuples, reverse_ = True))
print(order_list(tuples, 1))
print(order_list(tuples, 1, True))

# [(4, 3), (5, 1), (7, 2), (9, 0)]
# [(9, 0), (7, 2), (5, 1), (4, 3)]
# [(9, 0), (5, 1), (7, 2), (4, 3)]
# [(4, 3), (7, 2), (5, 1), (9, 0)]
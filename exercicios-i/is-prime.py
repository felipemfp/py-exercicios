# Implementar uma função que retorne verdadeiro se o número for primo 
# (falso caso contrário). Testar de 1 a 100.

def is_prime(number):
	if number < 2: return False
	elif number == 2: return True
	elif number % 2 == 0: return False
	else:
		for x in range(2, number):
			if number % x == 0:
				return False
		else:
			return True

print("Teste com números de 1 a 100")
for x in range(1, 100 + 1):
	print(x, "\t=>", "primo" if is_prime(x) else "não primo")
	
# Teste com números de 1 a 100
#  1    => não primo
#  2    => primo
#  3    => primo
#  4    => não primo
#  5    => primo
#  6    => não primo
#  7    => primo
#  8    => não primo
#  9    => não primo
#  10   => não primo
#  11   => primo
#  12   => não primo
#  13   => primo
#  14   => não primo
#  15   => não primo
#  16   => não primo
#  17   => primo
#  18   => não primo
#  19   => primo
#  20   => não primo
#  21   => não primo
#  22   => não primo
#  23   => primo
#  24   => não primo
#  25   => não primo
#  26   => não primo
#  27   => não primo
#  28   => não primo
#  29   => primo
#  30   => não primo
#  31   => primo
#  32   => não primo
#  33   => não primo
#  34   => não primo
#  35   => não primo
#  36   => não primo
#  37   => primo
#  38   => não primo
#  39   => não primo
#  40   => não primo
#  41   => primo
#  42   => não primo
#  43   => primo
#  44   => não primo
#  45   => não primo
#  46   => não primo
#  47   => primo
#  48   => não primo
#  49   => não primo
#  50   => não primo
#  51   => não primo
#  52   => não primo
#  53   => primo
#  54   => não primo
#  55   => não primo
#  56   => não primo
#  57   => não primo
#  58   => não primo
#  59   => primo
#  60   => não primo
#  61   => primo
#  62   => não primo
#  63   => não primo
#  64   => não primo
#  65   => não primo
#  66   => não primo
#  67   => primo
#  68   => não primo
#  69   => não primo
#  70   => não primo
#  71   => primo
#  72   => não primo
#  73   => primo
#  74   => não primo
#  75   => não primo
#  76   => não primo
#  77   => não primo
#  78   => não primo
#  79   => primo
#  80   => não primo
#  81   => não primo
#  82   => não primo
#  83   => primo
#  84   => não primo
#  85   => não primo
#  86   => não primo
#  87   => não primo
#  88   => não primo
#  89   => primo
#  90   => não primo
#  91   => não primo
#  92   => não primo
#  93   => não primo
#  94   => não primo
#  95   => não primo
#  96   => não primo
#  97   => primo
#  98   => não primo
#  99   => não primo
#  100  => não primo
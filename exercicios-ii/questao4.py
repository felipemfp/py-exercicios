# Implementar um módulo com duas funções:
# - split(fn, n), que quebra o arquivo fn em partes de n bytes 
#   e salva com nomes sequenciais (se fn = arq.txt, então arq_001.txt, arq_002.txt, ... )
# - join(fn, fnlist) que junte os arquivos da lista fnlist em um arquivo só fn.


def split_file(filename, length):
	bytes = list(open(filename, "rb").read())
	name, extension = filename.split(".")
	counter = 0
	while bytes:
		out = bytearray(bytes[:length])
		del bytes[:length]		
		new_file = "{0}_{1:03d}.{2}".format(name, counter, extension)
		open(new_file, "wb").write(out)
		counter += 1


def join_files(filename, files):
	out = []
	for file in files:
		out += list(open(file, 'rb').read())
	open(filename, 'wb').write(bytearray(out))


if __name__ == "__main__":
	import glob
	
	split_file("lorem.txt", 150)
	join_files("lorem2.txt", sorted(glob.glob('lorem_*.txt')))


# lorem_001.txt
# lorem_002.txt
# lorem_003.txt
# lorem_004.txt

# lorem2.txt
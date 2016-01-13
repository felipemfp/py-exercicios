# Implementar uma classe Animal com os atributos: nome, espécie, gênero, peso, altura e idade.
# O objeto derivado desta classe deverá salvar seu estado em arquivo com um método chamado “salvar”
# e recarregar o estado em um método chamado “desfazer”.

import pickle

FORMAT_FILENAME = "{0}.{1}.{2}.ani"

class Animal(object):

    def __init__(self, name = "", specie = "", gender = "", weight = "", height = "", age = ""):
        self.__name = name
        self.__specie = specie
        self.__gender = gender
        self.__weight = weight
        self.__height = height
        self.__age = age

    @property
    def name(self): return self.__name

    @property
    def specie(self): return self.__specie

    @property
    def gender(self): return self.__gender

    @property
    def weight(self): return self.__weight

    @property
    def height(self): return self.__height

    @property
    def age(self): return self.__age

    def __repr__(self):
        return """
Nome    => {0}
Espécie => {1}
Gênero  => {2}
Peso    => {3}
Altura  => {4}
Idade   => {5}
        """.format(self.name, self.specie, self.gender, self.weight, self.height, self.age)

    def save(self):
        filename = FORMAT_FILENAME.format(self.name, self.specie, self.age)
        pickle.dump(self, open(filename, "wb"))
        return filename

    def undo(self, filename):
        loaded = pickle.load(open(filename, "rb"))
        self.__name = loaded.name
        self.__specie = loaded.specie
        self.__gender = loaded.gender
        self.__weight = loaded.weight
        self.__height = loaded.height
        self.__age = loaded.age


if __name__ == "__main__":
    nico = Animal("Nico", "Cachorro", "Macho", "13 Kg", "50 cm", "2 anos")
    print(nico)
    filename = nico.save()
    nico = Animal("Nico", "Gato", "Macho", "7.5 Kg", "25 cm", "3 anos")
    print(nico)
    nico.undo(filename)
    print(nico)


# Nome    => Nico
# Espécie => Cachorro
# Gênero  => Macho
# Peso    => 13 Kg
# Altura  => 50 cm
# Idade   => 2 anos
#
#
# Nome    => Nico
# Espécie => Gato
# Gênero  => Macho
# Peso    => 7.5 Kg
# Altura  => 25 cm
# Idade   => 3 anos
#
#
# Nome    => Nico
# Espécie => Cachorro
# Gênero  => Macho
# Peso    => 13 Kg
# Altura  => 50 cm
# Idade   => 2 anos
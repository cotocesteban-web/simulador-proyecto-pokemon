## importamo ramdom
import random
## el abtractmethhod el contrato que llevaran la hijas
from abc import ABC, abstractmethod
## clase padre
class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.nombre = nombre
        self.__hp_maximo = hp_maximo
        self.__energia_maxima = energia_maxima
        self.__hp_actual = hp_maximo
        self.__energia_actual = energia_maxima
        self.defendiendo = False
## Las propiedades privadas se hacen con Property
    @property
    def hp_actual(self):
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, valor):
        if valor < 0:
            self.__hp_actual = 0
            print("Ha perdido")
        elif valor > self.__hp_maximo:
            self.__hp_actual = self.__hp_maximo
        else:
            self.__hp_actual = valor

    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self, valor):
        if valor < 0:
            self.__energia_actual = 0
        elif valor > self.__energia_maxima:
            self.__energia_actual = self.__energia_maxima
        else:
            self.__energia_actual = valor
## funcion defender
    def defender(self):
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defendiendo = True
            print(f"{self.nombre} se esta defendiendo.")
        else:
            print("No tiene energia suficiente.")
## funcion descansar
    def descansar(self):
        self.energia_actual += 20
        print(f"{self.nombre} descansa y vueleve a recuperar energia. HP acutual{self .hp_actual}")
# funcion que calcula el da;o
    def recibir_dano(self, dano):
        if self.defendiendo:
            dano = dano // 2
            self.defendiendo = False

        self.hp_actual -= dano
        print(f"{self.nombre} recibe {dano} de danio.")
# el metodo abstracto que va a atacar solamente
    @abstractmethod
    def atacar(self, oponente):
        pass

# clase hija
class PokemonAgua(Pokemon):
    # el constructor
    def __init__(self, nombre, hp_maximo, energia_maxima):
        # el super e para que si se ejecute
        super().__init__(nombre, hp_maximo, energia_maxima)
# metodo atacar con obreecitura
    def atacar(self, oponente):
        if self.energia_actual < 15:
            print("No hay energia suficiente.")
            return

        self.energia_actual -= 15
        dano = 10
# El isintnace
        if isinstance(oponente, PokemonFuego):
            dano *= 2
            print("¡Es super efectivo!")

        oponente.recibir_dano(dano)

# clase hija
class PokemonFuego(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)

    def atacar(self, oponente):
        if self.energia_actual < 15:
            print("No hay energia suficiente.")
            return

        self.energia_actual -= 15
        dano = 10

        if isinstance(oponente, PokemonPlanta):
            dano *= 2
            print("¡Es super efectivo!")

        oponente.recibir_dano(dano)

# clase hija
class PokemonPlanta(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)

    def atacar(self, oponente):
        if self.energia_actual < 15:
            print("No tiene energia suficiente")
            return

        self.energia_actual -= 15
        dano = 10

        if isinstance(oponente, PokemonAgua):
            dano *= 2
            print("¡Es efectivo!")

        oponente.recibir_dano(dano)
# clae hija
class PokemonElectrico(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)

    def atacar(self, oponente):
        if self.energia_actual < 15:
            print("No hay energia suficiente.")
            return

        self.energia_actual -= 15
        dano = 10
        ## ramdom escoje en aleatorio

        if random.random() < 0.2:
            print("Paralizado")
            dano = 20

        oponente.recibir_dano(dano)





    



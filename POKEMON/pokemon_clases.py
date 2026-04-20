import pokedex
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.nombre = nombre
        self.__hp_maximo = hp_maximo
        self.__energia_maxima = energia_maxima
        self.__hp_actual = hp_maximo
        self.__energia_actual = energia_maxima
        self.defendiendo = False

    @property
    def hp_actual(self):
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, valor):
        nuevo_valor = valor
        if nuevo_valor < 0:
            nuevo_valor = 0
        if nuevo_valor > self.__hp_maximo:
            nuevo_valor = self.__hp_maximo
        self.__hp_actual = nuevo_valor

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

    def defender(self):
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defendiendo = True
            print(f"{self.nombre} se esta defendiendo.")
        else:
            print("No tiene energia suficiente.")

    def descansar(self):
        self.energia_actual += 20
        print(f"{self.nombre} descansa y recupera energia.")

    def recibir_daño(self, daño):
        if self.defendiendo:
            daño = daño // 2
            self.defendiendo = False
        self.hp_actual -= daño
        print(f"{self.nombre} recibe {daño} de daño.")

    @abstractmethod
    def atacar(self, oponente):
        pass

class PokemonAgua(Pokemon):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        super().__init__(nombre, hp_maximo, energia_maxima)

    def atacar(self, oponente):
        if self.energia_actual < 15:
            print("No hay energía suficiente.")
            return

        self.energia_actual -= 15
        daño = 10

        if isinstance(oponente, PokemonFuego):
            daño *= 2
            print("¡Es súper efectivo!")

        oponente.recibir_daño(daño)

    



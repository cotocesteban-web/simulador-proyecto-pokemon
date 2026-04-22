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
### solo para mostrarlas.
    @property
    def hp_actual(self):
        return self.__hp_actual
## # este bloque garantiza que el hp no supero al maximo o que no sea menor al mininmo.
    @hp_actual.setter
    def hp_actual(self, valor):
        if valor < 0:
            self.__hp_actual = 0
            print("Ha perdido")
        elif valor > self.__hp_maximo:
            self.__hp_actual = self.__hp_maximo
        else:
            self.__hp_actual = valor
### Muestra la energia actual 
    @property
    def energia_actual(self):
        return self.__energia_actual
## # este bloque garantiza que la energia no supero al maximo o que no sea menor al mininmo.
    @energia_actual.setter
    def energia_actual(self, valor):
        if valor < 0:
            self.__energia_actual = 0
        elif valor > self.__energia_maxima:
            self.__energia_actual = self.__energia_maxima
        else:
            self.__energia_actual = valor
## funcion defender: garantiza que la energía nunca sea negativa aunque el coste fuera mayor.
    def defender(self):
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defendiendo = True
            print(f"{self.nombre} se esta defendiendo.")
        else:
            print("No tiene energia suficiente.")
## funcion descansar
    def descansar(self):
        # si el pokemon descansa recupera 20 de energia
        self.energia_actual += 20
        print(f"{self.nombre} descansa y vuelve a recuperar energia. HP actual{self .hp_actual}")
# funcion que calcula el danio: si la funcion self.defendiendo es verdadero el danio se divide ala mitad.
    def recibir_dano(self, dano):
        if self.defendiendo:
            dano = dano // 2
            self.defendiendo = False

        self.hp_actual -= dano
        print(f"{self.nombre} recibe {dano} de danio.")
# el metodo abstracto que va a atacar solamente y todas la hijas las deben de llevar.
    @abstractmethod
    def atacar(self, oponente):
        pass

# clase hija con herencia pokemon
class PokemonAgua(Pokemon):
    # el constructor
    def __init__(self, nombre, hp_maximo, energia_maxima):
       # El super para llamar al constructor de la clase padre
        #Esto asegura que el nombre, la vida y la energía se configuren, sin tener que repetirla.
        super().__init__(nombre, hp_maximo, energia_maxima)
 # Esta es la funcion del metodo abstracto: Sobreescritura del metodo.
    # Define una forma especifica para atacar.
    # Validación: Primero revisa si tiene al menos 15 de energía. Si no, corta la ejecución con un return. 
    def atacar(self, oponente):
        if self.energia_actual < 15:
            print("No hay energia suficiente.")
            return
 # Si tiene energía, le resta esos 15 puntos usando de nuevo el setter
        self.energia_actual -= 15
        # valor base de ataque.
        dano = 10
 ## si el oponente es de fuego el danio se duplica a 2
        if isinstance(oponente, PokemonFuego):
            dano *= 2
            print("¡Es super efectivo!")
# finalmente llama el metodo recibir_danio, ctivando toda la lógica de defensa y salud
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
# Defininedo la clase hija con la Herencia pokemon.
class PokemonElectrico(Pokemon):
    # Este es el constructor
    def __init__(self, nombre, hp_maximo, energia_maxima):
        # El super para llamar al constructor de la clase padre
        #Esto asegura que el nombre, la vida y la energía se configuren, sin tener que repetirla.
        super().__init__(nombre, hp_maximo, energia_maxima)
    # Esta es la funcion del metodo abstracto: Sobreescritura del metodo.
    # Define una forma especifica para atacar.
    # Validación: Primero revisa si tiene al menos 15 de energía. Si no, corta la ejecución con un return. 
    def atacar(self, oponente):
        if self.energia_actual < 15:
            print("No hay energia suficiente.")
            return
         # Si tiene energía, le resta esos 15 puntos usando de nuevo el setter
        self.energia_actual -= 15
        dano = 10

        ## ramdom escoje en aleatorio
        ## Introduce un elemento de azar donde, 1 de cada 5 veces, el ataque será más potente y mostrará un mensaje de "Paralizado"
        if random.random() < 0.2:
            print("Paralizado")
            dano = 20
     # finalmente llama el metodo recibir_danio
        oponente.recibir_dano(dano)





    



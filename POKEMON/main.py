import random
import pokedex
from pokemon_clases import PokemonFuego, PokemonAgua, PokemonPlanta, PokemonElectrico

def crear_pokemon(opcion):
    
    ##Creamos una instancia de un Pokemon basada en la opción seleccionada.
    
    # Convertimos a string por si acaso, ya que las llaves en pokedex.py son "1", "2", etc.
    opcion_str = str(opcion)
    
    if opcion_str in pokedex.CATALOGO_POKEMON:
        datos = pokedex.CATALOGO_POKEMON[opcion_str]
        tipo = datos["tipo"]
        nombre = datos["nombre"]
        hp = datos["hp_maximo"]
        en = datos["energia_maxima"]

        # Instanciamos la clase correcta según el tipo
        if tipo == "Fuego":
            return PokemonFuego(nombre, hp, en)
        elif tipo == "Agua":
            return PokemonAgua(nombre, hp, en)
        elif tipo == "Planta":
            return PokemonPlanta(nombre, hp, en)
        elif tipo == "Electrico":
            return PokemonElectrico(nombre, hp, en)
    else:
        print(f"La opción {opcion_str} no es válida.")
        return 


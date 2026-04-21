import random
import pokedex
from pokemon_clases import PokemonFuego, PokemonAgua, PokemonPlanta, PokemonElectrico
### aca cramos el pokemon: 
def crear_pokemon(opcion):
    opcion = input("Selecciona: ")
    if opcion.isdigit():
        opcion = int(opcion)
    
    if opcion in pokedex.CATALOGO_POKEMON:
        ### aca accedo a los datos del pokemon que esta en el catalogo
        datos = pokedex.CATALOGO_POKEMON[opcion]
        tipo = datos["tipo"]
        nombre =datos["nombre"]
        hp = datos["hp_maximo"]
        energia_max = datos["energia maxima"]

        #
    if tipo == "Fuego":
        return PokemonFuego(nombre, hp, energia_max)
    elif tipo == "Agua":    
        return PokemonAgua(nombre, hp, energia_max)
    elif tipo == "Planta":
        return PokemonAgua(nombre, hp, energia_max)
    elif tipo == "Electrico":
        return PokemonElectrico(nombre, hp, energia_max)
    else:
        print(f"La opcion {opcion} no es valida.")
        return
    
def jugar():
        ## mostrar los modos de juego al usuario:
        print("1. Jugador vs Jugador")
        print("2. Jugador vs Computadora")
        modo = input("Porfavor Seleccione el modo de juego: ")
        # mostrar el catalogo diponibles de pokemones imprimiendo en pantala:
        pokedex.mostrar_catalogo_disponible()
     
        # hacemos las comparaciones segun el modod de juego elegido por el usuario:
        if modo == "2":
            # si ingresso la opcion 2. puede seleccionar su personaje.



    

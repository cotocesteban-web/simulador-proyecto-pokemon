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
        nombre = datos["nombre"]
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
            eleccion_jugador = input ("elige el numeronde tu Pokemon: ")
            jugador = crear_pokemon(eleccion_jugador)

            selecion_compu = random.randrange(1,8)
            computadora = crear_pokemon(selecion_compu)

            if not jugador or not computadora:
                print("Erron en la seleccion.")
                return
            print(f"\n{jugador.nombre} VS {computadora.nombre} (computadora)")

        ### iniciar un bucle para hacer valido que el hp no sea 0
        while jugador.hp_actual > 0 and computadora.hp_actual > 0:
            # Mostrar el turno de jugador
            print(f"\n Turno de {jugador.nombre}")
            accion = input("Que accion deseas hacer?")

            if accion == "1":
                jugador.atacar(computadora)

            else:
                print("opcion invalida, espera nuevamente el turno")

        
           
        
    






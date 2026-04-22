### ** Este es el archivo Main (Principal) hara que ejecute todo lo que hemo llevado con los dos archivos
## Importamos ramdom para que nos elija un numero aleatorio del rando que le indiquemos.
import random
# Importar el pokedex que es donde esta el diccionario de todo los pokemones con sus caracteristicas:
import pokedex
# De pokemon clases importamos especificamente los pokemones.
from pokemon_clases import PokemonFuego, PokemonAgua, PokemonPlanta, PokemonElectrico

### aca creamos el pokemon: 
def crear_pokemon(opcion):

    opcion = str(opcion)
    
    if opcion in pokedex.CATALOGO_POKEMON:
        ### aca accedo a los datos del pokemon que esta en el catalogo
        datos = pokedex.CATALOGO_POKEMON[opcion]
        tipo = datos["tipo"]
        nombre = datos["nombre"]
        hp = datos["hp_maximo"]
        energia_max = datos["energia_maxima"]

        #
        if tipo == "Fuego":
            return PokemonFuego(nombre, hp, energia_max)
        elif tipo == "Agua":    
            return PokemonAgua(nombre, hp, energia_max)
        elif tipo == "Planta":
            return PokemonPlanta(nombre, hp, energia_max)
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
    # eleccion de los personajes
     ## Ete e el modo jugador vs Jugador
    if modo == "1":
        eleccion1 = input("Jugador 1, elije el numero de tu Pokemon: ")
        jugador = crear_pokemon(eleccion1)
        eleccion2 = input("Jugador 2, elige el numero de tu Pokemon; ")
        jugador2 = crear_pokemon(eleccion2)
    # Jugador vs computadora:
    elif modo == "2":
        # Jugador vs computadora:
        eleccion1 = input("Elije el numero de tu Pokemon: ")
        jugador = crear_pokemon(eleccion1)
        # Seleccion Aleatoria por random:
        eleccion_pc = str(random.randint(1, 8))
        jugador2 = crear_pokemon(eleccion_pc)

    else: 
        print("Modo invalido")

        ## Mostrar oponente en los mensajes
    if modo =="1":
        rival = "(Jugador vs jugador)"
    else:
        rival = "(Jugador vs Pc)"

    print(f"\n {jugador.nombre} vs {jugador2.nombre} {rival}")

    ## Comienzan las batallas mientra que ambos tengan vida
    while jugador.hp_actual > 0 and jugador2.hp_actual > 0:

        ## Turno del jugador 1;:
        print(f"\n Turno de {jugador.nombre} ")
        print(f" HP {jugador.hp_actual} | Energia: {jugador.energia_actual}")
        accion = input("Selecciona (1. Atacar, 2.Defender, 3.Descansar:)")

        if accion == "1":
            jugador.atacar(jugador2)
        elif accion == "2":
            jugador.defender()
        elif accion == "3":
            jugador.descansar()

        else:
            print("Opcion invalida, pierdes el turno: ")


            ## Verificar el estado del Jugador 2\
        if jugador2.hp_actual <= 0:
            print(f"\2 {jugador.nombre} Ha ganado la batalla")
            break

             # turno del jUGADOR 2
        print(F"\n  Turno de {jugador2.nombre} {rival} ")
        print(f"Hp {jugador2.hp_actual} | Energia:{jugador2.energia_actual}")
        
        if modo == "1":
            ## el Jugador2
            accion2 = input("Selecciona(1. Atacar, 2.Defender, 3.Decansar):")
            if accion2 == "1":
                jugador2.atacar(jugador)
            elif accion2 == "2":
                jugador2.defender()
            elif accion2 =="3":
                jugador2.descansar()
            else:
                print("Opcion invalida, pierdes turno")
            # Si es computadora;
        else: 
            accion_pc_eleccion = random.choice(["atacar", "atacar", "descansar"])
            if accion_pc_eleccion == "atacar":
                jugador2.atacar(jugador)

            else:
                jugador2.descansar()

            ## verificar i el jugador 1 murio:
        if jugador2.hp_actual <= 0:
          print(f"\n {jugador2.nombre} {rival} ha ganado la batalla")
  

if __name__ == "__main__":
    jugar()   



    


        
           
        
    






import random

def salida():
    salir = """
                    ¡¡¡Vuelve Pronto!!!

        "Juego el numero 30" creador: chris-developer
        """
    return salir


def menu():
    menu = """
                ¡¡¡Bienvenido Al Juego!!!

                     "El Numero 30"


                1. Ver reglas del juego.
                2. Iniciar Juego.
                3. Salir
"""
    return menu


def menu2():
    menuInicio = """
                    "Inicio Del Juego"


                    1. Jugador1 Vs Jugador2.
                    2. Jugador1 Vs Pc.
                    3. volver al Menu.     
    """
    return menuInicio


def reglas():
    reglas = """
                        ¡¡¡Reglas del Juego!!!

        1. Modo de juego (Jugador Vs Jugador o Jugador Vs Pc).
        2. El Juego escogera aleatoriamente que jugador comenzara.
        3. El primer jugador que llegue a 30 gana la partida.
        4. El jugador solo puede digitar un numero de 1 a 3.
        5. En cada turno el jugador solo podra digitar un numero.
    """
    return reglas


def inicio(): 
    print(menu())
    while True:
        try: 
            opcion = int(input(f"Digite una Opción: "))
            break
        except:
            print("¡Error! **Digite una opcion en numeros**\n")
    print("")
    while opcion != 1 and opcion != 2 and opcion != 3:
        print("¡Error! digite una opcion de 1 a 3\n")
        opcion = int(input(f"Digite una Opción: "))
    if opcion == 1:
        print(reglas())
        while True:
            try:
                paso = int(input("Digite 1 para volver al menu: "))
                break
            except:
                print("¡Error! Digite el numero 1")
        while paso != 1:
            print("¡Error! Digite el numero 1")
            paso = int(input("Digite 1 para volver al menu: "))
        print(inicio())
        
    elif opcion == 2:
        while True:
            try:
                dato = int(input(f"{menu2()}\nDigite una opcion: "))
                break
            except:
                print("¡Error! **Digite una opcion en numeros**\n")
        if dato == 1:
            print(juego())
        elif dato == 2:
            print(juegoPc())
        else:
            print(inicio())
            
            
    return salida()
            
           
def juego():
    print("")
    print("*Ingrese el nombre de los jugadores*\n")
    jugador1 = input("Jugador # 1: ")
    jugador2 = input("Jugador # 2: ")
    print("") 
    turno = random.randint(1,2)
    print(f"!!!El jugador que comienza es el jugador # {turno}!!!\n")
    contador = 0
    if turno == 1:
        while contador < 30:
            while True:
                try:
                    dato1 = int(input(f"Digite numero {jugador1}: "))
                    break
                except:
                    print("Digite solo valores numericos")
            while dato1 != 1 and dato1 != 2 and dato1 != 3:
                print(f"Dato incorecto {jugador1} (Digite un numero del 1 al 3)")
                dato1 = int(input(f"Digite numero {jugador1}: "))
            contador += dato1
            print(contador)
            if contador == 30:
                print(f"El ganador es el jugador {jugador1} ")
                break
            while True:
                try:
                    dato2 = int(input(f"Digite numero {jugador2}: "))
                    break
                except:
                    print("Digite solo valores numericos")
            while dato2 != 1 and dato2 != 2 and dato2 != 3:
                print(f"Dato incorecto {jugador2} (Digite un numero del 1 al 3)")
                dato2 = int(input(f"Digite numero {jugador2}: "))
            contador += dato2
            print(contador)
            if contador == 30:
                print(f"El ganador es el jugador: {jugador2}")
                break
    else: 
        while contador < 30:
            while True:
                try:
                    dato2 = int(input(f"Digite numero {jugador2}: "))
                    break
                except:
                    print("Digite solo valores numericos")
            while dato2 != 1 and dato2 != 2 and dato2 != 3:
                print(f"Dato incorecto {jugador2} (Digite un numero del 1 al 3)")
                dato2 = int(input(f"Digite numero {jugador2}: "))
            contador += dato2
            print(contador)
            if contador == 30:
                print(f"El ganador es el jugador: {jugador2}")
                break
            while True:
                try:
                    dato1 = int(input(f"Digite numero {jugador1}: "))
                    break
                except:
                    print("Digite solo valores numericos")
            while dato1 != 1 and dato1 != 2 and dato1 != 3:
                print(f"Dato incorecto {jugador1} (Digite un numero del 1 al 3)")
                dato1 = int(input(f"Digite numero {jugador1}: "))
            contador += dato1
            print(contador)
            if contador == 30:
                print(f"El ganador es el jugador {jugador1}")
                break
    return salida()
        

def juegoPc():
    print("")
    print("*Ingrese el nombre del jugador*\n")
    jugador2 = "Pc"
    jugador1 = input("Jugador # 1: ")
    print(f"Jugador # 2: {jugador2}\n")
    turno = random.randint(1,2)
    print(f"El jugador que comienza es el jugador # {turno}\n")
    contador = 0
    if turno == 1:
        while contador < 30:
            while True:
                try:
                    dato1 = int(input(f"Digite numero {jugador1}: "))
                    break
                except:
                    print("Digite solo valores numericos")
            while dato1 != 1 and dato1 != 2 and dato1 != 3:
                print(f"Dato incorecto {jugador1} (Digite un numero del 1 al 3)")
                dato1 = int(input(f"Digite numero {jugador1}: "))
            contador += dato1
            if contador >= 30:
                print(f"El ganador es el jugador {jugador1} ")
                break
            
            dato2 = random.randint(1, 3)
            print(f"Numero de {jugador2}: {dato2}")
            contador += dato2
            if contador == 30:
                print(f"El ganador es el jugador: {jugador2}")
                break
    else: 
        while contador < 30:
            dato2 = random.randint(1, 3)
            print(f"Numero de {jugador2}: {dato2}")
            contador += dato2
            if contador >= 30:
                print(f"El ganador es el jugador: {jugador2}")
                break
            while True:
                try:     
                    dato1 = int(input(f"Digite numero {jugador1}: "))
                    break
                except:
                    print("Digite solo valores numericos")
            while dato1 != 1 and dato1 != 2 and dato1 != 3:
                print(f"Dato incorecto {jugador1} (Digite un numero del 1 al 3)")
                dato1 = int(input(f"Digite numero {jugador1}: "))
            contador += dato1
            if contador == 30:
                print(f"El ganador es el jugador {jugador1}")
                break
    return inicio()



if __name__ == '__main__':
    inicio()
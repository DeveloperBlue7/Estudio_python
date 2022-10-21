import random

def menu():
    menu = """
        ¡¡¡Bienvenido Al Juego!!

            "EL NUMERO 30" 

    1. Ver reglas del juego
    2. Iniciar Juego
    3. Salir Del Juego
    """
    return menu
    

def reglas():
    reglas = """
                    ¡¡¡Reglas del Juego!!!

    1. tener conocimiento de las reglas de juego.
    2. El Juego escogera aleatoriamente que jugador comenzara.
    3. El primer jugador que llegue a 30 gana la partida.
    4. El jugador solo puede digitar un numero de 1 a 3.
    5. En cada turno el jugador solo podra digitar un numero.
    """
    return reglas


def juego():
    print("")
    print("*Ingrese el nombre de los jugadores*\n")
    jugador1 = input("Jugador # 1: ")
    jugador2 = input("Jugador # 2: ")
    print("¡¡¡JUGADOR QUE COMIENZA!!!\n") 
    turno = random.randint(1,2)
    print(turno)
    contador = 0
    if turno == 1:
        while contador < 30:
            dato1 = int(input(f"Digite numero {jugador1}: "))
            while dato1 != 1 and dato1 != 2 and dato1 != 3:
                print(f"Dato incorecto {jugador1} (Digite un numero del 1 al 3)")
                dato1 = int(input(f"Digite numero {jugador1}: "))
            contador += dato1
            print(contador)
            if contador == 30:
                print(f"El ganador es {jugador1} ")
                break
            
            dato2 = int(input(f"Digite numero {jugador2}: "))
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
            dato2 = int(input(f"Digite numero {jugador2}: "))
            while dato2 != 1 and dato2 != 2 and dato2 != 3:
                print("Digite un numero de 1 al 3")
                dato2 = int(input(f"Digite numero {jugador2}: "))
            contador += dato2
            print(contador)
            if contador == 30:
                print(f"El ganador es es jugador: {jugador2}")
                break
            dato1 = int(input(f"Digite numero {jugador1}: "))
            while dato1 != 1 and dato1 != 2 and dato1 != 3:
                print("Digite un numero de 1 al 3")
                dato1 = int(input(f"Digite numero {jugador1}: "))
            contador += dato1
            print(contador)
            if contador == 30:
                print(f"El ganador es el jugador {jugador1}")
                break
    return inicio()
        
        
def inicio(): 
    opcion = int(input(f"{menu()}\nDigite una Opción: "))
    if opcion == 1:
        print(reglas())
        paso = int(input("Digite una opcion:\n\n1. Comenzar el juego\n2. Para salir\n"))
        if paso == 1:
            print(juego())
        else:
            print("¡¡¡Vuelve pronto!!!")
    elif opcion == 3:
        pass
    else:
        print(juego())
    return """
        "Juego el numero 30"

    creador: chris-developer
    """

    
def prueba():
    num = random.randint(1,100)
    return(num)




if __name__ == '__main__':
    inicio()
    #prueba()
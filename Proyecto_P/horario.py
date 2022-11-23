problema = """
                        *****Horario de Clases*****

        Se solicita un algoritmo donde cada estudiante pueda registrar
        sus materias con el dia, la hora de la materia como tambien
        el nombre de la asignatura, se debera poder editar el horario
        si el estudiante comete errores, tambien se busca poder ver el
        horario por dia de la semana como tambien poder imprimir todo
        el horario completo.
    """
print(problema)

horario = {
    "Lunes":
    {  
    },
    "Martes":
    {   
    },
    "Miercoles":
    {
    },
    "Jueves":
    {  
    },
    "Viernes":
    {  
    },
}

def menu():
    menu = """
                    *****Horario de clases*****

                    Menu:
                    1. Ingreso de materias
                    2. Consultar Horario
                    3. Imprimir horario"""

    opcion = int(input(f"{menu}\n\nDigite una Opcion => "))
    if opcion == 1:
        print(inicio())
    if opcion == 2:
        print(consultar())
    if opcion == 3:
        print(imprimir())
    return menu


def ingresom():
    ing = """
                ***Ingreso Materias***


                    1. Lunes
                    2. Martes
                    3. Miercoles
                    4. Jueves
                    5. Viernes

    """
    return ing   
   

def inicio():
    global dia
    global day
    global l
    dia = int(input(f"{ingresom()}\nDigite el numero del dia: "))
    print("")
    while dia != 1 and dia != 2 and dia != 3 and dia != 4 and dia != 5:
        print("¡¡¡Error!!! Digite un numero de (1 a 5)")
        dia = int(input("Digite el numero del dia: \n\n1. Lunes\n2. Martes\n3. Miercoles\n4. Jueves\n5. Viernes\n\n"))
    if dia == 1:
        day = "Lunes"
        l = "Lunes"
        print(proceso())
    if dia == 2:
        day = "Martes"
        l = "Martes"
        print(proceso())
    if dia == 3:
        day = "Miercoles"
        l = "Miercoles"
        print(proceso())
    if dia == 4:
        day = "Jueves"
        l = "Jueves"
        print(proceso())
    if dia == 5:
        day = "Viernes"
        l = "Viernes"
        print(proceso())
    

def proceso():
    print(f"El dia escogido fue {day}\n")
    materia = int(input("¿Cuantas materias quiere Registrar? => "))
    print("")
    conteo = 0
    while conteo < materia:
        for i in range(1, materia +1):
            key = f" Clase # {i} "
            values = input(f"Digite la Hora (Ejemplo las 6:00AM)\n\nHora De La Clase # {i} : ")
            horario[l][key] = values
            key = f"Materia # {i} "
            values = input(f"Digite el Nombre de La materia # {i}: ")
            horario[l][key] = values
            conteo += 1
    print("\n***Horario Guardado correctamente***")
    return(menu())


def consultar():
    dato = input(f"Digite el dia del horario que quiere ver: ").capitalize()
    print(f"\n              Horario de clases del {dato}:\n")
    for c, d in horario[dato].items():
        print(f"                {c}: {d}\n")
    paso1 = input(f"            Quiere corregir su horario del {day}?\n\n(Digite 1 para Si o 2 Para NO)\n")
    if paso1 == "1":
        print(proceso())
    return menu()
    

def imprimir():
    print("             *****Horario De Clases*****")
    print("         Lunes:")
    for c, d in horario["Lunes"].items():
        print(f"\n                {c}: {d}\n")
    print("         Martes:")
    for c, d in horario["Martes"].items():
        print(f"\n                {c}: {d}\n")
    print("         Miercoles:")
    for c, d in horario["Miercoles"].items():
        print(f"\n                {c}: {d}\n")
    print("         Jueves:")
    for c, d in horario["Jueves"].items():
        print(f"\n                {c}: {d}\n")
    print("         Viernes:")
    for c, d in horario["Viernes"].items():
        print(f"\n                {c}: {d}\n")    

    return menu()


if __name__ == '__main__':
    menu()
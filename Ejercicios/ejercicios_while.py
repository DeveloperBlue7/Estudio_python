# Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).

def run1():
    print("Digite sí para continuar\n")
    respuesta = input("Desea continuar con el programa?: ")
    while respuesta == "sí":
        respuesta = input("Desea continuar con el programa?: ")
    
    print("Hasta La Vista")

# Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta exactamente SI (en mayúsculas y sin tilde).

def run2():
    print("Digite SI para terminar\n")
    respuesta = input("Desea Terminar el programa?: ")
    while respuesta != "SI":
        respuesta = input("Desea Terminar el programa?: ")
    print("Programa Terminado")

# Escriba un programa que pregunte una y otra vez si desea terminar el programa, siempre que se conteste exactamente N (en mayúsculas).

def run3():
    print("¡¡¡Digite N para terminar el programa!!!")
    respuesta =  input("Desea terminar el programa: ")
    while respuesta != "N":
        respuesta =  input("Desea terminar el programa: ")
    print("Programa Terminado")

# Escriba un programa que pregunte una y otra vez si desea continuar el programa, salvo si se contesta exactamente no (en minúsculas).

def run4():
    print("Escriba no para terminar")
    pregunta = input("Desea continuar el programa?:\n")
    while pregunta != "no":
        pregunta = input("Desea continuar el programa?:\n")
    print("Programa Terminado")
        
# Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste S o s (en mayúsculas o en minúsculas).

def run5():
    print("Digite S o s para Continuar")
    respuesta = input("Desea continuar con el programa?:\n")
    while respuesta == "S" or respuesta == "s":
        respuesta = input ("Desea continuar con el programa?:\n")
    print("!!!Programa Terminado¡¡¡")


# Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta S o s (en mayúsculas o en minúsculas).

def run6():
    print("Digite S O s si desea continuar")
    respuesta = input("Desea terminar el programa?:\n")
    while respuesta != "S" and respuesta != "s":
        respuesta = input("Desea terminar el programa?:\n")
    print("PROGRAMA TERMINADO")


# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.

def run7():
    contraseña = input("Digite La Contraseña:\n")
    confirmación = input("Confirme La Contraseña:\n")
    while contraseña != confirmación:
        print("Las Contraseñas No Conciden")
        contraseña = input("Digite La Contraseña\n")
        confirmación = input("Confirme La Contraseña\n")
    print("Contraseñas Correctas ¡¡¡Bienvenido!!!")


# Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las cantidades sean positivas.

def run8():
    ahorro = int (input("Cuanto desea ahorrar?\n"))
    cantidad = int(input("Ingrese la cantidad para el ahorro: "))
    while ahorro > cantidad:
        cantidad += int(input("Ingrese la cantidad para el ahorro: "))
        print(cantidad)
    print(f"la cantidad ahorrada es {cantidad}")


# Escriba un programa que mejore la simulación de la hucha del ejercicio anterior, no permitiendo que se escriban cantidades negativas.

def run9():
    ahorro = int (input("Cuanto desea ahorrar?\n"))
    
    while ahorro <= 0:
        print("error!! digite cantidades positivas")
        ahorro = int (input("Cuanto desea ahorrar?\n"))

    cantidad = 0  

    while ahorro > cantidad:
        ingreso = int(input("Ingrese la cantidad para el ahorro: "))
        if ingreso <= 0:
            print("error!! digite cantidades positivas")
        else:
            cantidad += ingreso  
    print(f"¡¡¡FELICITACIONES CUMPLISTE TU META¡¡¡la cantidad ahorrada es {cantidad}")


# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.
print("Bienvenido A BlueSystem")


def run10():
    menu ="""

    Ingrese Su Contraseña:"""
    contraseña = "Lobo21"
    conteo = 0
    intento = 3
    while conteo < 3:
        opcion = input(menu + "\n")
        if opcion != contraseña:
            intento -= 1
            print(f"¡¡¡Error!!! le quedan {intento} intentos ")
        else:
            print("bienvenido A BlueSystem Christian\n")
            print("Comenzamos inicio de sistema operativo Lord")
            break;
        conteo +=1
    if conteo == 3:
        print("Sistema Bloqueado, Se envio una alerta al administrador")




if __name__ == '__main__':
    run10()



    

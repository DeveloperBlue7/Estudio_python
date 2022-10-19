# ciclo while

# def run():
#     LIMITE = 10
#     contador = 0
#     potencia = 2** contador
#     while contador < LIMITE:
#         potencia = 2 ** contador
#         print(f" 2 elevado a  {contador} es igual a : {potencia}")
#         contador = contador + 1 
        

def pez():
    contador =0
    
    while contador < 11:
        multiplicacion = 2 * contador   
        print(f"2 x {contador} = {multiplicacion}")
        contador += 1


def ingreso(intento, intentos):
    contraseña = "Kaleb2121"
    conteo = 0
    print("¡¡¡Bienvenido A BlueSystem!!!")
    while conteo < intento:
        respuesta = input(f"Ingrese su contraseña: tienes {intentos} intentos: ")
        if respuesta != contraseña:
            intentos = intentos - 1
            print("Contraseña Incorrecta")
            conteo += 1 
        else:
            print("Bienvenido A System")
            break;



if __name__ == '__main__':
    pass


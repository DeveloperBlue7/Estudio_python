import random
import string


def generador_contraseña():
    print("-----Generador De Contraseñas-----")
    numero_caracteres = int(input("Digite el numero de caracteres que quiere para su contraseña: "))
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "X", "y", "z"]  
    simbolos = ["!", "¡", "#", "$", "%", "&", "/", "(", ")", "=", "?", "¿", "+", "-", "*", "{", "}", "[", "]", ".", ",", ":", ";", "<", ">"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    caracteres = mayusculas + minusculas + simbolos + numeros 


    contrasena = []

    for d in range(numero_caracteres):
        caracteres_aleatorios = random.choice(caracteres)
        contrasena.append(caracteres_aleatorios)

    contrasena = "".join(contrasena)   

    return contrasena 


def generador_contraseña1():
    print("-----Generador De Contraseñas-----")
    
    numero_caracteres = int(input("Digite el numero de caracteres que quiere para su contraseña: "))
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    contrasena = []

    for d in range(numero_caracteres):
        caracteres_aleatorios = random.choice(caracteres)
        contrasena.append(caracteres_aleatorios)

    contrasena = "".join(contrasena)   
    return contrasena 


def run():
    contrasena = generador_contraseña1()
    print(f"Su nueva contraseña es: {contrasena}")



if __name__ == '__main__':
    run()


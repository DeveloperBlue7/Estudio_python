import random

def juego():
    print("-----Adivina el numero-----")
    num = random.randint(1,10)
    numero = int (input("Digita un numero Pista (1 al 10): "))
    
    while num != numero:
        if numero < num:
            print("El numero es mayor")
            numero = int(input("Digita un numero Pista (1 al 10): "))
        else:
            print("el numero es menor")
        numero = int(input("Digita un numero Pista (1 al 10): "))
    print("Felicidades adivinaste el numero")
    


if __name__ == '__main__':
    juego()
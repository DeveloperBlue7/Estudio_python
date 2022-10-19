def ciclo():
    for c in range (1, 10):
        print(f"Numero {c}")

def ciclo1():
    for c in range (2, 12, 2):
        print(f"Numero {c}") 


def tabla():
    for c in range (11):
        print(f"11 * {c} = {11 * c}")
        print("")


def tabla2():
    conteo = 0
    while conteo < 11:
        print(f"11 x {conteo} = {conteo * 11}")
        conteo += 1

#recorrer un string con for

def run():
    nombre = input("Digite Su Nombre: ")
    for letra in (nombre):
        print(letra)


def run1():
    frase = input("digite una frase: ")
    for letra in (frase):
        print(letra.upper()) 

# Interrumpiendo ciclos con break y continue

def run2():
    for contador in range(100):
        if contador % 5 != 0:
            continue
        print(contador)


def run3():
    for d in range (100):
        if d % 10 != 0:
            continue
        print(d)


def run4():
    for d in range(100):
        print(d)
        if d == 77:
            break


def run5():
    palabra = input("Digite palabra: ")
    for c in palabra:
        print(c)
        if c == "e":
            break


def run6():
    for i in range(100):
        print(i)
        if i == 55:
            break


# Desafio ciclo while con break y continue

def run7():
    numero = 0
    while numero < 10:
        print(numero)
        numero += 1
        if numero == 3:
            break

    
def run8():
    while 1 < 5:
        frase = input("Digite su frase: ")
        if frase == "lobo":
            break
        
    
def run9():
    conteo = 0
    while conteo < 100:
        conteo += 1
        if conteo % 20 != 0:
            continue   
        print(conteo)    
        

def run10():
    lista = ["carlos", "cristian"]
    while 1 < 5:
        palabra = input ("Digite Nombres Con C: ")
        if palabra == lista[0]:
            print("Felicidades Adivinaste el nombre")
            break
        if palabra == "exit":
            break

       

if __name__ == '__main__':
    run10()
    


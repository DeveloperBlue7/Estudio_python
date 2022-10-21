def lista():
    numeros = [4 , 7 , 9 , 5 , 55 , 90]
    # Agregar a una lista con "append"
    numeros.append("Lobo")
    # borrar de lista "pop con indice"
    numeros.pop(5)
    # lista al reves [::-1]
    print(numeros[::-1])
    print(numeros)



if __name__ == '__main__':
    lista()


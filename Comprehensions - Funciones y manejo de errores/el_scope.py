# Algo valido del scope es lo siguiente en la funcion la variable si se puede utilizar
num = 7
print(num)


# la variable local se puede imprimir se puede operar pero no se puede sobreescribir
def numero():
    #num = 2
    num1 = num + 3
    print(num1)

numero()


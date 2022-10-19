
dolar = 4500
print("Conversion De Moneda\n")
print("1. Dolares a Pesos\n2. Pesos a dolares\n")
opcion = input("Digita la opcion que necesitas:\n")
opcion = int(opcion)
if opcion == 1:
    valor = int(input("Digita cuantos dolares tienes: "))
    resultado = valor * dolar
    resultado = round(resultado, 2)
    print(f"{valor} dolares equivalen a:\n{resultado} Pesos Colombianos")
elif opcion == 2:
    valor = int(input("Digita cuanto dinero en Pesos tienes: "))
    resultado = valor / dolar
    resultado = round(resultado, 2)
    print(f"{valor} pesos colombianos equivalen a:\n{resultado} Dolares")
else:
    print("Ingreso Incorrecto")





def conversion(tipo_pesos, dolar):
    valor = int(input("Digita cuantos pesos " + tipo_pesos +" tienes:\n"))
    resul = valor / dolar
    resul = round(resul, 2)
    print(f"{valor} pesos {tipo_pesos} equivalen a:\n{resul} Dolares")

    
dolarM = 19.99
dolarA = 151.02
dolarC = 4600.91
menu = """
Bienvenido al Convertidor de moneda 🤑🤑

1. Peso Mexicano a Dolares
2. Pesos Argentinos a Dolares
3. Pesos Colombianos a Dolares

Digita la opcion que necesitas:"""

opcion = int(input(menu))
if opcion == 1:
    conversion("Mexicanos", dolarM)
elif opcion == 2:
    conversion("Argentinos", dolarA)
elif opcion == 3:
    conversion("Colombianos", dolarC)
else:
    print("¡error! Digite una opcion incorrecta")


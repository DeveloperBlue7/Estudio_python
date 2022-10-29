
def suma_rango(a, b):
    print(a, b)
    suma = 0 
    for d in range(a, b):
        suma += d
    return suma

resultado = suma_rango(1, 10)
print(resultado)
resultado_2 = suma_rango(resultado, resultado + 3)
print(resultado_2)


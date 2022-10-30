# HIGHER ORDER FUNCTION (HOF) EJECUTAR UNA FUNCION SOBRE OTRA FUNCION

# EJEMPLO LARGO 

def incrementar(x):
    return x + 1

turno_1 = lambda x: x + 1

def turno(x, d):
    return x + d(x)

turno_2 = lambda x, d: x + d(x)


resultado = turno(3, incrementar)
print(resultado)

resultado = turno_2(2, lambda x: x + 5)
print(resultado)

resultado = turno_2(2, lambda x: x * 5)
print(resultado)




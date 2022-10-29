# PRIMER CASO
def volumen(length, width, depth):
    return length * width * depth
resultado = volumen(6, 7, 7)

print(resultado)

# SEGUNDO CASO
def volumen_2(length=1, width=2, depth=1):
    return length * width * depth
resultado = volumen_2(length=5)

print(resultado)

# TERCER CASO
def volumen_2(length=1, width=2, depth=1):
    return length * width * depth, width, "Hello"
resultado = volumen_2(length=5)

print(resultado)

# Cuarto CASO
def volumen_2(length=1, width=2, depth=1):
    return length * width * depth, width, "Hello"
resultado, c, d = volumen_2(length=5)

print(resultado)
print(c)
print(d)

# FUNCIONES LAMBDAS

def suma(x):
    return x + 10

resul = suma(10)
print(resul)

incrementar = lambda x: x + 10

resul = incrementar(20)
print(resul)

# Ejemplo

nombre = lambda nom, apell: f"Mi nombre es: {nom.title()} {apell.title()}"

texto = nombre("cristian", "camargo")
print(texto)
def poblacion():
    keys = ["Col", "Per"]
    values = [300, 500]
    return keys, values

a = "Inicio"

def populares(dato, pais):
    resultado = list(filter(lambda x: x["Pais"] == pais, dato))
    return resultado
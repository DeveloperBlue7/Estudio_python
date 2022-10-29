# DICTIONARY COMPREHENSION

# DICCIONARIO NORMAL 

dic = {}

for d in range(1, 11):
    dic[d] = d * 5
print(dic)

# DICTIONARY COMPREHENSION con menos lineas de codigo
dic_2 = { d: d * 5 for d in range(1, 11)}
print(dic_2)

# EJEMPLO
import random
countries = ["Colombia", "Argentina", "Ecuador"]
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
print(population)

# EJEMPLO 2

population_2 = {d : random.randint(1, 100) for d in countries}
print(population_2)

print("EJEMPLO 2")

names = ["Hugo", "Paco", "Polo"]
numero = [1, 2, 3]

print(list(zip(names, numero)))

nombres = { names: numero for (names, numero) in zip(names, numero)}
print(nombres, "\n")

print("EJEMPLO MIO")

receta = ["Sopa", "Pasta", "Arroz", "Ensalada"]
dificultad = ["Facil", "Medio", "Dificil", "Muy Dificil"]

recetas = { dificultad: receta for (dificultad, receta) in zip(dificultad, receta)}

print(recetas)

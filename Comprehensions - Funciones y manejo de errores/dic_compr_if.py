import random
countries = ["Colombia", "Argentina", "Ecuador", "Paraguay"]
population = {}

population_2 = {d : random.randint(1, 100) for d in countries}
print(population_2)

resultado = {c: d for (c,d) in population_2.items() if d > 30}
print(resultado)

texto = "las cosas increibles de la vida son las mas simples"

unir = { c: c.upper() for c in texto if c in "aeiu"}
print(unir)
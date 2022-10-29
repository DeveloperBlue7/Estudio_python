# LIST COMPREHENSION

# LISTA NORMAL CON UN FOR
numbers = []

for d in range(1, 20, 2):
    numbers.append(d)
print(numbers)

# LISTA MAS CORTA CON LIST COMPREHENSION

number_2 = [ d for d in range(0, 20, 2)]
print(number_2)

# LISTA NORMAL CON UN FOR con una operacion
numbers = []

for d in range(1, 20, 2):
    numbers.append(d * 3)
print(numbers)

# LISTA MAS CORTA CON LIST COMPREHENSION con operación

number_2 = [ d * 5 for d in range(0, 20, 2)]
print(number_2)

# LISTA MAS CORTA CON LIST COMPREHENSION con operación y con una condición
print("Procedimiento")
number_2 = [ d * 2 for d in range(1, 21) if d % 2 == 0]
print(number_2)


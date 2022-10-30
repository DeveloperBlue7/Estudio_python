# funcion map realiza transformaciones a una lista de elementos

num_1 = [1, 2, 3, 4, ]
num_2 =[]
for d in num_1:
    num_2.append(d * 5)

# funcion MAP
num_3 = list(map(lambda d: d * 7, num_1))


print(num_1)
print(num_2)
print(num_3)

nume_1 = [1, 2, 3, 7]
nume_2 = [6, 5, 4]

result = list(map(lambda x, y: x * y, nume_1, nume_2))
print(result)
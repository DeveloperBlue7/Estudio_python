# from cgitb import text


# # LEER UN TEXTO DE UN ARCHIVO 
file = open("./text.txt")
# #print(file.read())

# #LEERLO LINEA A LINEA
# print(file.readline())

for c in file:
    print(c)


file.close()

# otro modo de leer 

with open("./text.txt") as file:
    for c in file:
        print(c)
    
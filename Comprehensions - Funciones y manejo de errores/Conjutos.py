# EL ZEN DE PYTHON 
# import this   para traer zen de python
# CONJUNTOS (COMO EN LAS ESCUELAS )
# SE PUEDE MODIFICAR - NO TIENEN UN ORDEN - NO PERMITEN DUPLICADOS
set_counttries = {'Colombia', 'Mexico', 'Bolivia'}
print(set_counttries)
print(type(set_counttries))
set_number = {1, 2, 3, 4, 567, 777, 1}
print(set_number)
set_types = {1, "hola", False, 12.12}#Jamas importara el orden
print(set_types)
set_from_string = set("hola") #Otra forma de crear un conjunto 
print(set_from_string)
#UN DICCIONARIO EN UNA TUPLA
set_from_tuples = set(("abc", "fhj", "fhd", "abc"))
print(set_from_tuples)
# CONVERTIR UNA LISTA EN UN DICCIONARIO
numbers = [1, 2, 3, 5, 3, 6, 1, 2, 5]
set_from_list = set(numbers)
print(set_from_list)
lis = list(set_from_list)
print(lis)


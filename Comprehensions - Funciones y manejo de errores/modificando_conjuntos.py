# MODIFICAR CONJUTOS
from turtle import clear


set_countries = {'Colombia', 'Mexico', 'Bolivia'}
size = len(set_countries)
print(size)
print("Colombia" in set_countries)

# AGREGAR ELEMENTOS AL CONJUNTO (.ADD)
set_countries.add("Argentina")
print(set_countries)

# ACTUALIZAR CONJUNTOS (UPDATA)
set_countries.update({"Peru", "Ecuador", "Brazil"})
print(set_countries)

#BORRAR ELEMENTO DEL CONJUNTO (REMOVE)
set_countries.remove("Brazil")
print(set_countries)

#DESCARTAR UN ELEMENTO EN EL CONJUNTO SI NO ESTA NO PASA NADA (discard)
set_countries.discard('España')
print(set_countries)

#ELIMINAR UN ELEMENTO 
set_countries.discard('Ecuador')
print(set_countries)

#LIMPIAR UN CONJUNTO BORRANDO TODOS LOS ELEMENTOS (CLEAR)
set_countries.clear()
print(set_countries)
print(len(set_countries))
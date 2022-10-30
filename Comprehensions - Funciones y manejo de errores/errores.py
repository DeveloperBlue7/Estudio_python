#print(5 / 0)

#print(elemento)

suma = (lambda x, y: x + y)
assert suma(2,2) == 4
print(suma(2,2))

# Lanzar mis propios errores
age = 10 
if age < 18:
    raise Exception("ERROR PONGA ATENCION")

    
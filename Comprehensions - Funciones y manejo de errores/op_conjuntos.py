# OPERACIONES CON CONJUNTOS
from this import s


set_a = {'Colombia', 'Mexico', 'Bolivia'}
set_b = {'Peru', 'Bolivia'}

# PARA UNIR DOS CONJUNTOS SE UTILIZA .UNION(SET) O (|)
set_c = set_a.union(set_b)
print(set_c)
set_c = (set_a | set_b)
print(set_c)

# INTERSECIÓN ENTRE CONJUNTOS con (.intersection) o (&)
print("**********************")
set_d = set_a.intersection(set_b)
print(set_d)
set_d = (set_a & set_b)
print(set_d)

# DIFERENCIA DE ELEMENTOS DE UN CONJUNTO AL OTRO (DIFERENCE) O (-)
print("**********")
set_e = set_a.difference(set_b)
print(set_e)
set_e = (set_a - set_b)
print(set_e)

# DIFERENCIA SIMETRICA CON (SYMMETRIC_DIFFERENCE) HACER UNA UNION SIN LOS ELEMENTOS QUE TIENEN EN COMUN o (^)

set_1 = set_a.symmetric_difference(set_b)
print(set_1)
set_1 = (set_a ^ set_b)
print(set_1)
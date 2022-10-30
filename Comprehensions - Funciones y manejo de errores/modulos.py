# MODULOS 
from distutils.filelist import findall
import sys 

print(sys.path)
lista = (sys.path)

import re 

texto = "Mi numero de telefono 5873495034, codigo pais es 57, mi numere de la suerte es el 7"

resultado = re.findall("[0-9]+", texto)
print(resultado)

import time

tiempo = time.time()
print(tiempo)

tiempo_1 = time.localtime()
result = time.asctime(tiempo_1)

print(result)

import collections as c

numbers = [1,1,1,2,2,2,2,2,4,4,4,43,3,3,6,6,6,6,7,7,7,7,7,]
conteo = c.Counter(numbers)
print(conteo)
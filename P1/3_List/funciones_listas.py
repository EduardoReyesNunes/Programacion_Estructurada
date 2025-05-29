'''
list (array)
son colecciones  o conjuntos de datos/ valores bajo un mismo nombre,
para acceder a los valores se hace un indice numerico 

Nota: sus valores si son Modificables

las lastas es una coleccion ordenada y modificable , permite miembros duplicados 
'''

import os

os.system("cls")

#funciones mas comunes de las listas

paises=["Mexico","Brasil","España","Canada"]
numeros=[23,12,100,34]
varios=["Hola",True,33,3.12]

#ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort()
print(numeros)
paises.sort()
print(paises)



#añadir o insertai un item a las listas

print(paises)
paises.append("Honduras")
print(paises)


#2da Forma 
paises.insert(1,"Honduras")
print(paises)


#Elimina un registro 
paises.sort()
print(paises)
paises.pop(4)
print(paises)

#2da forma 
paises.remove("Honduras")
print(paises)

#Buscar un elemento en una lista
#paises=["Mexico","Brasis","España","Canada"]
print("Brasil" in paises)

#contar el numero de veces que un elemento existe o esta dentro de un lista
#numeros=[23,12,100,34]
print(numeros)
numeros.insert(1,12)
print(numeros.count(12))


#dar la inversa de una lista
print(paises)
paises.reverse()
print(paises)
print(numeros)
numeros.reverse()
print(numeros)

#conocer el indice o la posicion de un dato de la lista
posicion=(paises.index("España"))

paises[posicion]="ESPAÑA"

print(paises)

#unir el contenido de 2 o mas listas 
#numeros=[100, 34, 23, 12, 12]
numeros2=[300,500,100]
print(numeros,numeros2)
numeros.extend(numeros2)
print(numeros)
paises.extend(numeros2)
print(paises)
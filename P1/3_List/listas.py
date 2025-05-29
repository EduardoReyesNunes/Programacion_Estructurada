import os
#Ejemplo 1 crea una lista de numeros e imprimir el contenido
os.system("cls")
listanm=[15,16,17,18]
print(listanm)

for i in listanm:
    print(i)

for i in range(0,len(listanm)):
    print(listanm[i])

#ejemplo 2 Crear una lista de palabras y posteriormente buasca coincidencias de una palabra 

listapl=["hola","Junior","Natanael","Gabito"]
print(listapl)
palbusc=input("Que palabra quieres buscar : ")
if palbusc in listapl:
    print(f"La palabra {palbusc} esta en la posicion ",listapl.index(palbusc))
else:
    print("No sepuede encontrar la palabra")




#ejemplo 3 añadir elementos a una lista
resp="si"

while resp=="si":
    anadir=input("que palabra quieras añadir? ")
    listapl.append(anadir)
    print(listapl)


    resp=input("Quieres añadir otra palabra :").lower()
    while resp not in ["si","no"]:
        resp=input("Quieres añadir otra palabra").lower()

    print("Tu lista final fue ",listapl)

#Ejemplo 4 crear un alista multidimencional (Matriz) que almacene el nombre y telefono de 4 personas


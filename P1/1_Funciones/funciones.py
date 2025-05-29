"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#   1.- Funcion que no recibe parametros y no regresa valor
def solicitarDatos1():
    nombre=input("Nombr: ")
    telefono=input("telefono: ")
    print(f"Nombre: {nombre} \n\nTelefono: {telefono} ")

#   3.- Funcion que recibe parametros y no regresa valor
def solicitarDatos3(nom,tel):
    nombre=input("nom")
    telefono=input("tel")
    print(f"Nombre: {nombre} \n\nTelefono: {telefono} ")
    
#   2.- Funcion que no recibe parametros y regresa valor
def solicitarDatos2():
    nombre=input("Nombre: ")
    telefono=input("telefono: ")
    return nombre,telefono

#   4.- Funcion que recibe parametros y regresa valor
def solicitarDatos4(nom,tel):
    nombre=input("nom")
    telefono=input("tel")
    return nombre,telefono

#invocar las funciones 

#   1.- Funcion que no recibe parametros y no regresa valor
solicitarDatos1()

#   3.- Funcion que recibe parametros y no regresa valor
nombre=input("escribe el Nombr: ")
telefono=input("escribe el telefono: ")
solicitarDatos3(nombre,telefono)


#   2.- Funcion que no recibe parametros y regresa valor
nom,tel=solicitarDatos2()
print(f"\n\tLos datos de la agenda son \nNombre es {nom}\nTelefono es {tel}")


#   4.- Funcion que recibe parametros y regresa valor
nombre=input("escribe el Nombr: ")
telefono=input("escribe el telefono: ")
nom,tel=solicitarDatos2(nombre,telefono)
print(f"\n\tLos datos de la agenda son \nNombre es {nom}\nTelefono es {tel}")
import os

'''pelicula={
    "nombre":"",
    "categoria":"",
    "clasificacion":"",
    "genero":"",
    "ideoma":""
}
'''
peliculas = []
pelicula={}

def esperatecla():
    input("\n\t...Oprime cualquier tecla para continuar...")

def borrarpantalla():
    os.system("cls")

def crearpelicula():
    borrarpantalla()
    print("\t\t..::Crear Película::.. \n")
#    pelicula["nombre"] = input("Ingresa el nombre de la película: ").lower().strip()
    pelicula.update({"nombre": input("Ingresa el nombre: ").lower().strip()})
    pelicula.update({"categoria": input("Ingresa la categoría: ").lower().strip()})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: ").lower().strip()})
    pelicula.update({"genero": input("Ingresa el género: ").lower().strip()})
    pelicula.update({"ideoma": input("Ingresa el idioma: ").lower().strip()})
    print("\t\t..::La operacion se realizo con exito::..")

def borrarpelicula():
    borrarpantalla()
    print("\n\t::: Borrar Películas :::\n")
    resp =input("Seguro que quieres borrar una película? (si/no) ").lower().strip()
    if resp == "si":
        pelicula.clear
        print("\t\t..::La operacion se realizo con exito::..")
    elif resp == "no":
        input("La operación se ha cancelado")

def mostrarpelicula():
    borrarpantalla()
    print("..::Mostrar Película::.. ")
    if len(pelicula)>0:
        for i in pelicula :
            print(f"\t{i} :  {pelicula[i]}")
    else:
        print("\n\t\tEl catálogo de películas se encuentra vacío")

def agregarcaracteristicapelicula():
    borrarpantalla()
    print("\t\t..::Agregar caracteristica de la Película::.. ")
    caracteristica = input("Ingresa la característica a agregar: ").lower().strip()
    valor = input(f"Ingrese el valor de la característica '{caracteristica}': ").lower().strip()
    pelicula.update({caracteristica: valor})
    
def modificarcaracteristicapelicula():
    borrarpantalla()
    print("\n\t:::Modificar alguna caracteristica de la Películas:::\n")
    #print(f"\t\tCaracteristicas disponibles:\n\t\t{list(pelicula.keys())}")
    print("\t\tCaracteristicas disponibles:\n")
    '''
    if len(pelicula)>0:
    print(f"\n\tValor actuales: \n ")
    for i in pelicula:
      print(f"\t {(i)} : {pelicula[i]}")
      resp=input(f"\t¿Deseas cambiar el valor de {i}? (Si/No) ")
      if resp=="si":
        pelicula.update({f"{i}":input("\t \U0001F501 el nuevo valor: ").upper().strip()})
        print("\n\t\t ::: ¡LA OPERACION SE REALIZO CON EXÍTO!  :::") 
      else:
        print("\t..:: No hay peliculas en Sistema  ::..")
    esperarTecla()
    '''
    for i in pelicula:
        print(f"\t{i} :  {pelicula[i]}")
    caracteristica = input("\n\tQue caracteristica deseas modificar? ").lower().strip()
    valor = input(f"\tIngrese el valor que deseas cambiar de '{caracteristica}': ").lower().strip()
    pelicula.update({caracteristica: valor})
    print("\t..::La operacion se realizo con exito::..")
    esperatecla()
    borrarpantalla()
    print("\t..::Tu lista ya actualizada quedo asi::..\n")
    for i in pelicula:
        print(f"\t\t{i} :  {pelicula[i]}")

def borrarcaracteristicapeliculas():
    borrarpantalla()
    print("\n\tBorrar alguna caracteristica de la pelicula")
    print("\t\tCaracteristicas disponibles:\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i} :  {pelicula[i]}")
        resp = input("\n\t¿Deseas borrar una característica? (si/no) ").lower().strip()
        if resp =="si":
            caract_borr =input("\n\tQue caracteristica deseas borrar? ").lower().strip()
            while caract_borr not in pelicula:
                caract_borr =input("\n\tNo es un acaracteristica valida ,intentalo de nuevo :").lower().strip()
            del pelicula[caract_borr]
            print("\t..::La operacion se realizo con exito::..")
            esperatecla()
            borrarpantalla()
            print("\t..::Tu lista ya actualizada quedo asi::..\n")
            for i in pelicula:
                print(f"\t\t{i} :  {pelicula[i]}")
            esperatecla()
    else:
        input("No hay carateristicas registradas, preciona cualquier tecla y vuelve a intentarlo :)")

        
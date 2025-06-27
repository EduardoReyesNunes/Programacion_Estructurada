'''Proyecto 1 .
 crear un proyecto que permita gestionar(administrar) peliculas;colocar un menu de opciones para agregar, borrar, 
 modificar, consultar, buscara y vaciar peliculas
 Notas : 1.- utilizar funciones y mandara allamar deesde otro archivo 
         2.- Utilizar una diccionarios para almacenar los atributos o caracteristicas de un apelicula
'''
import peliculas 

opciones=["Crear","Borrar","Mostrar","Agregar Característica","Modificar característica","Borrar característica","SALIR"]
opc=True
while opc:
    peliculas.borrarpantalla()
    print("\t\t..::Bienvenidoa pelimundo::..")
    print("\t..::Un sistema para gestinar peliculas::..\n")

    for i in range(0,len(opciones)):
        print(f"\t\t{i+1}) {opciones[i]}")
    opc=input("\n\tQue opcion deseas elegir?  ").lower().strip()
    match opc:
        case "1" :
            peliculas.crearpelicula()
            peliculas.esperatecla()
        case  "2":
            peliculas.borrarpelicula()
            peliculas.esperatecla()
        case "3":
            peliculas.mostrarpelicula()
            peliculas.esperatecla()
        case  "4":
            peliculas.agregarcaracteristicapelicula()
            peliculas.esperatecla()
        case  "5":
            peliculas.modificarcaracteristicapelicula()
            peliculas.esperatecla()
        case  "6":
            peliculas.borrarcaracteristicapeliculas()
        case "7":
            opc=False
            peliculas.borrarpantalla
            print("Vuelve pronto")
        case _:
            input("ocion no valida, favor de reponder de nuevo")
            opc=True
print("El programa ha finalizado")

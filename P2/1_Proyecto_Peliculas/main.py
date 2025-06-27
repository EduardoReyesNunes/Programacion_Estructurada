'''Proyecto 1 .
 crear un proyecto que permita gestionar(administrar) peliculas;colocar un menu de opciones para agregar, borrar, 
 modificar, consultar, buscara y vaciar peliculas
 Notas : 1.- utilizar funciones y mandara allamar deesde otro archivo 
         2.- Utilizar una lista para almacenar los nombres de las peliculas
'''
import peliculas 

opciones=["Agregar","Borrar","Modificar","Colsultar","Buscar","Vaciar","Salir"]
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
            peliculas.agregarpelicula()
            peliculas.esperatecla()
        case  "2":
            peliculas.borarpelicula()
            peliculas.esperatecla()
        case "3":
            peliculas.modificarpelicula()
            peliculas.esperatecla()
        case  "4":
            peliculas.consultarpelicula()
            peliculas.esperatecla()
        case  "5":
            peliculas.buscarpelicula()
            peliculas.esperatecla()
        case  "6":
            peliculas.vaciarpeliculas()
            peliculas.esperatecla()
        case "7":
            opc=False
            peliculas.borrarpantalla
            print("Vuelve pronto")
        case _:
            input("ocion no valida, favor de reponder de nuevo")
            opc=True
print("El programa ha finalizado")

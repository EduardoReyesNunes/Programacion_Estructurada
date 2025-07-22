'''Proyecto 1 .
 crear un proyecto que permita gestionar(administrar) peliculas;colocar un menu de opciones para agregar, borrar, 
 modificar, consultar, buscara y vaciar peliculas
 Notas : 1.- utilizar funciones y mandara allamar deesde otro archivo 
         2.- Utilizar una diccionarios para almacenar los atributos o caracteristicas de un apelicula
'''
import peliculas

opciones = [
    "Crear",
    "Borrar",
    "Mostrar",
    "Buscar",
    "Modificar",
    "SALIR"
]

opc = True
while opc:
    peliculas.borrar_pantalla()
    print("\t\t..::Bienvenido a pelimundo::..")
    print("\t..::Un sistema para gestionar peliculas::..\n")

    for i in range(len(opciones)):
        print(f"\t\t{i+1}) {opciones[i]}")
    
    opc = input("\n\tQue opcion deseas elegir? ").strip()
    
    match opc:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperar_tecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperar_tecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperar_tecla()
        case "4":
            peliculas.buscarPeliculas()
            peliculas.esperar_tecla()
        case "5":
            peliculas.ModificarPeliculas()
            peliculas.esperar_tecla()
        case "6":
            opc = False
            peliculas.borrar_pantalla()
            print("Vuelve pronto")
        case _:
            input("Opción no válida, favor de responder de nuevo")
            opc = True

print("El programa ha finalizado")
'''
Proyecto 3
Crear un proyecto que permita Gestionar (Administrar) calificaciones; colocar un menu de opciones para agregar, mostrar y calcular
promedios de las calificaciones de los alumnos

Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacenar el nombre de un alumno y 3 calificaciones
'''

import calificaciones

def main():
    op = True
    datos = []
    while op:
        calificaciones.borrarPantalla()
        op = calificaciones.menu_principal()
        match op:
            case "1":
                calificaciones.agregarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcularPromedios(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscarAlumno(datos)
                calificaciones.esperarTecla()
            case "5":
                calificaciones.borrarPantalla()
                print("🚪 .::Terminaste de usar el programa::. 🚪")
                op = False
            case _:
                op = True
                print("⚠️ Opcion no valida, vuelva a intentarlo ⚠️")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()
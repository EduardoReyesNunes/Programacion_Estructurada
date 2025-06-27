'''Proyecto 3 .
 crear un proyecto que permita gestionar calificaciones colocar un  menu de opciones para agregar, borrar, 
 modificar y calcular promedio de las calificaciones de un alumno.
 Notas : 
         1.- utilizar funciones y mandara allamar deesde otro archivo 
         2.- Utilizar listas para alamacenar el nombre de un alumno y 3 calificaciones
'''
import calificaciones 

def main():
    opc=True
    datos = []
    while opc:
        calificaciones.borrarpantalla()
        opc=calificaciones.menu_principal()
        
        
        match opc:
            case "1" :
                calificaciones.agregar(datos)
                calificaciones.esperatecla()
            case  "2":
                calificaciones.mostar(datos)
                calificaciones.esperatecla()
            case  "3":
                calificaciones.calcular(datos)
                calificaciones.esperatecla()
            case "4":
                opc=False
                calificaciones.borrarpantalla
                print("Vuelve pronto")
            case _:
                input("ocion no valida, favor de reponder de nuevo")
                opc=True
if __name__=="__main__":
    main()
print("El programa ha finalizado")

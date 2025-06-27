import os

'''lista=[
    ["ruben", 10.0,10.0,10.8],
    ["maria", 9.0,8.5,9.2],
    ["juan", 7.5,6.0,8.0],
]'''
lista=[]
alumnos=[]

def menu_principal():
     opciones=["agregar","Mostar","calcular promedio","SALIR"]
     print("\t\t..::Bienvenidoa calificat::..")
     print("\t..::Un sistema para gestinar calificaciones::..\n")
 
     for i in range(0,len(opciones)):
         print(f"\t\t{i+1}) {opciones[i]}")
     opc=input("\n\tQue opcion deseas elegir?  ").lower().strip()
     return opc

def agregar(datos):
    borrarpantalla()
    print("\t\tAgregar una calificación")
    alumno = []
    nombre = input("\tIngrese el nombre del alumno: ").strip()
    alumno.append(nombre)

    for i in range(1, 4):
        continuar=True
        while continuar:
            try:
                calificacion = float(input(f"\tIngrese la calificación {i} del alumno: "))
                if calificacion>0 and calificacion<=10:
                    continuar = False
                else:
                    print("\tLa calificación debe estar entre 0 y 10. Inténtalo de nuevo.")

            except ValueError:
                print("\tEntrada inválida. Por favor, ingrese un número válido.")

                
        alumno.append(calificacion)

    datos.append(alumno)
    print("\t\tAlumno agregado con éxito.")

def mostar(datos):
    borrarpantalla()
    print("\t\tMostrar calificaciones")
    if not datos:
        print("\n\tNo hay calificaciones registradas.")
    else:
        borrarpantalla()
        print("\tLista de calificaciones:")
        print("\t------------------------------------------------------------")
        print("\t| Alumno | Calificación 1 | Calificación 2 | Calificación 3 |")
        print("\t------------------------------------------------------------")
        for i in range (len(datos)):
            alumno = datos[i]
            print(f"\t|{alumno[0]}\t\t {alumno[1]}\t\t {alumno[2]}\t\t {alumno[3]} |")
            print("\t------------------------------------------------------------")

def calcular(datos):
    borrarpantalla()
    print("\t\tCalcular promedios")
    if not datos:
        print("\t\tNo hay datos para calcular promedio.")
        return

    print("\t-------------------------------------------------")
    print("\t| Alumno\t| Promedio individual\t|")
    print("\t-------------------------------------------------")

    suma_total = 0
    total_calificaciones = 0

    for alumno in datos:
        nombre = alumno[0]
        calificaciones = alumno[1:]
        promedio = sum(calificaciones) / len(calificaciones)

        print(f"\t| {nombre}\t\t| {promedio:.2f}\t\t|")

        suma_total += sum(calificaciones)
        total_calificaciones += len(calificaciones)

    promedio_general = suma_total / total_calificaciones
    print("\t-------------------------------------------------")
    print(f"\tPromedio general de todos los alumnos: {promedio_general:.2f}")
    
def esperatecla():
    input("Presione una tecla para continuar...")

def borrarpantalla():
   os.system("cls")

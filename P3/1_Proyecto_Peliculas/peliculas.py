import os
import mysql.connector
from mysql.connector import Error

pelicula={}

def conectar():
  try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_peliculas"  
      )
    return conexion
  except Error as e:
    print(f"El error que se presento es: {e}")
    return None


def esperar_tecla():
    input("\n\t...Presiona cualquier tecla para continuar...")

def borrar_pantalla():
    os.system("cls")


def crearPeliculas():
  borrar_pantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Crear Películas ::. \n")
    pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
    #pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
    
    ####### BD
    cursor=conexionBD.cursor()
    sql="insert into peliculas (nombre,categoria,clasificacion,genero,idioma) value (%s,%s,%s,%s,%s)"
    val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
    cursor.execute(sql,val)
    conexionBD.commit()
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")

def borrarPeliculas():
  borrar_pantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Borrar Películas ::. \n")
    nombre=input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80) 
      resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        sql="delete from peliculas where nombre = %s"
        val=(nombre,)
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")
    else:
      print("\t .:: peliculas no encontradas en el sistema ::..")

def mostrarPeliculas():
  borrar_pantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Mostrar las Películas ::. \n")
    cursor=conexionBD.cursor()
    sql="select * from peliculas"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80)  
    else:
      print("\t .:: No hay peliculas en el sistema ::..") 

def buscarPeliculas():
  borrar_pantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Buscar Películas ::. \n")
    nombre=input("Ingresa el nombre de la pelicula a buscar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80)  
    else:
      print("\t .:: peliculas no encontradas en el sistema ::..")

def ModificarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\n\t🎥 .::Modificar Película::. 🎥\n")

        nombre = input("Ingresa el nombre de la pelicula a Modificar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()

        if registros:
            print("\n\t::Películas::.")
            print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificación':<15} {'Género':<15} {'Idioma':<15}")
            print(f"-" * 80)
            for peli in registros:
                print(f"{peli[0]:<10}{peli[1]:<15}{peli[2]:<15}{peli[3]:<15}{peli[4]:<15}{peli[5]:<15}")
                print(f"-" * 80)
                resp = input(f"¿Deseas Modificar la película {nombre}? (Si/No): ").upper().strip()
                if resp == "SI":
                    pelicula["nombre"] = input("Ingresa el Nombre: ").upper().strip()
                    #pelicula.update({"nombre": input("Ingresa el Nombre: ").upper().strip()})
                    pelicula.update({"categoria": input("Ingresa la Categoria: ").upper().strip()})
                    pelicula.update({"clasificacion": input("Ingresa la Clasificacion: ").upper().strip()})
                    pelicula.update({"genero": input("Ingresa el genero: ").upper().strip()})
                    pelicula.update({"idioma": input("Ingresa el Idioma: ").upper().strip()})

                    sql = "UPDATE peliculas SET nombre = %s, categoria = %s, clasificacion = %s, genero = %s, idioma = %s WHERE nombre = %s"
                    val = (pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"], nombre)
                    cursor.execute(sql, val)
                    conexionBD.commit()
                    print("\n\t✅ .::La película se ha modificado en la base de datos::. ✅")
        else:
            print("\n\t❌ .::Películas no encontradas en el sistema::. ❌")
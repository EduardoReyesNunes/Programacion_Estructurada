from conexionBD import *
import datetime

def registrar(nombre,apellido,email,contrasena):
    try:
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)"
        val = (nombre, apellido, email, contrasena, fecha)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False

def iniciarSesion(correo,contrasena):
    try:
        sql="SELECT * FROM usuarios WHERE email=%s AND password=%s"
        val=(correo,contrasena)
        cursor.execute(sql,val)
        usuario=cursor.fetchone()
        if usuario:
            return usuario
        else:
            return None
    except:
        return None
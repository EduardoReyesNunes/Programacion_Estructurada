from conexionBD import *
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre,apellido,email,password):
    try:
        contrasena=hash_password(password)
        sql = "INSERT INTO users (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, NOW())"
        val = (nombre, apellido, email, contrasena)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False

def iniciarSesion(correo, contrasena):
    try:
        contrasena = hash_password(contrasena)
        sql = "SELECT id, nombre, apellidos FROM users WHERE email=%s AND password=%s"
        val = (correo, contrasena)
        cursor.execute(sql, val)
        return cursor.fetchone() 
    except:
        return None
    
def mostrarUsuarios():
    try:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        return None

def modificarUsuario(id_usuario_mod, nombre, apellido, email, password):
    try:
        contrasena = hash_password(password)
        sql = "UPDATE users SET nombre=%s, apellidos=%s, email=%s, password=%s WHERE id=%s"
        val = (nombre, apellido, email, contrasena, id_usuario_mod)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False

def eliminarUsuario(id_usuario):
    try:
        sql = "DELETE FROM users WHERE id = %s"
        val = (id_usuario,)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False
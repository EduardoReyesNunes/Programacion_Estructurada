from conexionBD import *

def agregarProducto(nombre, descripcion, precio):
    try:
        sql = "INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)"
        val = (nombre, descripcion, precio)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False
    
def mostrarProductos():
    try:
        sql = "SELECT * FROM productos"
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        return None
def modificarProducto(id_producto_mod, nombre, descripcion, precio):
    try:
        sql = "UPDATE productos SET nombre=%s, descripcion=%s, precio=%s WHERE id_producto=%s"
        val = (nombre, descripcion, precio, id_producto_mod)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False
    
def eliminarProducto(id_producto):
    try:
        sql = "DELETE FROM productos WHERE id_producto = %s"
        val = (id_producto,)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False
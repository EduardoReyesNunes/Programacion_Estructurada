from conexionBD import *

def crearventa(usuario_id, cantidad, id_producto_vend,  nombre_producto_vend, precio_producto_vend):
    try:
        total= cantidad * float(precio_producto_vend)
        sql = "INSERT INTO ventas (id_vendedor,cantidad,id_producto,producto,total,fecha) VALUES (%s, %s, %s, %s, %s ,NOW())"
        val = (int(usuario_id),int(cantidad),int(id_producto_vend),nombre_producto_vend,float(total))
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False
    
def mostrarVentas():
    try:
        sql = "SELECT * FROM ventas"
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        return None
    
def modificarVenta(id_venta_mod,nueva_cantidad, id_producto_vend, nombre_producto_vend,precio_producto_vend):
    try:
        nuevo_total = int(nueva_cantidad) * float(precio_producto_vend)
        sql = "UPDATE ventas SET cantidad = %s, id_producto = %s, producto = %s , total = %s WHERE id_venta = %s"
        val = (int(nueva_cantidad), id_producto_vend, nombre_producto_vend,nuevo_total, id_venta_mod)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except :
        return False

def eliminarVenta(id_venta):
    try:
        sql = "DELETE FROM ventas WHERE id_venta = %s"
        val = (id_venta,)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except :
        return False
    
def mostrarVentasPorVendedor():
    try:
        # Todos los vendedores
        sql_vendedores = "SELECT id, nombre, apellidos FROM users"
        cursor.execute(sql_vendedores)
        vendedores = cursor.fetchall()
        
        resultados = []
        
        for vendedor in vendedores:
            vendedor_id, nombre, apellidos = vendedor
            # Ventas por cada vendedor
            sql_ventas = "SELECT * FROM ventas WHERE id_vendedor = %s"
            cursor.execute(sql_ventas, (vendedor_id,))
            ventas = cursor.fetchall()
            
            resultados.append({
                'vendedor': f"{nombre} {apellidos} (ID: {vendedor_id})",
                'ventas': ventas
            })
        
        return resultados
    except:
        return None
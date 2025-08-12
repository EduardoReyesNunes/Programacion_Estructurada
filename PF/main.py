import funciones
import conexionBD
from usuarios import usuarios
from productos import productos
from ventas import ventas
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n\t📝 ..:: Registro en el Sistema ::.. 📝")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            lista_usuarios=usuarios.registrar(nombre,apellidos,email,password)
            if lista_usuarios:
                print(f"\n\t\t✅ {nombre} {apellidos} se registrado correctamente con el email {email} ✅")
            else:
                print(f"\n\t\t⚠ No fue posible registrar al usuario {nombre} {apellidos}, intentelo más tarde ⚠")
            funciones.esperarTecla()

        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n\t📂 ..:: Inicio de Sesión ::.. 📂")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            lista_usuarios=usuarios.iniciarSesion(email,password)
            if lista_usuarios:
                if lista_usuarios[0]==1:
                    admin(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
                else:
                    vendedor(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
            else:
                print(f"\n\t⚠ Email y/o password incorrectos, por favor verifica y vuelve a intentar ⚠")
                funciones.esperarTecla()
              
        elif opcion=="3" or opcion=="SALIR": 
            print("🚪 Terminó la Ejecución del Sistema 🚪")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("⚠ Opción no válida ⚠")
            opcion=True
            funciones.esperarTecla()

def admin(usuario_id,nombre,apellidos):
   permanecer=True
   while permanecer:
        funciones.borrarPantalla()
        print(f"\n\t\t🛠 ..:: Bienvenido {nombre} {apellidos} ::.. 🛠")
        opcion=funciones.admin()
        match opcion:
            case "1":
                funciones.borrarPantalla()
                print("\t\t📄 ..:: Agregar producto ::.. 📄")
                agprod=input("Deseas agregar un producto al sistema (si/no) :").lower().strip()
                if agprod == "si":
                    funciones.borrarPantalla()
                    print("\t🍰 ..:: Agregar producto ::.. 🍰")
                    nombre=input("\n\t Nombre del producto: ").upper().strip()
                    descripcion=input("\t Descripción del producto: ").lower().strip()
                    precio=float(input("\t Precio del producto: "))
                    proceso=productos.agregarProducto(nombre, descripcion, precio)
                    if proceso: 
                        print(f"\n\t\t✅ El producto {nombre} se ha agregado correctamente ✅")
                    else:
                        print(f"\n\t\t❌ No fue posible agregar el producto {nombre}, intentelo mas tarde ❌")
                    funciones.esperarTecla()
                elif agprod == "no":
                    print("⭕ Cancelando...")
                    funciones.esperarTecla()
                else: 
                    print("⚠ Opción no válida ⚠")
                
            case "2":
                funciones.borrarPantalla()
                print("\t\t📝 ..:: Agregar vendedor ::.. 📝")
                agprod=input("Deseas agregar un vendedor/usuario al sistema (si/no) :").lower().strip()
                if agprod == "si":
                    nombre=input("\t ¿Nombre de vendedor?: ").upper().strip()
                    apellidos=input("\t ¿Cuales son sus apellidos?: ").upper().strip()
                    email=input("\t Ingresa el email: ").lower().strip()
                    password=getpass.getpass("\t Ingrese una contraseña: ").strip()
                    lista_usuarios=usuarios.registrar(nombre,apellidos,email,password)
                    if lista_usuarios:
                        print(f"\n\t\t✅ {nombre} {apellidos} se registrado correctamente con el email {email} ✅")
                    else:
                        print(f"\n\t\t❌ No fue posible registrar al usuario {nombre} {apellidos}, intentelo más tarde ❌")
                    funciones.esperarTecla()
                elif agprod == "no":
                    print("⭕ Cancelando...")
                    funciones.esperarTecla()
                else: 
                    print("⚠ Opción no válida ⚠")
                
            case "3":
                funciones.borrarPantalla()
                print("\t\t☕🍰 ..:: Productos registrados ::.. 🍰☕")
                productos_lista = productos.mostrarProductos()
                if len(productos_lista) >0:
                    print(f"\n{'ID':<6}|{'Nombre':<20}|{'Descripcion':<46}|{'Precio':<20}")
                    print("-" * 92)
                    for producto in productos_lista:
                        print(f"{producto[0]:<6}|{producto[1]:<20}|{producto[2]:<46}|{producto[3]:<20}")
                        print("-" * 92)
                    exportar = input("\n\t👉 ¿Exportar datos a Excel? (si/no): ").lower().strip()
                    if exportar == "si":
                        columnas = ["ID", "Nombre", "Descripción", "Precio"]
                        funciones.exportar_a_excel("productos", productos_lista, columnas, "Productos")
                    funciones.esperarTecla()  
                else:
                    print("\n\t\t❌ No hay productos registrados ❌")
                    funciones.esperarTecla()

            case "4":
                funciones.borrarPantalla()
                print("\t\t👤 ..:: Usuarios registrados ::.. 👤")
                usuarios_lista = usuarios.mostrarUsuarios()
                if len(usuarios_lista) >0:
                    print(f"\n{'ID':<6}|{'Fecha registro':<18}|{'Nombre':<13}|{'Apellido':<13}|{'Email':<30}")
                    print("-" * 92)
                    for usuario in usuarios_lista:
                        print(f"{usuario[0]:<6}|{usuario[5]}        |{usuario[1]:<13}|{usuario[2]:<13}|{usuario[3]:<30}")
                        print("-" * 92)
                    exportar = input("\n\t👉 ¿Exportar datos a Excel? (si/no): ").lower().strip()
                    if exportar == "si":
                        columnas = ["ID", "Nombre", "Apellidos", "Email", "Password", "Fecha Registro"]
                        funciones.exportar_a_excel("usuarios", usuarios_lista, columnas, "Usuarios")
                    funciones.esperarTecla()
                else:
                    print("\n\t\t❌ No hay usuarios registrados ❌")
                    funciones.esperarTecla()

            case "5":
                funciones.borrarPantalla()
                print("\t\t🔁 ..:: Modificar producto ::.. 🔁")
                print("\n\t\t🍽 ..:: Productos registrados ::.. 🍽")
                productos_lista = productos.mostrarProductos()
                if len(productos_lista) >0:
                    print(f"\n{'ID':<6}|{'Nombre':<20}|{'Descripcion':<46}|{'Precio':<20}")
                    print("-" * 92)
                    for producto in productos_lista:
                        print(f"{producto[0]:<6}|{producto[1]:<20}|{producto[2]:<46}|{producto[3]:<20}")
                        print("-" * 92)
                    respuesta = input("\n\t\t⚠ ¿Deseas modificar un producto? (si/no): ").lower().strip()
                    if respuesta == "si":
                        id_producto_mod = int(input("\n\t\t Ingresa el ID del producto a modificar: "))
                        nombre = input("\t\t Nuevo nombre del producto: ").upper().strip()
                        descripcion = input("\t\t Nueva descripción del producto: ").lower().strip()
                        precio = float(input("\t\t Nuevo precio del producto: "))
                        proceso = productos.modificarProducto(id_producto_mod, nombre, descripcion, precio)
                        if proceso:
                            print(f"\n\t\t✅ El producto con ID {id_producto_mod} ha sido modificado correctamente ✅")
                        else:
                            print(f"\n\t\t❌ No fue posible modificar el producto con ID {id_producto_mod}, intentelo más tarde ❌")
                        funciones.esperarTecla()
                    elif respuesta == "no":
                        print("⭕ Cancelando...")
                    else:
                        print("⚠ Opción no válida ⚠")  
                else:
                    print("\n\t\t❌ No hay productos registrados ❌")
                    funciones.esperarTecla()

            case "6":
                funciones.borrarPantalla()
                print("\t\t🔁 ..:: Modificar vendedor ::.. 🔁")
                print("\n\t\t👤 ..:: Usuarios registrados ::.. 👤")
                usuarios_lista = usuarios.mostrarUsuarios()
                if len(usuarios_lista) >0:
                    print(f"\n{'ID':<6}|{'Fecha registro':<18}|{'Nombre':<13}|{'Apellido':<13}|{'Email':<30}")
                    print("-" * 92)
                    for usuario in usuarios_lista:
                        print(f"{usuario[0]:<6}|{usuario[5]}        |{usuario[1]:<13}|{usuario[2]:<13}|{usuario[3]:<30}")
                        print("-" * 92)
                    respuesta = input("\n\t\t⚠ ¿Deseas modificar un usuario? (si/no): ").lower().strip()
                    if respuesta == "si":
                        id_usuario_mod = int(input("\n\t\t Ingresa el ID del usuario a modificar: "))
                        nombre = input("\t\t Nuevo nombre del usuario: ").upper().strip()
                        apellidos = input("\t\t Nuevos apellidos del usuario: ").upper().strip()
                        email = input("\t\t Nuevo email del usuario: ").lower().strip()
                        password = getpass.getpass("\t\t Nueva contraseña del usuario: ").strip()
                        proceso = usuarios.modificarUsuario(id_usuario_mod,nombre, apellidos, email, password)
                        if proceso:
                            print(f"\n\t\t✅ El usuario con ID {id_usuario_mod} ha sido modificado correctamente ✅")
                        else:
                            print(f"\n\t\t❌ No fue posible modificar el usuario con ID {id_usuario_mod}, intentelo mas tarde ❌")
                        funciones.esperarTecla()
                    elif respuesta == "no":
                        print("⭕ Cancelando...")
                else:
                    print("\n\t\t❌ No hay usuarios registrados ❌")
                    funciones.esperarTecla()

            case "7":
                funciones.borrarPantalla()
                print("\t\t🗑 ..:: Eliminar producto ::.. 🗑")
                productos_lista = productos.mostrarProductos()
                if len(productos_lista) >0:
                    print(f"\n{'ID':<6}|{'Nombre':<20}|{'Descripcion':<46}|{'Precio':<20}")
                    print("-" * 92)
                    for producto in productos_lista:
                        print(f"{producto[0]:<6}|{producto[1]:<20}|{producto[2]:<46}|{producto[3]:<20}")
                        print("-" * 92)
                    respuesta = input("\n\t\t⚠ ¿Deseas eliminar un producto? (si/no): ").lower().strip()
                    if respuesta == "si":
                        id_producto_del = int(input("\t\t👉 Ingresa el ID del producto a eliminar: "))
                        proceso = productos.eliminarProducto(id_producto_del)
                        if proceso:
                            print(f"\n\t\t✅ El producto con ID {id_producto_del} ha sido eliminado correctamente ✅")
                        else:
                            print(f"\n\t\t❌ No fue posible eliminar el producto con ID {id_producto_del}, intentelo mas tarde ❌")
                        funciones.esperarTecla()
                    elif respuesta == "no":
                        print("⭕ Cancelando...")
                    else:
                        print("⚠ Opción no válida ⚠")  
                else:
                    print("\n\t\t❌ No hay productos registrados ❌")
                    funciones.esperarTecla()

            case "8":
                funciones.borrarPantalla()
                print("\t\t🗑 ..:: Eliminar vendedor ::.. 🗑")
                usuarios_lista = usuarios.mostrarUsuarios()
                if len(usuarios_lista) >0:
                    print(f"\n{'ID':<6}|{'Fecha registro':<18}|{'Nombre':<13}|{'Apellido':<13}|{'Email':<30}")
                    print("-" * 92)
                    for usuario in usuarios_lista:
                        print(f"{usuario[0]:<6}|{usuario[5]}        |{usuario[1]:<13}|{usuario[2]:<13}|{usuario[3]:<30}")
                        print("-" * 92)
                    respuesta = input("\n\t\t⚠ ¿Deseas eliminar un vendedor? (si/no): ").lower().strip()
                    if respuesta == "si":
                        id_usuario_del = int(input("\t\t👉 Ingresa el ID del vendedor a eliminar: "))
                        proceso = usuarios.eliminarUsuario(id_usuario_del)
                        if proceso:
                            print(f"\n\t\t✅ El vendedor con ID {id_usuario_del} ha sido eliminado correctamente ✅")
                        else:
                            print(f"\n\t\t❌ No fue posible eliminar el vendedor con ID {id_usuario_del}, intentelo más tarde ❌")
                        funciones.esperarTecla()
                    elif respuesta == "no":
                        print("⭕ Cancelando...")
                    else:
                        print("⚠ Opción no válida ⚠")  
                else:
                    print("\n\t\t❌ No hay vendedores registrados ❌")
                    funciones.esperarTecla()

            case "9":
                funciones.borrarPantalla()
                print("\t\t💵 ..:: Ventas por vendedor ::.. 💵")
                ventas_por_vendedor = ventas.mostrarVentasPorVendedor()
                if ventas_por_vendedor:
                    for vendedor_data in ventas_por_vendedor:
                        print(f"\n\t\t === Vendedor: {vendedor_data['vendedor']} ===")
                        if vendedor_data['ventas']:
                            print(f"\n{'ID':<15}|{'ID vendedor':<15}|{'Cantidad':<15}|{'ID producto':<15}|{'Producto':<20}|{'Total':<15}|{'Fecha':<20}")
                            print("-" * 106)
                            for venta in vendedor_data['ventas']:
                                print(f"{venta[0]:<15}|{venta[1]:<15}|{venta[2]:<15}|{venta[3]:<15}|{venta[4]:<20}|{venta[5]:<15}|{venta[6]}")
                                print("-" * 106)
                        else:
                            print("\n\t\t❌ No hay ventas registradas para este vendedor ❌")
                    
                    exportar = input("\n\t👉 ¿Exportar a Excel? (si/no): ").lower().strip()
                    if exportar == "si":
                        # Preparamos los datos para exportar
                        datos_exportar = []
                        columnas = ["ID Venta", "ID Vendedor", "Cantidad", "ID Producto", "Producto", "Total", "Fecha"]
                        
                        for vendedor_data in ventas_por_vendedor:
                            for venta in vendedor_data['ventas']:
                                datos_exportar.append(venta)
                        
                        if datos_exportar:
                            funciones.exportar_a_excel("ventas_por_vendedor", datos_exportar, columnas, "Ventas por Vendedor")
                    
                    funciones.esperarTecla()
                else:
                    print("\n\t\t❌ No hay ventas registradas ❌")
                    funciones.esperarTecla()
            
            case "10" | "SALIR":
                permanecer=False
                print("🚪 Saliendo del sistema...")
            case _:
                print("⚠ Opción no válida ⚠")

def vendedor(usuario_id,nombre,apellidos):
    permanecer=True
    while permanecer:
        funciones.borrarPantalla()
        print(f"\n\t\t..:: Bienvenido {nombre} {apellidos} ::..")
        print("\t\t📄 ..:: Menú de Vendedor ::.. 📄")
        opcion=funciones.vendedor()
        match opcion:
                case "1":
                    funciones.borrarPantalla()
                    print("\t\t📝 ..:: Agregar una venta ::.. 📝")
                    agprod=input("Deseas agregar una venta al sistema (si/no) :").lower().strip()
                    if agprod == "si":
                        productos_lista = productos.mostrarProductos()
                        if len(productos_lista) >0:
                            print(f"\n{'ID':<6}|{'Nombre':<20}   |   {'ID':<6}|{'Nombre':<20}   |   {'ID':<6}|{'Nombre':<20}")
                            print("-" * 92)
                            for producto in productos_lista:
                                print(f"{producto[0]:<6}|{producto[1]:<20}|{producto[2]:<46}|{producto[3]:<20}")
                                print("-" * 92)
                            id_producto_vend = int(input("\n\t\t Ingresa el ID del producto a vender: "))
                            if len(productos_lista) >0:
                                for producto in productos_lista:
                                    if producto[0] == id_producto_vend:
                                        nombre_producto_vend = producto[1]
                                        precio_producto_vend = producto[3]
                                        break
                            cantidad = int(input("\t\t👉 Ingresa la cantidad a vender: "))
                            venta_crear = ventas.crearventa(usuario_id, cantidad, id_producto_vend,  nombre_producto_vend, precio_producto_vend)
                            if venta_crear:
                                print(f"\n\t\t✅ La venta de {cantidad} unidades del producto {nombre_producto_vend} se ha registrado correctamente ✅")
                            else:
                                print(f"\n\t\t❌ No fue posible registrar la venta del producto {nombre_producto_vend}, intentelo mas tarde ❌")
                            funciones.esperarTecla()  
                        else:
                            print("\n\t\t❌ No hay productos disponinbles para la venta ❌")
                            funciones.esperarTecla()

                    elif agprod == "no":
                        print("⭕ Cancelando...")
                        funciones.esperarTecla()
                    else:
                        print("⚠ Opción no válida ⚠")

                case "2":
                    funciones.borrarPantalla()
                    print("\t\t💵 ..:: Ventas Registradas ::.. 💵")
                    ventas_lista = ventas.mostrarVentas()
                    if len(ventas_lista) >0:
                        print(f"\n{'ID':<15}|{'ID vendedor':<15}|{'Cantidad':<15}|{'ID producto':<15}|{'Producto':<20}|{'Total':<15}|{'Fecha':<20}")
                        print("-" * 106)
                        for venta_unidad in ventas_lista:
                            print(f"{venta_unidad[0]:<15}|{venta_unidad[1]:<15}|{venta_unidad[2]:<15}|{venta_unidad[3]:<15}|{venta_unidad[4]:<20}|{venta_unidad[5]:<15}|{venta_unidad[6]}")
                            print("-" * 106)
                        exportar = input("\n\t👉 ¿Exportar a Excel? (si/no): ").lower().strip()
                        if exportar == "si":
                            columnas = ["ID Venta", "ID Vendedor", "Cantidad", "ID Producto", "Producto", "Total", "Fecha"]
                            funciones.exportar_a_excel("ventas", ventas_lista, columnas, "Ventas")
                        funciones.esperarTecla()  
                    else:
                        print("\n\t\t❌ No hay Ventas registrados ❌")
                        funciones.esperarTecla()

                case "3":
                    funciones.borrarPantalla()
                    print("\t\t🔁 ..:: Modificar venta ::.. 🔁")
                    ventas_lista = ventas.mostrarVentas()
                    if len(ventas_lista) > 0:
                        print(f"\n{'ID':<15}|{'ID vendedor':<15}|{'Cantidad':<15}|{'ID producto':<15}|{'Producto':<20}|{'Total':<15}|{'Fecha':<20}")
                        print("-" * 106)
                        for venta_unidad in ventas_lista:
                            print(f"{venta_unidad[0]:<15}|{venta_unidad[1]:<15}|{venta_unidad[2]:<15}|{venta_unidad[3]:<15}|{venta_unidad[4]:<20}|{venta_unidad[5]:<15}|{venta_unidad[6]}")
                            print("-" * 106)

                        respuesta = input("\n\t\t⚠ ¿Deseas modificar una venta? (si/no): ").lower().strip()
                        if respuesta == "si":
                            id_venta_mod = int(input("\t\t👉 Ingresa el ID de la venta a modificar: "))
                            new_prod=input("\t\t⚠ Deseas modificar el producto vendido (si/no): ").lower().strip()
                            if new_prod == "si":
                                productos_lista = productos.mostrarProductos()
                                if len(productos_lista) >0:
                                    print(f"\n{'ID':<6}|{'Nombre':<20}   |   {'ID':<6}|{'Nombre':<20}   |   {'ID':<6}|{'Nombre':<20}")
                                    print("-" * 92)
                                    for producto in productos_lista:
                                        print(f"{producto[0]:<6}|{producto[1]:<20}|{producto[2]:<46}|{producto[3]:<20}")
                                        print("-" * 92)
                                    id_producto_vend = int(input("\n\t\t👉 Ingresa el ID del nuevo producto vendido: "))
                                    if len(productos_lista) >0:
                                        for producto in productos_lista:
                                            if producto[0] == id_producto_vend:
                                                nombre_producto_vend = producto[1]
                                                precio_producto_vend = producto[3]
                                                break
                                else:
                                    print("\n\t\t❌ No hay productos disponinbles para la venta ❌")
                                    funciones.esperarTecla()
                            elif new_prod == "no":
                                for venta_unidad in ventas_lista:
                                    if venta_unidad[0] == id_venta_mod:
                                        id_producto_vend = venta_unidad[3]
                                        nombre_producto_vend = venta_unidad[4]
                                        precio_producto_vend = venta_unidad[5]
                                        break
                            nueva_cantidad = int(input("\t\t Nueva cantidad de productos vendidos: "))
                            proceso = ventas.modificarVenta(id_venta_mod,nueva_cantidad, id_producto_vend, nombre_producto_vend,precio_producto_vend)
                            if proceso:
                                print(f"\n\t\t✅ La venta con ID {id_venta_mod} ha sido modificada correctamente ✅")
                            else:
                                print(f"\n\t\t❌ No fue posible modificar la venta con ID {id_venta_mod} ❌")
                            funciones.esperarTecla()
                        elif respuesta == "no":
                            print("⭕ Cancelando...")
                            funciones.esperarTecla()
                    else:
                        print("\n\t\t❌ No hay ventas registradas ❌")
                        funciones.esperarTecla()
                case "4":
                    funciones.borrarPantalla()
                    print("\t\t🗑 ..:: Eliminar venta ::.. 🗑")
                    ventas_lista = ventas.mostrarVentas()
                    if len(ventas_lista) > 0:
                        print(f"\n{'ID':<15}|{'ID vendedor':<15}|{'Cantidad':<15}|{'ID producto':<15}|{'Producto':<20}|{'Total':<15}|{'Fecha':<20}")
                        print("-" * 106)
                        for venta_unidad in ventas_lista:
                            print(f"{venta_unidad[0]:<15}|{venta_unidad[1]:<15}|{venta_unidad[2]:<15}|{venta_unidad[3]:<15}|{venta_unidad[4]:<20}|{venta_unidad[5]:<15}|{venta_unidad[6]}")
                            print("-" * 106)

                        respuesta = input("\n\t\t⚠ ¿Deseas eliminar una venta? (si/no): ").lower().strip()
                        if respuesta == "si":
                            id_venta_del = int(input("\t\t👉 Ingresa el ID de la venta a eliminar: "))
                            proceso = ventas.eliminarVenta(id_venta_del)
                            if proceso:
                                print(f"\n\t\t✅ La venta con ID {id_venta_del} ha sido eliminada correctamente ✅")
                            else:
                                print(f"\n\t\t❌ No fue posible eliminar la venta con ID {id_venta_del} ❌")
                            funciones.esperarTecla()
                        elif respuesta == "no":
                            print("⭕ Cancelando...")
                            funciones.esperarTecla()
                    else:
                        print("\n\t\t❌ No hay ventas registradas ❌")
                        funciones.esperarTecla()
                case "5" | "SALIR":
                    permanecer=False
                    print("🚪 Saliendo del sistema...")
                case _:
                    print("⚠ Opción no válida ⚠")

if __name__ == "__main__":
    main()
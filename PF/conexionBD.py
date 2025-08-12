import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_proyecto_crepas"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde ...") 


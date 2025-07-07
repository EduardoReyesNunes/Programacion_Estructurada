import agenda

def main():
    datos = {}  
    while True:
        opcion = agenda.menu()
        match opcion:
            case "1":
                datos = agenda.agregar_contacto(datos)
            case "2":
                agenda.mostrar_contactos(datos)
            case "3":
                agenda.buscar_contacto(datos)
            case "4":
                datos = agenda.modificar_contacto(datos)
            case "5":
                datos = agenda.eliminar_contacto(datos)
            case "6":
                print("\nSaliendo del sistema...")
                break
            case _:
                print("\nOpción no válida")
                agenda.esperar_tecla()

if __name__ == "__main__":
    main()
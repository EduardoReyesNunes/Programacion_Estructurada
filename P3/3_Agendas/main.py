import agenda

def main():
    agenda_contacto = {}
    op = True
    while op:
        agenda.borrarPantalla()
        op = agenda.menu_principal()
        match op:
            case "1":
                agenda.agregarContacto(agenda_contacto)
                agenda.esperarTecla()
            case "2":
                agenda.mostrarContactos(agenda_contacto)
                agenda.esperarTecla()
            case "3":
                agenda.buscarContacto(agenda_contacto)
                agenda.esperarTecla()
            case "4":
                agenda.modificarContacto(agenda_contacto)
                agenda.esperarTecla()
            case "5":
                agenda.eliminarContacto(agenda_contacto)
                agenda.esperarTecla()
            case "6":
                agenda.borrarPantalla()
                print("🚪 .::Terminaste de usar el programa::. 🚪")
                op = False
            case _:
                op = True
                print("⚠️ ::Opción no válida, vuelva a intentarlo:: ⚠️")
                agenda.esperarTecla()

if __name__ == "__main__":
    main()
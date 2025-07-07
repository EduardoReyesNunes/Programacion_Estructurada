import os

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

def esperar_tecla():
    input("Presione cualquier tecla para continuar")

def menu():
    clean_screen()
    print("\n\t\t..::📒 Sistema de gestión de agenda de contactos ::..\n")
    opcion = input(f"""
    \t\t1️⃣  Agregar contacto
    \t\t2️⃣  Mostrar contactos
    \t\t3️⃣  Buscar contacto
    \t\t4️⃣  Modificar contacto
    \t\t5️⃣  Eliminar contacto
    \t\t6️⃣  Salir 🚪

    \t\tSeleccione una opción: (1-6) """)
    return opcion

def agregar_contacto(agenda):
    clean_screen()
    print("..::📒 Agregar contacto ::..")
    nombre = input("Nombre del contacto: ").upper().strip()
    
    if nombre in agenda:
        print("\n⚠️ Este contacto ya existe")
    else:
        telefono = input("Teléfono del contacto: ").strip()
        email = input("Email del contacto: ").upper().strip()
        agenda[nombre] = [telefono, email]
        print(f"\n✅ Contacto {nombre} agregado correctamente")
    
    esperar_tecla()
    return agenda

def mostrar_contactos(agenda):
    clean_screen()
    print("..::📒 Lista de contactos ::..")
    
    if not agenda:
        print("\nNo hay contactos en la agenda")
    else:
        print(f"\n{'Nombre':<20}{'Teléfono':<20}{'Email':<20}")
        print("-" * 60)
        for nombre, datos in agenda.items():
            print(f"{nombre:<20}{datos[0]:<20}{datos[1]:<20}")
        print("-" * 60)
    
    esperar_tecla()

def buscar_contacto(agenda):
    clean_screen()
    print("..::🔍 Buscar contacto ::..")
    
    if not agenda:
        print("\nNo hay contactos en la agenda")
    else:
        nombre = input("\nNombre del contacto a buscar: ").upper().strip()
        
        if nombre in agenda:
            print(f"\n{'Nombre':<20}{'Teléfono':<20}{'Email':<20}")
            print("-" * 60)
            print(f"{nombre:<20}{agenda[nombre][0]:<20}{agenda[nombre][1]:<20}")
            print("-" * 60)
        else:
            print("\n❌ Contacto no encontrado")
    
    esperar_tecla()

def modificar_contacto(agenda):
    clean_screen()
    print("..::✏️ Modificar contacto ::..")
    
    if not agenda:
        print("\nNo hay contactos en la agenda")
    else:
        nombre = input("\nNombre del contacto a modificar: ").upper().strip()
        
        if nombre in agenda:
            print(f"\n{'Nombre':<20}{'Teléfono':<20}{'Email':<20}")
            print("-" * 60)
            print(f"{nombre:<20}{agenda[nombre][0]:<20}{agenda[nombre][1]:<20}")
            print("-" * 60)
            
            resp = input("\n¿Deseas modificar este contacto? (S/N): ").upper().strip()
            if resp == "S":
                nuevo_tel = input("Nuevo teléfono: ").strip()
                nuevo_email = input("Nuevo email: ").upper().strip()
                agenda[nombre] = [nuevo_tel, nuevo_email]
                print("\n✅ Contacto modificado correctamente")
        else:
            print("\n❌ Contacto no encontrado")
    
    esperar_tecla()
    return agenda

def eliminar_contacto(agenda):
    clean_screen()
    print("..::🗑️ Eliminar contacto ::..")
    
    if not agenda:
        print("\nNo hay contactos en la agenda")
    else:
        nombre = input("\nNombre del contacto a eliminar: ").upper().strip()
        
        if nombre in agenda:
            print(f"\n{'Nombre':<20}{'Teléfono':<20}{'Email':<20}")
            print("-" * 60)
            print(f"{nombre:<20}{agenda[nombre][0]:<20}{agenda[nombre][1]:<20}")
            print("-" * 60)
            
            resp = input("\n¿Estás seguro de eliminar este contacto? (S/N): ").upper().strip()
            if resp == "S":
                agenda.pop(nombre)
                print("\n✅ Contacto eliminado correctamente")
        else:
            print("\n❌ Contacto no encontrado")
    
    esperar_tecla()
    return agenda
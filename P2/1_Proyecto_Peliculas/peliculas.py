import os

peliculas=["ll","llo","ll"]
pase="hola"

def esperatecla():
    input("\n\t...Oprime cualquier tecla para continuar...")

def borrarpantalla():
    os.system("cls")

def agregarpelicula():
    borrarpantalla()
    print("\t\t..::Agregar Película::.. \n")
    peliculas.append(input("\tIngresa el nombre de la película: ").lower().strip())
    print("\t\t..::La operacion se realizo con exito::..")

def borarpelicula():
    borrarpantalla()
    print("\n\t::: Borrar Películas :::\n")
    pelicula_buscar = input("Ingrese el nombre de la película a borrar: ").upper().strip()
    encontro = 0
    
    if not (pelicula_buscar in peliculas):
        print("\n\t\t¡No se encuentra la película!")
    else:
        resp = "si"
        while pelicula_buscar in peliculas:
            resp = input("¿Deseas borrar la película del sistema? (Si/No): ").lower()
            if resp == "si":
                posicion = peliculas.index(pelicula_buscar)
                print(f"\nLa película que se borró es: {pelicula_buscar} y estaba en la casilla: {posicion+1}")
                peliculas.remove(pelicula_buscar)
                encontro += 1
                print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
                
            print(f"\n\tSe borró: {encontro} película(s) con este título")

def modificarpelicula():
    borrarpantalla()
    print("..::Modificar Películas::.. ")

def consultarpelicula():
    borrarpantalla()
    print("\t\t..::Consultar o mostrar Película::.. ")
    if len(peliculas)==0:
        print("\n\t\tEl catalogo de peliculas se encuentra vacio")
    else:
        for i in range(0,len(peliculas)):
            print(f"\t\t{i+1}.- {peliculas[i]}")

def buscarpelicula():
    borrarpantalla()
    print("\n\t:::Buscar-Películas:::\n")
    película_buscar = input("Ingrese-el.nombre.de-la-película-a-buscar::").upper().strip()
    encontro = 0

    if not (película_buscar in peliculas):
        print("\n\t\t::No-se-encuentra-la-película!")
    else:
        for i in range(0, len(peliculas)):
            if película_buscar == peliculas[i]:
                print(f"\nLa-película-{película_buscar}-si-la-tenemos-y-esta-en-la-casi[la:{i+1}]")
                encontro += 1
        print(f"\nTenemos-{encontro}-película(s).con-este-título")
        print("\n\t\t:::·ILA·OPERACIÓN-SE-REALIZÓ-CON-EXÍTO!:::")
    esperatecla()

def vaciarpeliculas():
    borrarpantalla()
    input("\n\t Vaciar Lista de películas")
    resp=input("Deseas quitar TODAS la peliculas del sistema? (si/no)").lower().strip()
    if resp=="si" :
        contrasena=input("Para mayor seguridad ingresa la contraseña?")
        if contrasena==pase:
            peliculas.clear()
        else:
            input("Contraseña incorrecta,")
    elif resp=="no":
        input("La operacion se ha cacelado")
    else:
        input("Favor de responder correctamente")

from paquete1 import modulos

print(modulos.saludar("Daniel Contreras Ruano"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t.:: Agenda telefonica ::.\n\t\tNombre :{nom}\n\t\tTelefono :{tel}")
modulos.espereTecla()
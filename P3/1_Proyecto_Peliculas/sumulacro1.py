lista=[]

#lista=[34,23,34,10]

def almacenar():
   resp="si"
   while resp=="si":
        lista.append(float(input("Ingresa Numero: ").strip()))
        resp=input("¿Deseas ingresar otro numero? (Si/No):  ").lower().strip()

def buscar():
  numero=float(input("Ingresa un numero: ").strip())
  if numero in lista:
      for i in lista:
        if numero==lista[i]:
           print(f"El numero {numero} se encuentra posición: {i}")
  else:
     print("El numero no esta")   

almacenar()
buscar()
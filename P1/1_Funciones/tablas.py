'''
crear un programa que calcule e imprima la tabla de multiplicar del 2

restricciones:
1.-sin estructuras de control
2.- sin restricciones
'''
import os

os.system("cls")
multi=int(input(" Que tabla deseas multiplicar? "))
tabla = f"\n\t{multi} X 1 = {multi*1}\n\t{multi} X 2 = {multi*2}\n\t{multi} X 3 = {multi*3}\n\t{multi} X 4 = {multi*4}\n\t{multi} X 5 = {multi*5}\n\t{multi} X 6 = {multi*6}\n\t{multi} X 7 = {multi*7}\n\t{multi} X 8 = {multi*8}\n\t{multi} X 9 = {multi*9}\n\t{multi} X 10 = {multi*10}"
print(tabla)

'''
crear un programa que calcule e imprima la tabla de multiplicar del 2

restricciones:
1.-con estructuras de control
2.- sin funciones
'''

multi=int(input(" Que tabla deseas multiplicar? "))
for i in range(1,11,1):
    print(f"\t{multi} X {i} = {multi*i}")

'''
crear un programa que calcule e imprima la tabla de multiplicar del 2

restricciones:
1.-con estructuras de control
2.- con funciones
'''
def multiplicacion (num):
    multi=num
    for i in range(1,11,1):
        print(f"\t{multi} X {i} = {multi*i}")

num=int(input(" Que tabla deseas multiplicar? "))
multiplicacion(num)
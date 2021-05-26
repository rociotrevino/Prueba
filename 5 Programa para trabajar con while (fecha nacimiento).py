#programa para trabajar con while
#preguntar la edad
import os
os.system('cls')
print('Programa que calcula la fecha de nacimiento')
nombre=str(input('\n\t\tDime tu nombre    :'))
edad=int(input('\n\t\t¿Cuántos años tienes  ?  '))
while(edad<0 or edad>100):
    os.system('cls')
    print('Esa Edad NO es válida')
    edad=int(input('\n\t\t¿Cuántos años tienes ?   '))
else:
    fecha=str(input('\n\t\t¿En que fecha cumples años (Día y Mes):  '))
    year=2021-edad
    os.system('cls')
    print('\n\t',nombre, 'Tu fecha de nacimiento es :   ',fecha, year)
#Leer numeros enteros positivos de teclado, hasta que el usuario ingrese el 0
#mostrar la sumatoria de todos los números enteros ingresados.
suma=0
print('\n\nPrograma que lee números enteros positivos y realiza la sumatoria ')
print('\n Hasta que el usuario teclee el valor de 0')
numero=int(input('\n\t\tCapture un numero entero  : '))
if numero < 0:
    print("\n\t\t¡El numero no es positivo!")
    numero=int(input('\n\t\tCapture un numero entero  : '))
while (numero!=0):
    suma=numero+suma
    numero=int(input('\n\t\tCapture un numero entero  : '))
    if numero < 0:
        print("\n\t\t¡El numero no es positivo!")
        numero=int(input('\n\t\tCapture un numero entero  : '))
print('\n\t\tLa Suma Total es :  ',suma)
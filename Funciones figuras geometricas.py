#Programa que calcula el área de diversas figuras
def Areacuadrado():
    print('\n\tPara calcular el área de un Cuadrado')
    lado=float(input('\n\t\t Medida de un lado  '))
    area=lado*lado
    return area
def Areacirculo():
    print('\n\t Para calcular el área de un Círculo')
    radio=float(input('\n\t Medida del radio  '))
    area=3.1416*radio
    return area
def Arearectangulo():
    print('\n\t Para calcular el área de un Rectángulo')
    base=float(input('\n\t Medida de la base  '))
    altura=float(input('\n\t Medida de la altura  '))
    area=base*altura
    return area
def Areatriangulo():
    print('\n\t Para calcular el área de un Triángulo')
    base=float(input('\n\t Medida de la base       '))
    altura=float(input('\n\t Medida de la altura   '))
    area=base*altura/2
    return area
def Arearombo():
    print('\n\t Para calcular el área de un Rombo')
    diagmayor=float(input('\n\t Medida de la diagonal mayor  '))
    diagmenor=float(input('\n\t Medida de la diagonal menor  '))
    area=diagmayor*diagmenor/2
    print('\n\t El área del Rombo es:   ',area)
print('\n PROGRAMA QUE CALCULA EL ÁREA DE FIGURAS GEOMÉTRICAS')
print('\n\t\t\t MENÚ DE FIGURAS')
print('\n\t\t\t 1. Cuadrado')
print('\n\t\t\t 2. Círculo')
print('\n\t\t\t 3. Rectángulo')
print('\n\t\t\t 4. Triángulo')
print('\n\t\t\t 5. Rombo')
opcion=int(input('\n\t Capture la opción     '))
if (opcion==1):
    print('\t\t El area del cuadrado es: ',(Areacuadrado()))
elif (opcion==2):
    print('\n\t\t El área del Círculo es:   ',(Areacirculo()))
elif (opcion==3):
    print('\n\t\t El área del Rectángulo es:   ',(Arearectangulo()))
elif (opcion==4):
    print('\n\t El área del Triángulo es:   ',(Areatriangulo()))
elif (opcion==5):
    Arearombo()
else:
    print('\n\ ERROR, NÚMERO NO VÁLIDO, SÓLO <1,2,3,4,5>')
    print('\t Ejecute nuevamente el programa')



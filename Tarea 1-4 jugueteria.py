#Programa que calcula el peso de paquete enviado y el costo 
print ("JUGUETERIA REGIOMONTANA")
print ("CAPTURE SU PEDIDO/CANTIDAD")
payasos=int(input ("Payasos   "))
muñecas=int(input ("Muñecas   "))
peso=(payasos*112+muñecas*75)
kilos=(peso/1000)
precio=0
if kilos>55:
    pesocobro=float(kilos/55)
    precio =(pesocobro*115)
    #Falta aplicar la condicion que solo cobre en multiples de peso de 55 kilos (por cada 55 kilos el costo es de $115)
print ("El peso Total del pedido es ... ",kilos)
print ("El pago es $", precio)
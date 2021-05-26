#Programa para verificar palabra palindromo
print("Este programa te indicará si la palabra que escribes es Palíndromo")
palabra = input ("Ingresa una palabra: ")
izqpalabra=palabra
palabra=list(palabra)
izqpalabra=list(izqpalabra)
izqpalabra.reverse()
if palabra==izqpalabra:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")



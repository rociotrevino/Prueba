#Programa que almacena una cadena de caracteres (contraseña) y pregunta al usuario por la contraseña, e imprima si coincide o no
contra="hola"
nuevacontra=str(input("Escriba la contraseña :   "))
nuevacontra=nuevacontra.lower()
if (contra==nuevacontra.lower()):
   print("Contraseña válida")
else:
   print("Contraseña inválida")
#programa que solcita nombre, peso, longitud de un dinosaurio
nom=str(input("¿Cómo se llama el Dinosaurio   ?"))
peso=float(input("¿Cuánto pesa en Kilos      ? "))
lon=float(input("¿Cuánto mide en pies        ? "))
kg=float(peso*0.454)
m=float(lon*3.28)
print(str(nom), "es un dinosaurio que mide", m, "metros y pesa ",kg, "kilogramos")
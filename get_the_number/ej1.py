import random

numeroOculto=random.randrange(1,10)
numeroUsuario=int(input("Dame un numero del 1 al 10: "))

if numeroOculto == numeroUsuario:
    print("Lo has adivinado")
elif numeroUsuario < numeroOculto:
    print("Tu numero es menor que el oculto")
else:
    print("Tu numero es mayor que el oculto")
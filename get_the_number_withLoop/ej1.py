import random

numeroOculto=random.randrange(1,10)
numeroUsuario=int(input("Dame un numero del 1 al 10: "))

while numeroUsuario != numeroOculto:
    if numeroUsuario < numeroOculto:
        numeroUsuario=int(input("Tu numero es menor que el oculto "))
    elif numeroUsuario > numeroOculto:
        numeroUsuario=int(input("Tu numero es mayor que el oculto "))

print("Has acertado el numero")

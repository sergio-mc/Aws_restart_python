# Añadir: 0
# Pagar: 1
# Salir: 2

facturas = {
    "1":"40",
    "2":"30"
}

userInput = ""

cantidadCobrada = 0
cantidadPendiente = 0

while userInput != "3":
    userInput = input("¿Que desea hacer? Añadir: 0 / Pagar: 1 / Ver Facturas: 2 / Salir: 3 ")

    if userInput == "0":
        numero = input("Dime el numero de factura: ")
        coste = input("Dime el coste de la factura: ")
        facturas[numero] = coste
    elif userInput == "1":
        numeroPagar = input("Dime el numero de la factura a pagar: ")
        try:
            cantidadCobrada += int(facturas[numeroPagar])
            facturas.pop(numeroPagar)
        except:
            print("La factura no existe. Volviendo atras")
    elif userInput == "2":
        print(facturas)
    else:
        print("Selecciona una opcion correcta")
    
    for i in facturas:
        cantidadPendiente = int(facturas[i])
    
    print("Cantidad total a cobrar: " + str(cantidadPendiente))
    print("Cantidad total cobrada: " + str(cantidadCobrada))

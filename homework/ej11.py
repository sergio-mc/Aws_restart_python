rentaAnual = int(input("Dime tu renta anual: "))

if rentaAnual < 10000:
    print("Tipo impositivo del 5%")
elif rentaAnual > 10000 and rentaAnual < 20000:
    print("Tipo impositivo del 15%")
elif rentaAnual > 20000 and rentaAnual < 35000:
    print("Tipo impositivo del 20%")
elif rentaAnual > 35000 and rentaAnual < 60000:
    print("Tipo impositivo del 30%")
elif rentaAnual > 60000:
    print("Tipo impositivo del 45%")
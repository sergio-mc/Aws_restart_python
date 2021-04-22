def pedirNumero():
    num = int(input("Dame un numero entre el 1 al 11: "))

    tabla = {}

    if num >= 1:
        try:
            f = open("tabla-" + str(num), "x")
        except:
            f = open("tabla-" + str(num), "w")
        
        for i in range(0,10):
            tabla[str(i) + "*" + str(num)] = i * num
        f.write(str(tabla))
        f.close

pedirNumero()

listin = {}

userInput = ""

while userInput != "5":

    try:
        with open("listin", "r") as f:
            for line in f:
                linerStrip = line.rstrip(",\n")
                lineSplited = linerStrip.split(",")
                listin[lineSplited[0]] = lineSplited[1]
    except:
        print("No se pudo leer listin porque no existe")

    userInput = input("""
    ---------------------------------
    # Crear fichero listin: 1
    # Consultar tlf cliente: 2
    # Añadir tlf nuevo cliente: 3
    # Eliminar tlf de un cliente: 4
    # Terminar : 5
    ---------------------------------- 
    
    """)
    
    
    if userInput == "1":
        try:
            f = open("listin", "x")
            for i in listin:
                f.write(str(i) + "," +  str(listin[i]) + "\n")
                f.close
        except:
            f = open("listin", "w")
            for i in listin:
                f.write(str(i) + "," + str(listin[i]) + "\n")
                f.close
        
        

    elif userInput == "2":
        userPhoneConsult = input("Dime el nombre del telefono a consultar: ")
        for cliente in listin:
            if userPhoneConsult == cliente:
                print(listin[cliente])

    elif userInput == "3":
        addUserName = input("Dime el nombre del nuevo cliente: ")
        addUserPhone = input("Dime el telefono del nuevo cliente: ")
        f = open("listin", "a")
        f.write(addUserName + "," +  addUserPhone + "\n")
        f.close()

    elif userInput == "4":
        userRemove = input("Dime el nombre del usuario a eliminar: ")
        
        try:
            # leer archivo y guardarmelo para luego al usar open("w") y me vacie el listin poderlo rellenar con lo que tenia antes
            with open("listin", "r") as x:
                linesReadListin = x.readlines()
            with open("listin", "w") as f:
                for line in linesReadListin:
                    linerStrip = line.partition(",")
                    print(linerStrip[0])
                    if linerStrip[0] != userRemove:
                        f.write(line)
            f.close()  
        except:
            print("error")
                # if lineSplited[0] == userRemove:

                
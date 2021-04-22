

listin = {
    "sergio":"640103006",
    "cristina":"123134908",
    "patricia":"765434321",
    "javier":"002244330",
}

userInput = ""

while userInput != "5":

    f = open("listin", "r")
    line = f.readline()
    lineSplited = line.split(",")
    for i in lineSplited:
        print(i)

    userInput = input("""
    ---------------------------------
    # Crear fichero con listin: 1
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
        
        

    # elif userInput == "2":
        

        

        

    # elif userInput == "3":
        
        
        
    # elif userInput == "4":
        
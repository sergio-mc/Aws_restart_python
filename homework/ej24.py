# Añadir Cliente: 1
# Eliminar cliente: 2
# Mostrar cliente: 3
# Listar clientes : 4
# Listar clientes preferentes: 5
# Terminar : 6


# clientes = {
#     "53204303B":{
#         "nombre":"Sergio",
#         "direccion":"Leganes",
#         "telefono":"640103006",
#         "correo":"sergiodev0106@gmail.com",
#         "preferente":True
#     },
# }

clientes = {
    "53204303B":{
        "nombre":"Sergio",
        "direccion":"Leganes",
        "telefono":"640103006",
        "correo":"sergiodev0106@gmail.com",
        "preferente":"no"
    },
    "24564354F":{
        "nombre":"Cristina",
        "direccion":"Madrid",
        "telefono":"601231325",
        "correo":"cristina@gmail.com",
        "preferente":"si"
    },
}

userInput = ""

while userInput != "6":

    userInput = input("""
    ---------------------------------
    # Añadir Cliente: 1
    # Eliminar cliente: 2
    # Mostrar cliente: 3
    # Listar clientes : 4
    # Listar clientes preferentes: 5
    # Terminar : 6 
    ---------------------------------- 
    
    """)
    
    
    if userInput == "1":
        nif = input("Dime tu NIF: ")
        nombre = input("Dime tu nombre: ")
        direccion = input("Dime tu direccion: ")
        telefono = input("Dime tu telefono: ")
        correo = input("Dime tu correo: ")
        preferente = input("Dime si eres preferente: ")
        
        dic2 = {
            "nombre" : nombre,
            "direccion" : direccion,
            "telefono" : telefono,
            "correo" : correo,
            "preferente" : preferente
        }
        
        clientes[nif] = dic2

    elif userInput == "2":

        nifDelete = input("Dime el NIF del cliente a eliminar: ")

        try:
            clientes.pop(nifDelete)
            print("Cliente eliminado con exito")
        except:
            print("El cliente no existe. Volviendo atras")

    elif userInput == "3":
        
        nifGet = input("Dime el NIF del cliente a obtener datos: ")

        try:
            print(clientes[nifGet])
        except:
            print("El cliente no existe. Volviendo atras")
        
    elif userInput == "4":

        for i in clientes:
            print("NIF: " + i + " | Nombre: " + clientes[i]["nombre"] )

    elif userInput == "5":
        
        for i in clientes:
            if clientes[i]["preferente"] == "si":
                print("NIF: " + i + " | Nombre: " + clientes[i]["nombre"] )
                
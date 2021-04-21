iVeg = ["Pimiento","Tofu"]
iNoVeg = ["Peperoni","Jamon","Salmon"]
i = ["Mozzarella", "Tomate"]

user = input("¿Quieres pizza vegetariana? si o no ")

if user == "si":
    userSelection = input("Escoge entre estos ingredientes: " + str(iVeg))
    if userSelection == "Pimiento":
        userI = iVeg[0]
    elif userSelection == "Tofu":
        userI = iVeg[1]
    print("La pizza es vegetariana y contiene los siguientes ingredientes: " + str(userI) + str(i))
else:
    userSelection = input("Escoge entre estos ingredientes: " + str(iNoVeg))
    if userSelection == "Peperoni":
        userI = iNoVeg[0]
    elif userSelection == "Jamon":
        userI = iNoVeg[1]
    elif userSelection == "Salmon":
        userI = iNoVeg[2]
    print("La pizza no es vegetariana y contiene los siguientes ingredientes: " + str(userI) + str(i))



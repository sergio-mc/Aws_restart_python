userInput = ""
articulos = {}

while userInput != "salir":
    item = input("Dime un articulo: ")
    price = input("Dime el precio del articulo: ")
    articulos[item] = price + "€"
    userInput = input("¿Desea continuar añadiendo articulos?")

print(articulos)

userInput = ""
articulos = {}
costeTotal = 0

while userInput != "salir":
    item = input("Dime un articulo: ")
    price = input("Dime el precio del articulo: ")
    articulos[item] = price
    userInput = input("¿Desea continuar añadiendo articulos? ")

for i in articulos:
    costeTotal += float(articulos[i])

print(costeTotal)
print(articulos)

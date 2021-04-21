name = input("Dime el nombre del producto: ")
price = float(input("Dime el precio del producto: "))
stock = int(input("Dime la cantidad del producto: "))

priceRounded = round(price, 2)
priceStr = str(priceRounded)
priceFill = priceStr.zfill(8)

stockStr = str(stock)
stockFill = stockStr.zfill(5)

totalCost = price * stock
totalCostRounded = round(totalCost, 2)
totalCostStr = str(totalCostRounded)
totalCostFill = totalCostStr.zfill(10)

toDisplay = "El producto {name} con precio unitario de {precuni}, stock de {stock} y precio total de {prectotal}".format(name = name, precuni = priceFill, stock = stockFill, prectotal = totalCostFill)
print(toDisplay)
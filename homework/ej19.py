divisas = {
    "Euros" : "€",
    "Dollar" : "$",
    "Yen" : "¥"
}

user = input("Elige una divisa entre estas: "+ str(divisas) + " ")
existe = False

for divisa in divisas:
    if divisa == user:
        print(divisas[divisa])
        existe = True

if existe == False:
    print("La divisa no existe")


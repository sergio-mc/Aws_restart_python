frase = input("Dime una frase: ")

fraseSplit = frase.split(" ")


fraseDic = dict.fromkeys(fraseSplit, 0)

for word in fraseSplit:
    if word in fraseSplit:
        fraseDic[word] += 1
    else:
        fraseDic[word] = 1

print(fraseSplit)
print(fraseDic)

# Dividir la frase entre las palabras e ir añadiendolas a un diccionario como clave y su frecuencia como valor
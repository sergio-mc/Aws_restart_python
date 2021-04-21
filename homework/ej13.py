number = int(input("Dame un numero: "))
counter = 1
imparList = ""

for i in range(1,number):
    if i % 2 != 0:
        imparList += str(i) + ","

# print(imparList, sep=',')
print(imparList)


    


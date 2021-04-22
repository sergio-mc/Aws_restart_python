name = input("Dime tu nombre: ")
age = input("Dime tu edad: ")
address = input("Dime tu direccion: ")
phone = input("Dime tu telefono: ")

user = {
    "name" : name,
    "age" : age,
    "address" : address,
    "phone" : phone,
}

print("{name} tiene {age} años, vive en {address} y su número de teléfono es {phone}".format(name = user.get("name"), age = user.get("age"), address = user.get("address"), phone = user.get("phone")))
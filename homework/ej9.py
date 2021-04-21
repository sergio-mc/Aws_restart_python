pwdDefault = "nic3"
pwd = str(input("Dime tu contraseña de acceso: "))
pwdLowerCase = pwd.lower()

if pwdLowerCase == pwdDefault:
    print("Contraseña correcta")
else:
    print("Contraseña erronea")


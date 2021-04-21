fecha = input("Dime tu fecha de nacimiento en formato dd/mm/aaaa : ")

fechaSplit = fecha.split("/")

dia = fechaSplit[0]
mes = fechaSplit[1]
año = fechaSplit[2]

if len(dia) < 2:
    dia = "0" + dia
if len(mes) < 2:
    mes = "0" + mes


print("Dia: " + dia)
print("Mes: " + mes)
print("Año: " + año)
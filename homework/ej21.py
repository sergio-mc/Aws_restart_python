fecha = input("Dime tu fecha de nacimiento en formato dd/mm/aaaa : ")

fechaSplit = fecha.split("/")

dia = fechaSplit[0]
mes = fechaSplit[1]
año = fechaSplit[2]

if len(dia) < 2:
    dia = "0" + dia
if len(mes) < 2:
    mes = "0" + mes

meses = {
    "01" : "Enero",
    "02" : "Febrero",
    "03" : "Marzo",
    "04" : "Abril",
    "05" : "Mayo",
    "06" : "Junio",
    "07" : "Julio",
    "08" : "Agosto",
    "09" : "Septiembre",
    "10" : "Octubre",
    "11" : "Noviembre",
    "12" : "Diciembre",
}

for i in meses:
    if i == mes:
        mes = meses[i]



print("Dia: " + dia)
print("Mes: " + mes)
print("Año: " + año)
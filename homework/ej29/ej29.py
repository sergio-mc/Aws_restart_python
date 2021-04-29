import csv

data = []
calificacion = {}
calificaciones = []

def firstLineCSV():
    with open('homework/ej29/calificaciones.csv', 'r') as file:
        first_line = file.readline().split(';')
        first_line_dic = []
        for i in first_line:
            first_line_dic.append(i.rstrip()) 
        # print('Primera Linea: ' + str(first_line_dic))

        reader = csv.reader(file, delimiter = ';')

        for row in reader:
            data.append(row)

        # print(data)


        for i in data:
            print(i)
            for index, value in enumerate(i):
                calificacion[first_line_dic[index]] = value
            # print(calificacion)
            calificaciones.append(calificacion)
            # print(calificaciones)
            
        print(calificacion)

        # print("Datos: " + str(data))
        

        # for d in data:
        #     cal


firstLineCSV()
        
    
# with open('homework/ej29/calificaciones.csv', 'r') as file:
#     reader = csv.reader(file, delimiter = ';')
#     for row in reader:
#         print(row)
#         key, value
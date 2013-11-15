# Script para converter pontos em coordenada latlong para WKT, e deixa em um format para inserção no plugin Neatline do Omeka
# script to convert latlong cordinates to wkt
# input: csv file (input.csv) with 3rd and 4rd colum with lat and long cordinates
# output: csv file (output.csv) with 3rd colum with wkt cordinate in format to insert on Neatline plugin for Omeka

import math
import csv

def convertlatlong (lat,long) :
    half_circ = 20037508.34
    x = long * half_circ /180
    y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    y = y * half_circ / 180
    return "GEOMETRYCOLLECTION(POINT("+str(x)+" "+str(y)+"))"


#parte para ler o csv e depois converter para wkt e gerar o resultado



arq_cvs = csv.reader(open('input.csv','rb'),delimiter=',',quotechar='"')

lista_cvs = list(arq_cvs)

for i in range(1,len(lista_cvs)):
	lista_cvs[i][2] = convertlatlong(float(lista_cvs[i][2]),float(lista_cvs[i][3]))
	lista_cvs[i].pop(3)


result = open('output.csv','wb')
writer=csv.writer(result,dialect='excel')
headings=writer.writerows(lista_cvs)
result.close()






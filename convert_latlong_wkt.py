# Script para converter pontos em coordenada latlong para WKT

import math
import csv

def convertlatlong (lat,long) :
    half_circ = 20037508.34
    x = long * half_circ /180
    y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    y = y * half_circ / 180
    return "GEOMETRYCOLLECTION(POINT("+str(x)+" "+str(y)+"))"


#parte para ler o csv e depois converter para wkt e gerar o resultado



arq_cvs = csv.reader(open('mapeamento2.csv','rb'),delimiter=',',quotechar='"')

lista_cvs = list(arq_cvs)

for i in range(1,len(lista_cvs)):
	lista_cvs[i][2] = convertlatlong(float(lista_cvs[i][2]),float(lista_cvs[i][3]))
	lista_cvs[i].pop(3)


result = open('resultado.csv','wb')
writer=csv.writer(result,dialect='excel')
headings=writer.writerows(lista_cvs)
result.close()






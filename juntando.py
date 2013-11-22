# coding: utf-8
import csv

#script para juntar os dados de filiacao com os dados dos servidores

arq1_cvs = csv.reader(open('teste1.csv','rb'),delimiter=',')

lista1_cvs = list(arq1_cvs)

arq2_cvs = csv.reader(open('teste2.csv','rb'),delimiter=',')

lista2_cvs = list(arq2_cvs)

servidores = {}

#servidores = {'JOAO' : {'orgao':'MINC','contador':1},'PEDRO' ... }

for servidor in lista1_cvs:
	if servidores.has_key(servidor[0]):
		servidores[servidor[0]]['contador'] += 1
	else:
		servidores[servidor[0]] = {}
		servidores[servidor[0]]['orgao'] = servidor[1]
		servidores[servidor[0]]['contador'] = 1
	

filiados = {}

#filiados = {'PAULO' : {'partido':'PT','contador':1}, 'JOAQUIM' ...}

for filiado in lista2_cvs:
	if filiados.has_key(filiado[0]):
		filiados[filiado[0]]['contador'] += 1 
	else:
		filiados[filiado[0]] = {}
		filiados[filiado[0]]['partido'] = filiado[1]
		filiados[filiado[0]]['contador'] = 1

result = {}

for filiado in filiados:
	if filiados[filiado]['contador'] == 1 :
		if servidores.has_key(filiado) and servidores:
			if servidores[filiado]['contador'] == 1:
				if result.has_key(filiados[filiado]['partido']) and result[filiados[filiado]['partido']].has_key(servidores[filiado]['orgao']):
					result[filiados[filiado]['partido']][servidores[filiado]['orgao']] += 1
				elif result.has_key(filiados[filiado]['partido']) and not result[filiados[filiado]['partido']].has_key(servidores[filiado]['orgao']):
					result[filiados[filiado]['partido']][servidores[filiado]['orgao']] = 1
				else:			
					result[filiados[filiado]['partido']] = {servidores[filiado]['orgao']:1}
	
print result		



#resultado final partido, orgão, count

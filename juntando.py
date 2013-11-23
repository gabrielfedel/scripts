# coding: utf-8
import csv
import json

#script para juntar os dados de filiacao com os dados dos servidores
#desenvolvido durante o 2o ENDA em Brasilia

arq1_csv = csv.reader(open('teste1.csv','rb'),delimiter=',')

lista1_csv = list(arq1_csv)

arq2_csv = csv.reader(open('teste2.csv','rb'),delimiter=',')

lista2_csv = list(arq2_csv)

servidores = {}

#servidores = {'JOAO' : {'orgao':'MINC','contador':1},'PEDRO' ... }

#Guarda o total de funcionários de cada orgão
total_orgao = {}

for servidor in lista1_csv:
	if servidores.has_key(servidor[0]):
		servidores[servidor[0]]['contador'] += 1
	else:
		servidores[servidor[0]] = {}
		servidores[servidor[0]]['orgao'] = servidor[1]
		servidores[servidor[0]]['contador'] = 1
	if total_orgao.has_key(servidor[1]):
		total_orgao[servidor[1]] += 1
	else:
		total_orgao[servidor[1]] = 1
	

filiados = {}

#filiados = {'PAULO' : {'partido':'PT','contador':1}, 'JOAQUIM' ...}

for filiado in lista2_csv:
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
	
with open("resultado.json", "w") as resultado:
    resultado.write(json.dumps(result, indent=4))


#resultado final partido, orgão, count

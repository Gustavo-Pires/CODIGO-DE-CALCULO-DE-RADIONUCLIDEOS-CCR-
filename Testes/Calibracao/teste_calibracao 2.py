#---------------------------------------------BIBLIOTECAS ---------------------------------------------
import time
start_time1= time.time()
from datetime import datetime
import xlwings as xw
import pandas as pd
import os
import glob
import sys
import csv
import re
import locale


#------------------------------------------------------------------------------------------------------
#---------------------------------------------CONTAGEM -------------------------------------
print("=" * 20 + "CALIBRAÇÃO INICIADA" + "=" * 20)

diretorio_atual = os.path.abspath(os.path.dirname(__file__))
arquivos_csv = glob.glob(os.path.join(diretorio_atual, '*.csv'))

if len(arquivos_csv) == 0:
    print("Nenhum arquivo CSV foi encontrado no diretório atual.")
    print("=" * 20 + "CALIBRAÇÃO NÃO REALIZADA" + "=" * 20)
    sys.exit()
elif len(arquivos_csv) > 1:
    print("Mais de um arquivo CSV foi encontrado no diretório atual. \nDeixei apenas o arquivo correto")
    print("=" * 20 + "CALIBRAÇÃO NÃO REALIZADA" + "=" * 20)
    sys.exit()

arquivo_csv = arquivos_csv[0]

try:
    with open(arquivo_csv, newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        # Extrair as colunas específicas
        ekev = [row[0] for row in rows[6:27]]
        resolucao = [row[1] for row in rows[6:27]]
        canal = [row[5] for row in rows[6:27]]
        contagem = [row[3] for row in rows[6:27]]
        incerteza = [row[4] for row in rows[6:27]]
        data = rows[1][0]
        nome_amostra = rows[0][0].rsplit("\\", 1)[-1]
        print(nome_amostra)

        # Remover células vazias
        ekev = [x for x in ekev if x]
        resolucao = [x for x in resolucao if x]
        canal = [x for x in canal if x]
        contagem = [x for x in contagem if x]
        incerteza = [x for x in incerteza if x]

except FileNotFoundError:
    print("Arquivo CSV não encontrado.")

#------------------------------------------------------------------------------------------------------
end_time1= time.time()

elapsed_time1= end_time1 - start_time1
nome = input('Digite seu nome: ')
start_time2= time.time() 
#---------------------------------------------ARQUIVO DE CONTAGEM -------------------------------------

#-------------------------------------------------------------------------------------------------


#---------------------------------------------IMPORTANDO DADOS-------------------------------------
ws2 = xw.Book("Calibracao.xlsx").sheets['Calibracao']

data_hora= ws2.range("B9:B40").options(numbers=str).value

co_57_ekev= ws2.range("C9:C40").options(numbers=str).value
co_57_resolucao= ws2.range("D9:D40").options(numbers=str).value
co_57_canal =ws2.range("E9:E40").options(numbers=str).value
co_57_contagem =ws2.range("F9:F40").options(numbers=str).value
co_57_incerteza =ws2.range("G9:G40").options(numbers=str).value

co_60_ekev= ws2.range("H9:H40").options(numbers=str).value
co_60_resolucao= ws2.range("I9:I40").options(numbers=str).value
co_60_canal =ws2.range("J9:J40").options(numbers=str).value
co_60_contagem =ws2.range("K9:K40").options(numbers=str).value
co_60_incerteza =ws2.range("L9:L40").options(numbers=str).value

usuario= ws2.range("M9:M40").options(numbers=str).value
#------------------------------------------------------------------------------------------------------

#----------removendo celulas vazias----------
data_hora=[x for x in data_hora if x is not None]

co_57_ekev= [x for x in co_57_ekev if x is not None]
co_57_resolucao= [x for x in co_57_resolucao if x is not None]
co_57_canal =[x for x in co_57_canal if x is not None]
co_57_contagem =[x for x in co_57_contagem if x is not None]
co_57_incerteza =[x for x in co_57_incerteza if x is not None]

co_60_ekev= [x for x in co_60_ekev if x is not None]
co_60_resolucao= [x for x in co_60_resolucao if x is not None]
co_60_canal =[x for x in co_60_canal if x is not None]
co_60_contagem =[x for x in co_60_contagem if x is not None]
co_60_incerteza=[x for x in co_60_incerteza if x is not None]

usuario= [x for x in usuario if x is not None]
#----------------------------------------------

data_hora.append(data)
usuario.append(nome)

#-----------------------------------------ACHANDO OS PICOS-------------------------------------------------------------
valor_procurado = 122.06
encontrado = False

for j in range(len(ekev)):
    valor = ekev[j].replace(" ", "").replace(",", ".")
    if float(valor) >= valor_procurado - 2 and float(valor) <= valor_procurado + 2:
        encontrado = True
        co_57_ekev.append(ekev[j])
        co_57_resolucao.append(resolucao[j])
        co_57_contagem.append(contagem[j])
        co_57_incerteza.append(incerteza[j])
        co_57_canal.append(canal[j])
        break  # interrompe o laço de repetição

if not encontrado:
    print("Pico de energia do co-57 não encontrado dentro da variação.")
    print("="*20 + "CALIBRAÇÃO NÃo CONCLUIDA" + "="*20  )
    sys.exit()

    
valor_procurado = 1332.5
encontrado = False

for j in range(len(ekev)):
    valor = ekev[j].replace(" ", "").replace(",", ".")
    if float(valor) >= valor_procurado - 2 and float(valor) <= valor_procurado + 2:
        encontrado = True
        co_60_ekev.append(ekev[j])
        co_60_resolucao.append(resolucao[j])
        co_60_contagem.append(contagem[j])
        co_60_incerteza.append(incerteza[j])
        co_60_canal.append(canal[j])
        break  # interrompe o laço de repetição

if not encontrado:
    print("Pico de energia do co-60 não encontrado dentro da variação.")
    print("="*20 + "CALIBRAÇÃO NÃo CONCLUIDA" + "="*20  )
    sys.exit()


#----------------------------------------------------------------------------------------------------------------

#-----------------------SALVANDO-----------------------------------------------------------------------------------------
# Convertendo os valores para o formato americano com ponto decimal
co_57_ekev = [x.replace('.', ',') for x in co_57_ekev]
co_57_resolucao = [x.replace('.', ',') for x in co_57_resolucao]
co_57_canal = [x.replace('.', ',') for x in co_57_canal]
co_57_contagem = [x.replace('.', ',') for x in co_57_contagem]
co_57_incerteza = [x.replace('.', ',') for x in co_57_incerteza]

co_60_ekev = [x.replace('.', ',') for x in co_60_ekev]
co_60_resolucao = [x.replace('.', ',') for x in co_60_resolucao]
co_60_canal = [x.replace('.', ',') for x in co_60_canal]
co_60_contagem = [x.replace('.', ',') for x in co_60_contagem]
co_60_incerteza = [x.replace('.', ',') for x in co_60_incerteza]

# Salvando os dados convertidos no formato americano
ws2.range('B9:B40').options(transpose=True).value = [data_hora]
ws2.range('C9:C40').options(transpose=True).value = [co_57_ekev]
ws2.range('D9:D40').options(transpose=True).value = [co_57_resolucao]
ws2.range('E9:E40').options(transpose=True).value = [co_57_canal]
ws2.range('F9:F40').options(transpose=True).value = [co_57_contagem]
ws2.range('G9:G40').options(transpose=True).value = [co_57_incerteza]
ws2.range('H9:H40').options(transpose=True).value = [co_60_ekev]
ws2.range('I9:I40').options(transpose=True).value = [co_60_resolucao]
ws2.range('J9:J40').options(transpose=True).value = [co_60_canal]
ws2.range('K9:K40').options(transpose=True).value = [co_60_contagem]
ws2.range('L9:L40').options(transpose=True).value = [co_60_incerteza]
ws2.range('M9:M40').options(transpose=True).value = [usuario]


#----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------
end_time2= time.time()
elapsed_time2= end_time2 - start_time2
elapsed_time = elapsed_time1 + elapsed_time2
#-----------------------------------------------------------------

#wb.save()
#ws2.close()

print("Tempo de execução:", elapsed_time, "segundos")
print("="*20 + "CALIBRAÇÃO CONCLUIDA" + "="*20  )







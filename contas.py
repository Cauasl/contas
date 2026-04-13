import sys
from datetime import datetime
import os
import csv
import json

def procurarIndexValor(arry=[], val=str):
    try:
        res = int(arry.index(val))
        return arry[res]
    except ValueError:
        return '-1'

# nome dos arquivos mês_ano
# -alteracao //faz a alteraçao no arquivo criado

#ADICIONAR/COLOCAR CONTA
# conta dinheiro -adm (adicionar mais contas)
# 

args = sys.argv[1:] # pega o que está escrito depois do arquivo chamado e separa ele em []
print(args)

noMomento = datetime.now()
mes = noMomento.month
ano = noMomento.year
arquivoConta = f'{mes}_{ano}'
caminho = f'meses/{arquivoConta}'

#Verefica se o arquivo com a data atual existe, se não 
if not os.path.isfile(caminho + '/contas.json') and len(args) == 0:
    print('O arquivo não existe ainda, deseja criar outro?')
    res = input('Sim/Não: ')
    if res == 's' or res == 'sim' or res == 'Sim':
        contaArray = []

        #Pergunta e já adiciona o sálario
        valorSalario = float(input('Qual o sálario do mês: '))

        #Pergunta sobre qual conta quer adicionar e seu valor
        resConta = input('Conta dinheiro: ').split() #[conta, valor, -adm(Comando)]
        valorLiquido = float(resConta[1])
        #Se for apenas um valor ele coloca no arquivo também
        if len(resConta) < 3:
            contaArray.append(resConta)
        while len(resConta) > 2 and procurarIndexValor(resConta, '-adm') == '-adm': #Loop para adicionar quantos valores quiser
            resConta.remove('-adm')
            contaArray.append(resConta)
            resConta = input('Conta dinheiro (lp): ').split()
            valorLiquido += float(resConta[1])
            if procurarIndexValor(resConta, '-adm') == '-1':
                contaArray.append(resConta)

        valorTotal = valorSalario - valorLiquido
        contaObj = [{
            "valorSalario": valorSalario,
            "valorLiquido": valorLiquido,
            "valorTotal": valorTotal
        }]
        #Cria o arquivo csv e adiciona os respectivos valores
        if not os.path.exists(caminho):
            os.makedirs(caminho)
            for i in range(0, len(contaArray)):
                contaObj.append({
                    "conta": contaArray[i][0],
                    "valor": float(contaArray[i][1]),
                    "comando": contaArray[i][2]
                })
            contaJson = json.dumps(contaObj, ensure_ascii=False, indent=4)
            
            with open(caminho + '/contas.json', 'w') as arqJson:
                arqJson.write(contaJson)

            with open(caminho + '/va.json', 'w') as vaJson:
                vaJson.write(json.dumps({
                    "VA_total": 300,
                    "total": 300
                }, ensure_ascii=False, indent=4))

            print('\n Conta do mês criada! \n')

#Lê o arquivo csv do mês
elif os.path.isfile(f'meses/{arquivoConta}.csv'):
    with open(f'meses/{arquivoConta}.csv', 'r') as arq:
        csv_lido = csv.reader(arq, delimiter=';')
        for linha in csv_lido:
            print(linha)
        



if len(args) == 1:
    match args[0]:
        case '-status':
            with open(caminho + '/contas.json', 'r', encoding='utf-8') as arq:
                json_carregado = json.load(arq)
                print(json_carregado[0]['valorSalario'])
                print('=============')
                for i in range(1, len(json_carregado)):
                    print(f'{json_carregado[i]['valor']} - {json_carregado[i]['conta']}')
                print(f'============= Total: {json_carregado[0]['valorLiquido']}')
                print('Pagas: \n')
                print(f'============= Total gasto: {json_carregado[0]['valorLiquido']}')
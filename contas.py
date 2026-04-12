import sys
from datetime import datetime
import os
import csv

# nome dos arquivos mês_ano
# -alteracao //faz a alteraçao no arquivo criado

#ADICIONAR/COLOCAR CONTA
# conta dinheiro -adm (adicionar mais contas)
# 

args = sys.argv[1:] # pega o que está escrito depois do arquivo chamado e separa ele em []

noMomento = datetime.now()
mes = noMomento.month
ano = noMomento.year
arquivoConta = f'{mes}_{ano}'

#Verefica se o arquivo com a data atual existe, se não 
if not os.path.isfile(f'meses/{arquivoConta}.csv') and len(args) == 0:
    print('O arquivo não existe ainda, deseja criar outro?')
    res = input('Sim/Não: ')
    if res == 's' or res == 'sim' or res == 'Sim':
        contaArray = []
        
        #Pergunta e já adiciona o sálario
        contaArray.append(['Valor recebido', input('Qual o sálario do mês: ')])

        #Pergunta sobre qual conta quer adicionar e seu valor
        resConta = input('Conta dinheiro: ').split() #[conta, valor, -adm(Comando)]

        #Se for apenas um valor ele coloca no arquivo também
        if len(resConta) < 3:
            contaArray.append(resConta)
        while len(resConta) > 2 and resConta[2] == '-adm': #Loop para adicionar quantos valores quiser
            resConta.remove('-adm')
            contaArray.append(resConta)
            resConta = input('Conta dinheiro (lp): ').split()
            if len(resConta) < 3:
                contaArray.append(resConta)

        #Cria o arquivo csv e adiciona os respectivos valores
        with open(f'meses/{arquivoConta}.csv', 'w') as arqq:
            for linha in contaArray:
                linhaCsv = ';'.join(linha)
                arqq.write(linhaCsv + '\n')

#Lê o arquivo csv do mês
elif os.path.isfile(f'meses/{arquivoConta}.csv'):
    with open(f'meses/{arquivoConta}.csv', 'r') as arq:
        csv_lido = csv.reader(arq, delimiter=';')
        for linha in csv_lido:
            print(linha)
        




# match args:
#     case '-alteracao':
        
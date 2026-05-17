import sys
from datetime import datetime
import os
import json
import funcoes

# nome dos arquivos mês_ano
# -al //faz a alteraçao no arquivo criado

#ADICIONAR/COLOCAR CONTA
# conta dinheiro -ad (adicionar mais contas)
# -pgp (pagar proximo mes)
#
#PAGAR CONTA
# contas.py conta (se for -pc)
# contas.py conta valor (se for -pp)

args = sys.argv[1:] # pega o que está escrito depois do arquivo chamado e separa ele em []

noMomento = datetime.now()
mes = noMomento.month
ano = noMomento.year
arquivoConta = f'{mes}_{ano}'
caminho = f'meses/{arquivoConta}'
contasPagas = []

#Verefica se o arquivo com a data atual existe, se não 
if not os.path.isfile(caminho + '/contas.json') and len(args) == 0:
    print('O arquivo não existe ainda, deseja criar outro?')
    res = input('Sim/Não: ')
    if res == 's' or res == 'sim' or res == 'Sim':

        #Pergunta e já adiciona o sálario
        valorSalario = float(input('Qual o sálario do mês: '))
        
        sla = funcoes.criacaoConta()

        valorTotal = valorSalario - sla['valorLiquido']
        contaObj = [{
            "valorSalario": valorSalario,
            "valorLiquido": sla['valorLiquido'],
            "valorLiquidoTotal": sla['valorLiquido']
        }]
        #Cria o caminho e adiciona os respectivos valores ao arquivo
        if not os.path.exists(caminho) or not os.path.exists(caminho+'/contas.json'):
            os.makedirs(caminho)
            for i in range(0, len(sla['objConta'])):
                contaObj.append({
                    "conta": sla['objConta'][i][0],
                    "valor": float(sla['objConta'][i][1]),
                    "comando": sla['objConta'][i][2],
                    "status": 'nao_paga'
                })
            contaJson = json.dumps(contaObj, ensure_ascii=False, indent=4)
            
            with open(caminho + '/contas.json', 'w') as arqJson:
                arqJson.write(contaJson)

            with open(caminho + '/va.json', 'w') as vaJson:
                vaJson.write(json.dumps({
                    "VA_parte1": 300.0,
                    "histParte1": [],
                    "VA_parte2": 300.0,
                    "histParte2": [], 
                    "total": 600.0
                }, ensure_ascii=False, indent=4))

            print('\n Conta do mês criada! \n')

#Lê o arquivo csv do mês
elif os.path.isfile(f'meses/{arquivoConta}.csv'):
  ...
        



for a, argumento in enumerate(args): #Torna possível colocar mais argumentos
  with open(caminho + '/contas.json', 'r', encoding='utf-8') as arq:
    json_carregado = json.load(arq)
    match argumento:
       
      #Mostra uma visão geral das contas
      case '-status':
        arqVisualizado = caminho + '/contas.json'
        if len(args[a:]) > 1: #Reconfigura para ver outra conta
          arqVisualizado = f'meses/{args[a:][1]}_2026/contas.json'
        
        #Abre o arquivo e fez a leitura
        with open(arqVisualizado, 'r', encoding='utf-8') as arqLido:
          
          statusConta = json.load(arqLido)
          print(statusConta[0]['valorSalario'])
          print(statusConta[0]['valorSalario'] - statusConta[0]['valorLiquido'])
          print('=============')
          for j, item in enumerate(statusConta):
            if j == 0:
               continue
            if item['status'] == 'paga':
              contasPagas.append(item['conta'])
            print(f'{item['valor']} - {item['conta']}')
          
          print(f'============= Total: {statusConta[0]['valorLiquido']}')
          print('Pagas: \n')
          if len(contasPagas) > 0:
            for cpaga in contasPagas:
              print(cpaga)
          print(f'============= Total gasto: {statusConta[0]['valorLiquidoTotal']}')
      
      #Mostra uma conta específica (-v contaEscolhida)
      case '-v':
        contaSelecionada = args[a+1]
        for uc, umaConta in enumerate(json_carregado):
          if uc == 0:
            continue
          if contaSelecionada == umaConta['conta']:
            statusConta = ''
            if umaConta['status'] == 'nao_paga':
              statusConta = 'não paga'
            else: 
              statusConta = 'paga'
            print(umaConta['conta'] + f', R${umaConta['valor']} status: {statusConta}')

      #Adiciona uma conta para o arquivo do mês            
      case '-ad':
        # -ad contaParaAdicionar valor comando
        if funcoes.seComando(argumento):
          json_carregado[0]['valorLiquidoTotal'] = json_carregado[0]['valorLiquidoTotal'] + float(args[i+2])
          json_carregado.append({
                      "conta": args[a+1],
                      "valor": float(args[a+2]),
                      "comando": args[a+3],
                      "status": 'nao_paga'
                  })
          with open(caminho+'/contas.json', 'w') as arq:
            arq.write(json.dumps(json_carregado, ensure_ascii=False, indent=4))
            
      case '-s': #simulação
        simu = funcoes.criacaoConta()
        print(simu['valorLiquido'])
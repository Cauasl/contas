import sys
from datetime import datetime
import os
import json

def procurarIndexValor(arry=[], val=str):
    try:
        if arry.index(val):
          return True
    except ValueError:
        return False

def seComando(comd=str):
  listaComandos = ['-ad', '-pp', '-pc', '-v', '-status']
  try:
    if listaComandos.index(comd) >= 0:
      return True
  except ValueError:
    return False

def verificacaoEntradaConta(arry=[]):
  comandos = ['-pp', '-pc']
  try:
    print(float(arry[1]))
    for i in range(0, len(comandos)):
      if len(arry) > 2 and arry[2] == comandos[i]:
        return []
      elif i == len(comandos) - 1:
          return arry
  except ValueError:
    return arry


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
        contaArray = []


        #Pergunta e já adiciona o sálario
        valorSalario = float(input('Qual o sálario do mês: '))
        valorLiquido = 0 
        #Pergunta sobre qual conta quer adicionar e seu valor
        resConta = []
        while not procurarIndexValor(resConta, '-t'): #Loop para adicionar quantos valores quiser // -t termina o loop
          resConta = input('Conta dinheiro -tipo: ').split()
          resErroInput = verificacaoEntradaConta(resConta) #Caso não compra os requisitos retorna uma arry vazia

          while len(resErroInput) > 0:
            fraseInput = " ".join(resErroInput)
            print('Valor não segue o esperado.')
            resConta = input(fraseInput + ": ").split()
            for i, item in enumerate(resErroInput):
              if i < len(resErroInput)-1: #Coloca os valores anteriores ao index com valor errado
                resConta.insert(i, item)
            resErroInput = verificacaoEntradaConta(resConta)

          contaArray.append(resConta)
          valorLiquido += float(resConta[1])
          if procurarIndexValor(resConta, '-t'):
              contaArray.append(resConta)


        valorTotal = valorSalario - valorLiquido
        contaObj = [{
            "valorSalario": valorSalario,
            "valorLiquido": valorLiquido,
            "valorLiquidoTotal": valorLiquido
        }]
        #Cria o caminho e adiciona os respectivos valores ao arquivo
        if not os.path.exists(caminho) or not os.path.exists(caminho+'/contas.json'):
            os.makedirs(caminho)
            for i in range(0, len(contaArray)):
                contaObj.append({
                    "conta": contaArray[i][0],
                    "valor": float(contaArray[i][1]),
                    "comando": contaArray[i][2],
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
        if seComando(argumento):
          json_carregado[0]['valorLiquidoTotal'] = json_carregado[0]['valorLiquidoTotal'] + float(args[i+2])
          json_carregado.append({
                      "conta": args[a+1],
                      "valor": float(args[a+2]),
                      "comando": args[a+3],
                      "status": 'nao_paga'
                  })
          with open(caminho+'/contas.json', 'w') as arq:
            arq.write(json.dumps(json_carregado, ensure_ascii=False, indent=4))
            
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

# nome dos arquivos mês_ano
# -al //faz a alteraçao no arquivo criado

#ADICIONAR/COLOCAR CONTA
# conta dinheiro -ad (adicionar mais contas)
# 
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

        #Pergunta sobre qual conta quer adicionar e seu valor
        resConta = input('Conta dinheiro: ').split() #[conta, valor, -adm(Comando)]
        valorLiquido = float(resConta[1])
        #Se for apenas um valor ele coloca no arquivo também
        if len(resConta) < 3:
            contaArray.append(resConta)
        while len(resConta) > 2 and procurarIndexValor(resConta, '-ad'): #Loop para adicionar quantos valores quiser
            resConta.remove('-adm')
            contaArray.append(resConta)
            resConta = input('Conta dinheiro (lp): ').split()
            valorLiquido += float(resConta[1])
            if procurarIndexValor(resConta, '-adm'):
                contaArray.append(resConta)

        valorTotal = valorSalario - valorLiquido
        contaObj = [{
            "valorSalario": valorSalario,
            "valorLiquido": valorLiquido,
            "valorLiquidoTotal": valorLiquido
        }]
        #Cria o arquivo csv e adiciona os respectivos valores
        if not os.path.exists(caminho):
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
                    "VA_total": 300,
                    "total": 300
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
        print(json_carregado[0]['valorSalario'])
        print('=============')
        for j, item in enumerate(json_carregado):
          if j == 0:
             continue
          if item['status'] == 'paga':
            contasPagas.append(item['conta'])
          print(f'{item['valor']} - {item['conta']}')
        
        print(f'============= Total: {json_carregado[0]['valorLiquido']}')
        print('Pagas: \n')
        if len(contasPagas) > 0:
          for cpaga in contasPagas:
            print(cpaga)
        print(f'============= Total gasto: {json_carregado[0]['valorLiquidoTotal']}')
      
      #Mostra uma conta específica (-v contaEscolhida)
      case '-v':
        contaSelecionada = args[a+1]
        for umaConta in json_carregado:
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
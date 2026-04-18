import sys
import os
import json
from datetime import datetime

args = sys.argv[1:]
noMomento = datetime.now()
mes = noMomento.month
ano = noMomento.year
arquivoConta = f'{mes}_{ano}'
caminho = f'meses/{arquivoConta}'

if os.path.isfile(caminho + '/contas.json') and len(args) > 0:
  valorAlterado = 0
  json_carregado = []
  conta = ''
  status = ''
  
  #Abre o arquivo json para fazer as alterações
  with open(caminho+'/contas.json', 'r') as arqq:
    json_carregado = json.load(arqq)
    valorTotal = json_carregado[0]['valorLiquidoTotal']
    argumento = args[0]
    
    #Passa um por um verificando qual é o correto
    for ci, cItem in enumerate(json_carregado):
      if ci == 0: #ci = conta index
        continue
      conta = cItem['conta']
      status = cItem['status']
      valorPassado = 0 #Variavel de controle
      
      if len(args) > 1 and args[1][0] == '+':
        valorPassado = float(args[1].replace('+', ''))
        if conta == argumento:
          valorAlterado = valorTotal + valorPassado
          json_carregado[0]['valorLiquidoTotal'] = valorAlterado
          cItem['valor'] = cItem['valor'] + valorPassado 
          print('\nFeito \n')
      
      #Se for a conta passada para fazer o desconto
      elif conta == argumento and status != 'paga' and json_carregado[0]['valorLiquidoTotal'] > 0:
        #Se for o pagamento completo
        if cItem['comando'] == '-pc':
          valorAlterado = valorTotal - cItem['valor']
          cItem['status'] = 'paga'
          
        #Se for o pagamento parcial
        elif cItem['comando'] == '-pp' and len(args) > 1:
          
          calculoPP = cItem['valor'] - valorPassado
          if calculoPP <= 0:
            print('AVISO: Ultrapassou o limite estipulado da conta!')
            cItem['status'] = 'paga'
          cItem['valor'] = calculoPP
          valorAlterado = valorTotal - float(args[1])
          
        #Se for pagamento parcial e não foi apresentado o valor
        elif len(args) < 2:
          print('Não especificado o valor')
          break
        
        #Faz a alteração no dicionario
        json_carregado[0]['valorLiquidoTotal'] = valorAlterado
        print('\nFeito \n')
        break
      
      #Caso a conta já tenha sido paga
      elif status == 'paga' and conta == argumento:
        print(f'A {conta} já está paga')

  #Abre o arquivo e rescreve com as alterações
  with open(caminho+'/contas.json', 'w') as arq:
    arq.write(json.dumps(json_carregado, ensure_ascii=False, indent=4))

else:
  print('O arquivo não existe')
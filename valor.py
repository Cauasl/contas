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

if os.path.isfile(caminho + '/contas.json'):
  valorAlterado = 0
  json_carregado = []
  conta = ''
  status = ''
  
  #Abre o arquivo json para fazer as alterações
  with open(caminho+'/contas.json', 'r') as arqq:
    json_carregado = json.load(arqq)
    valorTotal = json_carregado[0]['valorLiquidoTotal']
    argumento = args[0]
    print(args)
    
    #Passa um por um verificando qual é o correto
    for i in range(1, len(json_carregado)):
      conta = json_carregado[i]['conta']
      status = json_carregado[i]['status']
      valorPassado = 0
      
      if len(args) > 1 and args[1][0] == '+':
        valorPassado = float(args[1].replace('+', ''))
        if conta == argumento:
          valorAlterado = valorTotal + valorPassado
          json_carregado[0]['valorLiquidoTotal'] = valorAlterado
          json_carregado[i]['valor'] = json_carregado[i]['valor'] + valorPassado
          print('\nFeito \n')
      
      #Se for a conta passada para fazer o desconto
      elif conta == argumento and status != 'paga':
        valorPassado = float(args[1])
        #Se for o pagamento completo
        if json_carregado[i]['comando'] == '-pc':
          valorAlterado = valorTotal - json_carregado[i]['valor']
          json_carregado[i]['status'] = 'paga'
          
        #Se for o pagamento parcial
        elif json_carregado[i]['comando'] == '-pp' and len(args) > 1:
          
          calculoPP = json_carregado[i]['valor'] - valorPassado
          if calculoPP <= 0:
            print('AVISO: Ultrapassou o limite estipulado da conta!')
          json_carregado[i]['valor'] = calculoPP
          valorAlterado = valorTotal - float(args[1])
          json_carregado[i]['status'] = 'paga'
          
        #Se for pagamento parcial e não foi apresentado o valor
        elif len(args) < 2:
          print('Não especificado o valor')
          break
        
        #Faz a alteração no dicionario
        json_carregado[0]['valorLiquidoTotal'] = valorAlterado
        print('\nFeito \n')
        break
      
      #Caso a conta já tenha sido paga
      elif status == 'paga':
        print(f'A {conta} já está paga')
        break

  #Abre o arquivo e rescreve com as alterações
  with open(caminho+'/contas.json', 'w') as arq:
    arq.write(json.dumps(json_carregado, ensure_ascii=False, indent=4))

else:
  print('O arquivo não existe')
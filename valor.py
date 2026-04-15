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
  with open(caminho+'/contas.json') as arq:
    json_carregado = json.load(arq)
    valorTotal = json_carregado[0]['valorLiquidoTotal']
    argumento = args[0]
    
    for i in range(1, len(json_carregado)):
      if json_carregado[i]['conta'] == argumento:
        print(valorTotal - float(args[1]))
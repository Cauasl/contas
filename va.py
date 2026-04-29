import sys
import os
import json
from datetime import datetime

noMomento = datetime.now()
mes = noMomento.month
ano = noMomento.year
arquivoConta = f'{mes}_{ano}'
caminho = f'meses/{arquivoConta}'

args = sys.argv[1:]

if os.path.isfile(caminho+'/va.json') and len(args) > 0:
  with open(caminho+'/va.json', 'r', encoding='utf-8') as arqVA:
    arqVAjson = json.load(arqVA)
    match args[0]:
      case 'p1':
        if len(args) > 1:
          arqVAjson['VA_parte1'] = arqVAjson['VA_parte1'] - float(args[1])
          arqVAjson['total'] = arqVAjson['total'] - float(args[1])
          
          print('Valor p1 ' + arqVAjson['VA_parte1'])
          print(arqVAjson['total'])
        else:
          print('falta o valor!')
          
      case 'p2':
        if len(args) > 1:
          arqVAjson['VA_parte2'] = arqVAjson['VA_parte1'] - float(args[1])
          arqVAjson['total'] = arqVAjson['total'] - float(args[1])
          
          print('Valor p2 ' + arqVAjson['VA_parte2'])
          print('Valor total ' + arqVAjson['total'])
        else:
          print('falta o valor!')
      case '-status':
        print('Valor p1: ' + str(arqVAjson['VA_parte1']))
        print('Valor p2: ' + str(arqVAjson['VA_parte2']))
        print('Total: ' + str(arqVAjson['total']))
        
    with open(caminho+'/va.json', 'w', encoding='utf-8') as arqVA:
      arqVA.write(json.dumps(arqVAjson, ensure_ascii=False, indent=4))
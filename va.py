import sys
import os
import json
from datetime import datetime

def procurarIndexValor(val=str, proc=str):
  try:
    if val.index(proc):
      return True
  except ValueError:
    return False
  

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
          
          if len(args) > 2:
            arqVAjson['histParte1'].append(f"{args[1]};{args[2]}")
          else:
            arqVAjson['histParte1'].append(f"{args[1]}")
          
          print('Valor p1 ' + str(arqVAjson['VA_parte1']))
          print('Valor total ' + str(arqVAjson['total']))
        else:
          print('falta o valor!')
          
      case 'p2':
        if len(args) > 1:
          arqVAjson['VA_parte2'] = arqVAjson['VA_parte2'] - float(args[1])
          arqVAjson['total'] = arqVAjson['total'] - float(args[1])
          
          if len(args) > 2:
            arqVAjson['histParte2'].append(f"{args[1]};{args[2]}")
          else:
            arqVAjson['histParte2'].append(f"{args[1]}")
          
          print('Valor p2 ' + str(arqVAjson['VA_parte2']))
          print('Valor total ' + str(arqVAjson['total']))
        else:
          print('falta o valor!')
          
          
      case '-status':
        print('Valor p1: ' + str(arqVAjson['VA_parte1']))
        for gasto in arqVAjson['histParte1']:
          if procurarIndexValor(gasto, ';'):
            gasto_eMotivo = gasto.split(';')
            print(f' --- {gasto_eMotivo[0]}: {gasto_eMotivo[1]}')
          else:
            print(f' --- {gasto}')
        print('')
        print('Valor p2: ' + str(arqVAjson['VA_parte2']))
        for gasto in arqVAjson['histParte2']:
          if procurarIndexValor(gasto, ';'):
            gasto_eMotivo = gasto.split(';')
            print(f' --- {gasto_eMotivo[0]}: {gasto_eMotivo[1]}')
          else:
            print(f' --- {gasto}')
        print('')
        print('Total: ' + str(arqVAjson['total']))
        
    with open(caminho+'/va.json', 'w', encoding='utf-8') as arqVA:
      arqVA.write(json.dumps(arqVAjson, ensure_ascii=False, indent=4))
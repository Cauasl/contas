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
    if args[0] == 'p1' and len(args) > 1:
      arqVAjson['VA_parte1'] = arqVAjson['VA_parte1'] - float(args[1])
      arqVAjson['total'] = arqVAjson['total'] - float(args[1])
    elif args[0] == 'p2' and len(args) > 1:
      arqVAjson['VA_parte2'] = arqVAjson['VA_parte1'] - float(args[1])
      arqVAjson['total'] = arqVAjson['total'] - float(args[1])
      
    with open(caminho+'/va.json', 'w', encoding='utf-8') as arqVA:
      arqVA.write(json.dumps(arqVAjson, ensure_ascii=False, indent=4))
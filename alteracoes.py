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

arqSelecionado = arquivoConta

if args
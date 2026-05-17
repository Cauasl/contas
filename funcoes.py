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

def criacaoConta():
  dadosConta = []
  objConta = []
  valorLiquido = 0
  while not procurarIndexValor(dadosConta, '-t'):
    dadosConta = input('Conta dinheiro -tipo: ').split()
    if len(dadosConta) < 2:
      print('Falta informações')
      continue
    
    contaIncompleta = verificacaoEntradaConta(dadosConta)
    
    while len(contaIncompleta) > 0:
      print('Valor não segue o esperado.')
      fraseInput = " ".join(contaIncompleta)
      dadosConta = input(f"Conta dinheiro -tipo: {fraseInput} ").split()
      if len(dadosConta) == 0:
        continue

      for i, item in enumerate(contaIncompleta):
        if i < len(contaIncompleta)-1: #Coloca os valores anteriores ao index com valor errado
          dadosConta.insert(i, item)
          contaIncompleta = verificacaoEntradaConta(dadosConta)

    valorLiquido += float(dadosConta[1])
    objConta.append(dadosConta)

  if len(objConta) > 0:
    return {
      "objConta": objConta,
      "valorLiquido": valorLiquido
    }
  else:
    print("ERRO: Vazio")
    return {}

def criacaoConta():
  dadosConta = []
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
      if len(resConta) == 0:
        continue

      for i, item in enumerate(contaIncompleta):
        if i < len(contaIncompleta)-1: #Coloca os valores anteriores ao index com valor errado
        dadosConta.insert(i, item)
        contaIncompleta = verificacaoEntradaConta(dadosConta)
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
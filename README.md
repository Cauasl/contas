# Contas

Projeto para gerenciamento de contas do mês via terminal

<br>

## Ideia do projeto

A ideia partiu da necessidade de conseguir gerenciar melhor os gastos, de uma forma que funcionasse de maneira semelhante aos comandos de terminal Linux.

A partir disso, utilizando a linguagem Python que estou aprendendo durante a faculdade de ADS, comecei esse projeto, que segue mais ou menos a forma como eu estava organizando minhas contas.

## Como funciona?

Como mencionado antes, esse projeto funciona de forma parecida com o terminal, onde existem *comando*, *opção* e *argumento*. Porém, os próprios comandos (que seriam os arquivos) já executam alguma ação.

## contas.py

Ao executar apenas `python3 contas.py`, o programa inicia o processo de criação do arquivo. Ele pergunta quanto foi recebido no mês e quais são as contas que você precisa pagar, seguindo o padrão:

`nomeDaConta valor -comando`
### Comandos
`-pp` pagamento parcial <br>
`-pc` pagamento completo

Se quiser adicionar mais de uma conta, é necessário colocar na mesma linha o `-ad`.

Esses **comandos** servem para indicar se o desconto será completo ou parcial.

No caso do desconto completo, ao informar que o valor foi pago, será utilizado o próprio valor definido anteriormente para descontar do total, eliminando a necessidade de informar o valor novamente a cada atualização do sistema.
Já no desconto parcial, é necessário informar o valor que será descontado.

<br>

Em relação às opções utilizadas após o comando, temos o `-status`, que mostra uma visão geral das contas, indicando quais foram pagas e a soma total de todas elas.

O `-v` exibe a visualização de uma conta específica, que deve ser informada como argumento. Nessa visualização, são mostrados o valor da conta e o seu status.

Além disso, há o `-ad`, que também pode ser utilizado para adicionar uma nova conta, informando, como de costume, `nomeDaConta valor -comando`.

## valor.py

Ao contrário do `contas.py`, o `valor.py` precisa que seja passado algum argumento. Ele é responsável por realizar os descontos e também por adicionar valores a uma conta.

De forma simples, basta informar a conta na qual deseja fazer a alteração e o valor correspondente, respeitando os [comandos](#comandos) definidos anteriormente para essas contas. <br> <br>
Ex: <br>
`python3 valor.py contaDoMes` (Se o comando definido anteriormente foi `-pc`) <br>
`python3 valor.py contaDoMes 25` (Se o comando definido anteriormente foi `-pp`)

No caso de adicionar um valor a uma conta, é necessário apenas colocar um `+` na frente do valor que deseja adicionar. <br>
Ex: `python3 valor.py contaDoMes +300` 

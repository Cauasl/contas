# Contas

Projeto para gerenciamento de contas do mês via terminal

<br>

## Ideia do projeto

A ideia partiu da necessidade de conseguir gerenciar melhor os gastos, de uma forma que funcionasse de maneira semelhante aos comandos de terminal Linux.

A partir disso, utilizando a linguagem Python que estou aprendendo durante a faculdade de ADS, comecei esse projeto, que segue mais ou menos a forma como eu estava organizando minhas contas.

## Como funciona?

Como mencionado antes, esse projeto funciona de forma parecida com o terminal, onde existem *comando*, *opção* e *argumento*. Porém, os próprios comandos (que seriam os arquivos) já executam alguma ação.

### contas.py

Ao executar apenas `python3 contas.py`, o programa inicia o processo de criação do arquivo. Ele pergunta quanto foi recebido no mês e quais são as contas que você precisa pagar, seguindo o padrão:

`nomeDaConta valor -comando`
### Comandos
`-pp` pagamento parcial <br>
`-pc` pagamento completo

Se quiser adicionar mais de uma conta, é necessário colocar na mesma linha o `-ad`.

Esses **comandos** servem para indicar se o desconto será completo ou parcial.

No caso do desconto completo, ao informar que o valor foi pago, será utilizado o próprio valor definido anteriormente para descontar do total, eliminando a necessidade de informar o valor novamente a cada atualização do sistema.

Já no desconto parcial, é necessário informar o valor que será descontado.


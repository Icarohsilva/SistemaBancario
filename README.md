# Sistema Bancário em Python

Este é um programa simples em Python que simula as operações básicas de uma conta bancária. Ele oferece funcionalidades para depósito, saque, visualização de extrato e saída do programa.

## Funcionalidades

1. **Depositar:** Os usuários podem realizar depósitos em suas contas bancárias, especificando o valor que desejam depositar. O saldo da conta é atualizado de acordo com o valor do depósito, e a transação é registrada no extrato.

2. **Sacar:** Os usuários podem realizar saques, desde que o valor solicitado não exceda o limite diário de saque (definido como R$ 500) e o saldo disponível em sua conta. O número de saques diários é limitado a três. Os saques bem-sucedidos são registrados no extrato, e os usuários são notificados caso o saque não possa ser efetuado devido a falta de saldo ou atingimento do limite.

3. **Extrato:** Os usuários podem visualizar o extrato de sua conta, que lista todas as transações de depósito e saque realizadas, juntamente com o saldo atual. Caso não tenham sido realizadas transações, uma mensagem informando que não foram realizadas movimentações é exibida.

4. **Sair:** Os usuários podem sair do programa a qualquer momento, encerrando a execução.

## Como Usar

1. Clone o repositório para sua máquina local:

    git clone https://github.com/seu-usuario/sistema-bancario-python.git

2. Navegue até o diretório do projeto:

    cd sistema-bancario-python

3. Execute o programa Python:

    python sistema_bancario.py


4. Siga as instruções no menu para realizar operações bancárias.

## Requisitos

- Python 3.x

## Autor

Icaro Henrique

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

---
**Nota:** Este é um projeto simplificado e didático, destinado a demonstrar os conceitos básicos de controle de saldo, limites de saque e registro de transações em uma conta bancária.


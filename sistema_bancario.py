menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo += valor_deposito
        extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")

    elif opcao == '2':
        if numero_saques >= LIMITE_SAQUE:
            print("Você atingiu o limite diário de saques.")
        else:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque <= saldo and valor_saque <= limite:
                saldo -= valor_saque
                extrato.append(f"Saque: R$ {valor_saque:.2f}")
                numero_saques += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
            else:
                print("Não é possível sacar o valor especificado por falta de saldo ou limite diário.")

    elif opcao == '3':
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for movimentacao in extrato:
                print(movimentacao)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == '4':
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Escolha uma opção válida.")

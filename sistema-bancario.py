menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Você atingiu o limite de saques!")
        elif excedeu_saques:
            print("Você atingiu o limite de saques por dia!")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
    
    elif opcao == "e":
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Extrato:\n{extrato}")
    
    elif opcao == "q":
        break

    else:
        print("Opção inválida!")
        continue
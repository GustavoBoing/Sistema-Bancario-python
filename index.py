import time

qtd_saque = 0
extrato = """ """
saldo = 0
VALOR_LIMITE_SAQUE = 500
LIMITE_SAQUE = 3

menu = """
Digite uma opção: 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("\nDigite um valor para depósito(apenas números): "))
        while(saque < 0):
            print("\nValor inválido pois é um valor negativo. Tente novamente")
            time.sleep(2)
            deposito = float(input("\nDigite um valor para depósito(apenas números): "))
        saldo += deposito
        print("Depositando....")
        time.sleep(2)
        print("Depósito concluído!!")
        time.sleep(2)
        extrato += f"\n Você depositou R$ {deposito}"
    elif opcao == "s":
        if qtd_saque == LIMITE_SAQUE:
            print("\nVocê ja fez a qtd maxima de saques diários")
            time.sleep(2)
        else:
            saque = float(input("\nDigite um valor para saque(apenas números): "))
            while(saque > VALOR_LIMITE_SAQUE):
                print("\nValor inválido pois seu limite por saque é menor. Tente novamente")
                time.sleep(2)
                saque = float(input("Digite um valor para saque(apenas números): "))
            while(saque > saldo):
                print("\nValor inválido pois seu saldo é menor do que o valor que deseja sacar. Tente novamente")
                time.sleep(2)
                saque = float(input("\nDigite um valor para saque(apenas números): "))
            saldo -= saque
            print("Sacando....")
            time.sleep(2)
            print("Saque concluído!!")
            time.sleep(2)
            extrato += f"\n Você sacou R$ {saque}"
            qtd_saque += 1
    elif opcao == "e":
        print("\nImprimindo extrato....\n")
        time.sleep(2)
        print(extrato)
        print(f"\n Seu saldo é de R$ {saldo}")
        time.sleep(2)
    elif opcao == "q":
        print("\nVocê apertou na opção de sair!!\nVolte Sempre!!")
        break
    else:
        "A opção digitada é inválida"
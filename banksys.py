menu = """

[1] = Depósito
[2] = Saque
[3] = Extrato
[0] = Saia do sistema

"""
SALDO = 0
EXTRATO_S = ""
EXTRATO_D = ""
QTD_SAQUES = 0
LIMITE_SAQUES = 3
LIMITE = 500

while True:
    opt = input(menu)

    if opt == "1":
        deposito = float(input("Qual o valor do depósito? \n"))
        if deposito > 0:
            SALDO += deposito
            EXTRATO_D += f"Depósito: R$ {deposito}\n"
        else:
            print("Deposito somente de valores positivos\n")
            
    elif opt == "2":
        saque = float(input("Quanto deseja sacar? \n"))
        
        if QTD_SAQUES >= LIMITE_SAQUES:
            print("Limite de Saques diários atingidos\n")
        
        elif saque > LIMITE:
            print("Limite de Saque de R$500 atingido\n")
            
        elif saque < SALDO:
            SALDO -= saque
            EXTRATO_S += f"Saque: R$ {saque}\n"
            QTD_SAQUES += 1
        else:
            print(f"Saldo insuficiente\n")
            
    elif opt == "3":
        print("#", "Extrato")
        print(f"{EXTRATO_D}\n")
        print(f"{EXTRATO_S}\n")
        print(f"Seu saldo é de {SALDO}")  
          
    elif opt == "0":
        print("Obrigado por nos escolher!")
        break
    else:
        print("Digite uma opção válida!")

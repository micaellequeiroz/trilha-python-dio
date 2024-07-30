limite = 500
LIMITE_SAQUES = 3

def menu_text():
    return """
    [1] Depositar
    [2] Saldo
    [3] Sacar
    [4] Extrato
    [5] Sair
    => """

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return valor, saldo, extrato
        
    return print("Operação falhou! O valor informado é inválido.")

def ver_saldo(saldo):
    return print(f"\nSaldo: R$ {saldo:.2f}")
    
def sacar(valor, saldo, extrato, numero_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return valor, saldo, extrato, numero_saques
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return valor, saldo, extrato, numero_saques

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        return valor, saldo, extrato, numero_saques

    elif valor:
        if valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            return valor, saldo, extrato, numero_saques
    else:
       print("Operação falhou! O valor informado é inválido.")
       return valor, saldo, extrato, numero_saques

def extrair(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return saldo, extrato

def menu():
    saldo = 0
    extrato = ""
    numero_saques = 0
 
    while True:
        opcao = input(menu_text())
        if opcao == '1':
            valor = float(input("Informe o valor do depósito: "))
            valor, saldo, extrato = depositar(valor, saldo, extrato)
        
        elif opcao == '2':
            ver_saldo(saldo)

        elif opcao == '3':
            valor = float(input("Informe o valor do saque: "))
            valor, saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques)
        
        elif opcao == '4':
            extrair(extrato, saldo)
        
        elif opcao == '5':
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    menu()
import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [vs]\tVer saldo atual
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [lu]\tListar usuários
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} 💰\n"
        print("\n Depósito realizado com sucesso! ✅")
    else:
        print("Operação falhou! O valor informado é inválido. ❌")
    return saldo, extrato

def ver_saldo(saldo):
    return print(f"\nSaldo: R$ {saldo:.2f} 💰")
    
def sacar(*, valor, saldo, limite, extrato, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente. 💸")
    
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite. ⛔")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido. ❌")

    elif valor:
        if valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n Saque realizado com sucesso! ✅")
    else:
       print("Operação falhou! O valor informado é inválido. ⛔")
    
    return saldo, extrato

def extrair(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações. ❗ " if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f} 💰")
    print("==========================================")
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): 🛂")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        return print("Já existe usuário com esse CPF! ❌")
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso! ✅")

def filtrar_usuario(cpf, usuarios):
    filtro_usuarios = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro_usuarios[0] if filtro_usuarios else None

def listar_usuarios(usuarios):
    if usuarios == []:
        print("Não há usuários listados. ⛔")

    for usuario in usuarios:
        linha = f"""\
            Titular:\t{usuario['nome']}
            Data de nascimento:\t\t{usuario['data_nascimento']}
            Endereço:\t{usuario['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): 🛂")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario == None:
        return print("\n Usuário não encontrado, Não foi possível criar a conta! ❌")
    
    print("Conta criada com sucesso! ✅")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    if contas == []:
        print("Não há contas listadas. ⛔")

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    limite = 500
    LIMITE_SAQUES = 3
    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    AGENCIA = "0001" 

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)
        
        elif opcao == 'vs':
            ver_saldo(saldo)
        
        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                valor=valor, 
                saldo=saldo, 
                limite=limite, 
                extrato=extrato, 
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == 'e':
            extrair(saldo, extrato=extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == 'lc': 
            listar_contas(contas)     

        elif opcao == 'lu': 
            listar_usuarios(usuarios)   
        
        elif opcao == 'q':
            break       
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()

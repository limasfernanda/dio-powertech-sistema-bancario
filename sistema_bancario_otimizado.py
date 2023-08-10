# Potência Tech powered by iFood | Ciência de Dados
# Fernanda Lima
# Otimizando o Sistema Bancário com Funções Python


# Separar as funções existentes de saque, depósito e extrato em funções
# Criar duas novas funções: cadastrar usuário e cadastrar conta bancária
# Vincular a conta corrente com o usuário (cliente do banco)
# Exercitar separação em funções, por posição e por nome
# Saque recebe valores por keyword only.
# Sugestão de valores: saldo, valor, extrato, limite, numero_saques, limite_saques
# Sugestão retorno de saque: saldo e extrato
# Depósito recebe os argumentos por positional only
# Sugestão de argumentos: saldo, valor, extrato. Retorno: saldo e extrato
# Extrato recebe por posição e nome. Posição: saldo, Nome: extrato
# Sugestão criar mais funções: listar usuários, inativar conta
# Criar usuário: nome, data nascimento, cpf e endereço
# Endereço formato rua, nº, bairro, cidade/estado
# CPF somente numéros xxxxxxxxxxx. Não cadastra usuários mesmo cpf
# Criar conta: armazena em lista: agência, número conta e usuário.
# Número conta sequencial, inicia em 1, agência fixo "0001"
# Usuário pode ter mais de uma conta, porém uma conta é apenas de um usuário

## DICA: PARA VINCULAR USUARIO A CONTA, FILTRAR A LISTA BUSCANDO O NUMERO DO CPF INFORMADO
# As funções devem ter nomes diferentes das variáveis
# Verificar se sua variável é uma lista ou dicionário
# Quando criar listas, lembrar de colocar a definição vazio anteriormente
# Verificar as variáveis de retorno das funções

saldo=1000
limite_max=500
extrato=""
numero_saques= 0
numero_depositos=0
LIMITE_SAQUES= 3
usuarios = []
contas= []
AGENCIA= "0001"

def deposito(saldo, valor_deposito, extrato,numero_saques,numero_depositos,/):
    if valor_deposito>0:
        print("\nDepositando...")
        saldo_antigo=saldo
        saldo+=valor_deposito
        
        # No caso de não ter sido realizada nenhuma transação
        if numero_saques==0 and numero_depositos==0:
            extrato=saldo
            extrato=(f"\nSaldo atual: R$ {saldo_antigo:.2f} \nDepósito: (+) R$ {valor_deposito:.2f} \nSaldo atual: R$ {extrato:.2f}")
        
        #Caso já exista valores de saldo e saques
        else:
            extrato=(f"{extrato} \nDepósito: (+) R$ {valor_deposito} \nSaldo atual: R$ {saldo}")
        numero_depositos +=1
        print(f"\nSaldo atual: R${saldo}")
        print("Numero de depósitos atual:", numero_depositos )
    else:
        print("Não foi possível realizar a operação, informe um valor válido!")
    return saldo, extrato, numero_depositos

def saque(*, saldo, valor_saque, extrato, numero_saques, numero_depositos,limite_max):
    if valor_saque>0:
            
                #Não permitir tirar valores acima de 500 reais
                if valor_saque>limite_max:
                    print("Operação não permitida, seu limite diário é R$ 500.00!")
                
                #Caso tente tirar um valor maior que tem no banco
                elif valor_saque>saldo:
                    print("Operação não permitida, valor de saldo insuficiente!")
                else:
                    numero_saques +=1  #Se permitir, então irá sim contar como saque válido
                    
                    print("\nSacando...")

                    saldo_antigo=saldo
                    saldo-=valor_saque
                    print(f"\nSaldo atual: R${saldo}")

                        # No caso de não ter sido realizada nenhuma transação
                    if numero_saques==1 and numero_depositos==0:
                        extrato=saldo
                        extrato=(f"\nSaldo atual: R$ {saldo_antigo}  \nSaque: (-) R$ {valor_saque} \nSaldo atual: R$ {extrato}")
                        
                        #Caso já exista valores de saldo e saques
                    else:
                        extrato=(f"{extrato} \nSaque: (-) R$ {valor_saque} \nSaldo atual: R$ {saldo}")
                            
                    print("Numero de saques atual:", numero_saques )

    else:
        print("Não foi possível realizar a operação, informe um valor válido!")
    return saldo, extrato, numero_saques

def mostra_extrato(saldo,numero_saques,numero_depositos, /, *, extrato):
    if numero_saques==0 and numero_depositos==0:
                print(f"Ainda não foram realizadas movimentações. Saldo atual R$ {saldo:.2f}")

    elif numero_depositos>=1 or numero_saques>=1:

        mensagem=("Transições realizadas")
        print(mensagem.center(54," "))
        print("------------------------------------------------------")
        print(f"{extrato}\n")


def criar_usuario(usuarios):
    cpf=int((input("\nInforme apenas os numero do CPF: ")))

    filtro_usuarios=[usuario for usuario in usuarios if usuario["cpf"] == cpf]

    if filtro_usuarios==[]: 
        
        nome=(input("\nInforme nome do usuário: "))
        data_nascimento=(input("\nEscreva a data de nascimento (formato:dd/mm/aaaa): "))
        rua=(input("\nInforme o endereço (logradouro, número, bairro, cidade/estado): "))
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": rua})

        print("\n........\n")
        print("Usuário cadastrado com sucesso! Crie uma conta caso não tenha.")

    else:
        print("\n........\n")
        print ("Já existe um usuário cadastrado neste CPF, só é permitido cadastro único!!")
 

def criar_conta(agencia, numero_conta, usuarios):
    cpf=int((input("\nInforme apenas os numero do CPF: ")))
    filtro_usuarios=[usuario for usuario in usuarios if usuario["cpf"] == cpf]

    if filtro_usuarios==[]: 
        print("\n........\n")
        print("CPF de usuário não encontrado, não é possível criar uma conta!")        

    else:
        print("\n........\n")
        print("Conta cadastrada com sucesso! É possível o cliente ter mais de uma conta, sinta-se livre para criar outras!")

        return  {"agência": agencia, "numero_conta":numero_conta, "usuario":filtro_usuarios[0]}
    

def inicio():
    mensagem = (f"""
        ################### MENU ####################

        1- Depositar
        2- Sacar
        3- Extrato
        4- Criar novo usuário
        5- Cadastrar uma nova conta
        6- Listar contas
        0- Sair

        #############################################
        """
        )
    return mensagem


while True:  
    
    print(inicio())
       
    opcao=float(input("\nInsira a opção que deseja realizar: "))

    if opcao == 1:
        valor_deposito=float(input("\nInsira o valor que deseja depositar: "))
        (saldo,extrato,numero_depositos)=deposito(saldo, valor_deposito, extrato,numero_saques,numero_depositos)

        
    elif opcao == 2:
        if numero_saques==3:
            print("Número limite de saques diários atingidos, retorne outro dia ou escolha outra opção!")
            continue
        else:
            valor_saque=float(input("\nInsira o valor que deseja sacar: "))
            (saldo,extrato,numero_saques)=saque(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                numero_saques=numero_saques,
                numero_depositos=numero_depositos,
                limite_max=limite_max,
            )


    elif opcao == 3:
        print("\nTirando o extrato...\n")
        mensagem="EXTRATO"
        print(mensagem.center(54,"="))
        print("------------------------------------------------------")
        mostra_extrato(saldo,numero_saques,numero_depositos,extrato=extrato)

        print("------------------------------------------------------")
        
    
    elif opcao == 4:
         print("\nPara cadastro do novo usuário insira as informações...\n")
         
         criar_usuario(usuarios)

         print("\n........\n")

    elif opcao == 5:
        print("\nPara cadastro de nova conta insira as informações...\n")
        numero_conta= 1+len(contas)  #Inicialmente é 0, porque está vazio, aí +1, primeira conta
        
        conta= criar_conta(AGENCIA,numero_conta,usuarios) #vai ver o cpf do usuário

        if conta:
            contas.append(conta)
        
        print("\n........\n")

    elif opcao == 6:
        ao=""
        if contas==[]:
            
            print("\n")
            print(ao.center(54,"-"))
            print("\n")
            print("Não foi criada nenhuma conta até o momento!")
            print("\n")
            print(ao.center(54,"-"))
        else:
            for conta in contas:
                
                print(f"\nAgência:\t{conta['agência']}\nConta:\t\t{conta['numero_conta']}\nNúmero cpf:\t{conta['usuario']['cpf']}\nNome cliente:\t{conta['usuario']['nome']}\n") 
                print(ao.center(54,"-"))

    elif opcao == 0:
        print("\nObrigada pela preferência...")
        break
    else:
        print("\nPor favor digite uma opção válida")


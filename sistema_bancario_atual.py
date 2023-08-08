#Potência Tech powered by iFood | Ciência de Dados
#Fernanda Lima
#Criando um Sistema Bancário com Python

#Sitema permite operações de depósito, saque, extrato
#Sistema deve permitir 3 saques diários, com no máx 500 reais por saque
#Sem saldo, mensagem informando saldo insuficiente
#Todas operações armazenadas em uma variável e exibidas no extrato
#Extrato exibe todos depósitos e saques realizados
#No final da lista mostrar valor do saldo atual, formato R$ xxx.xx

saldo=1000
limite_max=500
extrato=""
numero_saques= 0
numero_depositos=0
LIMITE_SAQUES= 3
saldo_antigo=saldo


while numero_saques <= LIMITE_SAQUES:  #MELHOR UTILIZAR APENAS COM O INPUT
    #LEMBRAR DE COLOCAR SAIDA O ELSE APÓS O WHILE

    mensagem = f"""
    ################### MENU ####################

    1- Depositar
    2- Sacar
    3- Extrato
    0- Sair

    #############################################

    """
    print(mensagem)
    
    opcao=int(input("\nInsira a opção que deseja realizar: "))

    if opcao == 1:
        valor_deposito=float(input("\nInsira o valor que deseja depositar: "))

        if valor_deposito>0:
            print("\nDepositando...")
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

        
    elif opcao == 2:
        if numero_saques==3:
            print("Número limite de saques diários atingidos, retorne outro dia ou escolha outra opção")
            continue
        else:
            valor_saque=float(input("\nInsira o valor que deseja sacar: "))

            if valor_saque>0:
            
                #Não permitir tirar valores acima de 500 reais
                if valor_saque>limite_max:
                    print("Operação não permitida, seu limite diário é R$ 500.00")
                
                #Caso tente tirar um valor maior que tem no banco
                elif valor_saque>saldo:
                    print("Operação não permitida, valor de saldo insuficiente")
                else:
                    numero_saques +=1  #Se permitir, então irá sim contar como saque válido
                    
                    print("\nSacando...")

                    saldo-=valor_saque
                    print(f"\nSaldo atual: R${saldo}")

                        # No caso de não ter sido realizada nenhuma transação
                    if numero_saques==0 and numero_depositos==0:
                        extrato=saldo
                        extrato=(f"\nSaldo atual: R$ {saldo_antigo}  \nSaque: (-) R$ {valor_saque} \nSaldo atual: R$ {extrato}")
                        
                        #Caso já exista valores de saldo e saques
                    else:
                        extrato=(f"{extrato} \nSaque: (-) R$ {valor_saque} \nSaldo atual: R$ {saldo}")
                            
                    print("Numero de saques atual:", numero_saques )
            else:
                print("Não foi possível realizar a operação, informe um valor válido!")


    elif opcao == 3:
        print("\nTirando o extrato...\n")
        mensagem="EXTRATO"
        print(mensagem.center(54,"="))
        print("------------------------------------------------------")
        if numero_saques==0 and numero_depositos==0:
            print(f"Ainda não foram realizadas movimentações. Saldo atual R$ {saldo:.2f}")

        elif numero_depositos>=1 or numero_saques>=1:

            mensagem=("Transições realizadas")
            print(mensagem.center(54," "))
            print("------------------------------------------------------")
            print(f"{extrato}\n")
        print("------------------------------------------------------")

    elif opcao == 0:
        print("\nObrigada pela preferência...")
        break
    else:
        print("\nPor favor digite uma opção válida")


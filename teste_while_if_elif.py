numero_saques=0
LIMITE_SAQUES=3

while numero_saques<=LIMITE_SAQUES:  #MELHOR UTILIZAR APENAS COM O INPUT
    #LEMBRAR DE COLOCAR SAIDA O ELSE APÓS O WHILE
    opcao=int(input("\nInsira a opção que deseja realizar: "))
    print(numero_saques)
    if opcao == 1:
        print("Depósito...")
        
    elif opcao == 2:
       
        valor_saque=int(input("\nInsira o valor que deseja sacar: "))
        if valor_saque>=300:
            print ("Insuficiente")
        else:
            print("Sacando...")
            numero_saques +=1
            print(numero_saques)
        
    elif opcao == 3:
        print("Tirando o extrato...")


    elif opcao == 0:
        print("Obrigada pela preferência...")
        break
    else:
        print("""Por favor digite uma opção válida""")


import re

saldo=5000
lista=""
print(f"Ainda não foram realizadas movimentações. Saldo atual R$ {saldo:.2f}")
        
#lista= list()
print(lista)
lista = saldo
print(lista, "Valor lista")
desconto=300
saldo-=desconto
lista=(f"Saldo atual: R$ {lista:.2f}  \nSaque: (-) R$ {desconto:.2f}   \nSaldo atual: R$ {saldo:.2f}")

# texto2=(f"Chamo {lista} e tenho {saldo} anos.")
# print(texto2)

print(lista)

print()

desconto=300
saldo-=desconto
lista=(f"{lista}  \nSaque: (-) R${desconto:.2f}   \nSaldo atual: R${saldo:.2f}")

print(lista)
print("------------------------------------------------------")

num = []
for i in range(3, 15, 2):
	num.append(i)
print(num)

lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000, 20000, 50000]
print(lojas+vendas)
['Curitiba', 'Rio de Janeiro', 'São Paulo', 10000, 20000, 50000]
vendas=vendas,vendas
print(vendas)


string = "Hey! What's up?"
string = re.sub("\!|\'|\?","",string)
print(string)


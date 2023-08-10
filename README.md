# Dominando o Python Para Ciência de Dados

## Desafio 1

🔎  Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

<u><b>Criando um Sistema Bancário com Python</b></u> - <u>[Desafio de Projeto (Básico)](https://web.dio.me/lab/desafio-de-projeto-criando-um-sistema-bancario/learning/fa812356-0da6-4a85-9ffb-8b255748a288)</u>

## 📑Regras:
<table>
    <tbody> 
        <tr>
            <td>→ Sitema deve permitir operações de depósito, saque e extrato<td>
            <td>→ Sistema deve ter um limite de 3 saques diários, no valor máximo de 500 reais por saque<td>
        </tr>
        <tr>
            <td>→ Em caso de não haver saldo para transação, mensagem informando saldo insuficiente<td>
            <td>→ Todas as operações devem ser armazenadas em uma variável e exibidas no extrato<td>
        <tr>  
        <tr>
            <td>→ Extrato exibe todos depósitos e saques realizados<td>
            <td>→ No final da lista mostrar valor do saldo atual. Utilizar formato 'R$ xxx.xx' para as operações<td>
        <tr>      

<table>

<hr>
<br>

[Código do projeto realizado no VSCode](sistema_bancario_atual.py)

<hr>
<br>

## Desafio 2

🔎 Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Prepare-se para aplicar conceitos avançados de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.

<u><b>Otimizando um Sistema Bancário com Python</b></u> - <u>[Desafio de projeto (Avançado)](https://web.dio.me/lab/otimizando-o-sistema-bancario-com-funcoes-python/learning/82a55799-cfb8-479d-85a3-4982e29c90ba)</u>

## 📑Regras:
<table>
    <tbody> 
        <tr>
            <td>→ Separar as funções existentes de saque, depósito e extrato em funções. Exercitar separação em funções, por posição e por nome<td>
            <td>→ Criar duas novas funções: cadastrar usuário e cadastrar conta bancária. Vincular a conta corrente com o usuário (cliente do banco)<td>
        </tr>
        <tr>
            <td>→ Saque recebe valores por keyword only. Depósito recebe os argumentos por positional only. Extrato recebe por posição e nome.<td>
            <td>→ Criar usuário: nome, data nascimento, cpf e endereço.  Criar conta armazena em lista: agência, número conta e usuário.<td>
        <tr>  
        <tr>
            <td>→ Número conta sequencial, inicia em 1, agência fixo "0001"<td>
            <td>→ Usuário pode ter mais de uma conta, porém uma conta é apenas de um usuário<td>
        <tr>      
<table>

#### Dicas:
 
 ● As funções devem ter nomes diferentes das variáveis; <br>
 ● Verificar se sua variável é uma lista ou dicionário; <br>
 ● Quando criar listas, lembrar de colocar a definição vazio anteriormente; <br>
 ● Verificar as variáveis de retorno das funções.

<hr>
<br>

[Código do projeto realizado no VSCode](sistema_bancario_otimizado.py)

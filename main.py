from Classes.conta import Conta
import random

cliente = []

while 1==1:
    opcao = int(input("[1] - Cadastrar\n[2] - Listar Dados\n[3] - Depositar\n [4] - Sacar\n[0] - Sair"))
    match opcao:
        case 1:
            numConta = random.randint(0,1000)
            nomeCliente = str(input("Digite o nome: "))
            saldo = 0
            conta = Conta(numConta, nomeCliente, saldo)
            conta.cadastrar()
            cliente.append(conta)
            print(f"Número da Conta: {numConta}")

        case 2:
            numConta = int(input("Digite num da sua conta: "))
            for dadosCliente in cliente:
                if numConta == dadosCliente.numConta:
                    dados = dadosCliente.listarDados()
                    print(dados)

        case 3:
            numConta = int(input("Digite num da sua conta: "))
            valor = float(input("Valor a depositar: "))
            for dadosCliente in cliente:
                if numConta == dadosCliente.numConta:
                    deposito = dadosCliente.depositar(valor)
                    print(f"Valor depositado: {valor}")
        case 0:
            break
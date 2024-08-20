class Conta:
    def __init__(self, numConta, nomeCliente, saldo):
        self.numConta = numConta
        self.nomeCliente = nomeCliente
        self.saldo = saldo

    def cadastrar(self) -> bool:
        try:
            self.numConta = self.numConta
            self.nomeCliente = self.nomeCliente
            self.saldo = self.saldo
            return True
        except:
            return False

    def depositar(self, valor) -> bool:
        try:
            self.saldo = self.saldo + valor
            return True
        except:
            return False

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
        return self.saldo

    def listarDados(self) -> str:
        dados = {
            "Número da Conta: ":self.numConta,
            "Nome: ":self.nomeCliente,
            "Saldo R$ ": self.saldo
        }
        return dados
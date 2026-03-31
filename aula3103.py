class Banco:
    def __init__(self, num_conta, nome_titular, saldo):
        self.num_conta = num_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def sacar(self, valor):
        
        if(self.saldo < valor):
            print(f"Saldo insuficiente para saque!, seu saldo é {self.saldo}")
        else: 
            self.saldo -= valor
            print("Saque realizado com sucesso!") 
            print(f"Nome títular: {self.nome_titular}. Seu saldo é: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor 
        print("Depósito realizado com sucesso!")
        print(f"Nome títular: {self.nome_titular}. Seu saldo é: {self.saldo}")

    def transferir(self, valor, banco):
        self.saldo -= valor 
        banco.saldo += valor
        print("Transferência realizada com sucesso!")
        print(f"Nome títular: {self.nome_titular}. Seu saldo é: {self.saldo}")
        print(f"Nome títular: {banco.nome_titular}. Seu saldo é: {banco.saldo}")    

    def __str__(self):
        return f"{self.nome_titular}: {self.saldo}"
    
conta_1 = Banco(1, "João", 1000.00)
conta_2 = Banco(2, "Maria", 500.00)

print(conta_1)
print(conta_2)

conta_1.depositar(200.00)

conta_2.sacar(300.00)

conta_1.transferir(400, conta_2)

conta_2.sacar(1000.00)

print(f"Saldo Final conta João: {conta_1}")
print(f"Saldo Final conta Maria: {conta_2}")
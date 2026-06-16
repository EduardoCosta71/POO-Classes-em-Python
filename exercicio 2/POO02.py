class ContaBancaria:

    """
Cria conta uma conta bancariae permite fazer saques e depositos.

    """

    def __init__(self, id, titular, saldo): # Metodo Construtor

        #Atributos
        self.id = id
        self.titular = titular 
        self.saldo = saldo
        print(f"Conta criada com sucesso!")

# Metodos 
    def __str__(self):

        return f"ID = {self.id}, TITULAR = {self.titular}, SALDO = R${self.saldo:,.2f}"
    

    def deposito(self, valor):
        
        self.saldo = self.saldo + valor
        print(f"Depósito de RS{valor:,.2f} autorizado na conta {self.id}")
        

    def saque(self, valor):

        if valor > self.saldo:
            print(f"Saldo insulficiente - Saque de R${valor:,.2f} NEGADO")

        else:
            self.saldo = self.saldo - valor
            print(f"Saque realizado com sucesso {self.saldo:,.2f}")


c1 = ContaBancaria(112, "Eduardo", 3000)
c1.deposito(0)
c1.saque(4000)
print(c1)
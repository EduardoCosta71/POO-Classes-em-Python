class Funcionario:

    def __init__(self, nome, setor, cargo):

        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):

        return f"Olá, eu sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa MEGA. "
    

c1 = Funcionario("Eduardo", "T.I", "Programador")
print(c1.apresentacao())

c2 = Funcionario("Ana", "Finanças", "Contadora")
print(c2.apresentacao())
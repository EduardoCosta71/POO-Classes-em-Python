from rich import print
from rich import inspect

class Funcionario:

    empresa = "MEGA"

    def __init__(self, nome, setor, cargo):

        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):

        return f"Olá, eu sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa  "
    

c1 = Funcionario("Eduardo", "T.I", "Programador")
#inspect(c1)
print(c1.apresentacao())

c2 = Funcionario("Ana", "Finanças", "Contadora")
#inspect(c2)
print(c2.apresentacao())
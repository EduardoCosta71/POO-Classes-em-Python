from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:

    def __init__(self, nome, nick):

        self.nome = nome
        self.nick = nick
        self.jogos = list()


    def jogosFav(self, jg):

        self.jogos.append(jg)

    def ficha(self):

        conteudo = f"Nome real: {self.nome}"

        conteudo += f"\nNome jogo: {self.nick}"

        conteudo += f"\nJogos favoritos: {self.jogos}"

        painel = Panel(conteudo, title=f"Ficha <{self.nick}>", width=50)

        print(painel)
    

g1 = Gamer("Eduardo Costa", "MALOKA_RPG")
g1.jogosFav("Fortnite")
g1.jogosFav("God Of War")
g1.ficha()

    
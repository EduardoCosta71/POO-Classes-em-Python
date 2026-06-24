from rich import print
class Caneta:

    def __init__(self, cor = "azul"):

        escolha = ""

        match cor.lower().strip():
        
            case "azul":        
                escolha = "[blue]"

            case "vermelho" | "vermelha":
                escolha = "[red]"

            case "verde":
                escolha = "[green]"

            case _:
                escolha = "[white]"
        
        self.cor = escolha
        self.tampada = True


    def escrever(self, msg):

        if self.tampada:
            print(f"A {self.cor}caneta[/] está tampada")

        else:
            print(f"{self.cor}{msg}[/]")
        
    
    def quebrar_linha(self, qdt = 1):
        
        print("\n" * qdt, end='')

    def tampar(self):

        self.tampada = True
        

    def destampar(self):
        
        self.tampada = False


c1 = Caneta("azul")
c2 = Caneta ("vermelho")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá mundo")
c2.escrever("Meu nome é eduardo")
c2.quebrar_linha(6)
c3.escrever("Giovanna")

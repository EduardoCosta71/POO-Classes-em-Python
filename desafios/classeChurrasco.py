from rich import print
from rich.panel import Panel

class Churrasco:

    #Atributos de classe

    consumo_padrao: float = 0.400
    preco_kg: float = 82.40

    def __init__(self, titulo, pessoas): # Método Construtor

        self.titulo = titulo
        self.pessoas = pessoas

    def __str__(self):

        return f"Esse é {self.titulo} com {self.pessoas} pessoas participantes."
    
    #Método de Instacia
    def calcular_carne(self) -> float:

        return self.pessoas * Churrasco.consumo_padrao


    def calcular_custo_total(self) -> float:
        
        return self.calcular_carne() * Churrasco.preco_kg
    

    def calcular_custo_individual(self) -> float:

        return self.calcular_custo_total() / self.pessoas



    def analise(self):
        
        conteudo = f"Analisando o [green]{self.titulo}[/] com [blue]{self.pessoas}[/] convidados"
        
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao} Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}."
        
        conteudo += f"\nRecomendo comprar [green]{self.calcular_carne():.3f}[/] KG de carne"

        conteudo += f"\nO custo total será [red]{self.calcular_custo_total():.3f} KG [/] de carne"

        conteudo += f"\n Cada pessoa pagará [yellow]R${self.calcular_custo_individual():.2f}[/] para participante."
        
        painel = Panel(conteudo, title=self.titulo)

        print(painel)


#Objeto Instaciado
c1 = Churrasco("Churrasco", 15)
print(c1.analise())


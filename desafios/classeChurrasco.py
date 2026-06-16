class Churrasco:

    def __init__(self, titulo, pessoas):

        self.titulo = titulo
        self.pessoas = pessoas

    def analise(self):

        kg = self.pessoas * 0.4
        soma = kg * 82.40
        final = soma / self.pessoas


        return f"Analisando o {self.titulo} com {self.pessoas} convidados \nCada participante comerá 400 kl e cada Kg 82.40 \nRecomendo comprar {kg} Kg de carne \nO custo total será de R${soma:,.2f} \nCada pessoa pagará R${final:,.2f}."


c1 = Churrasco("Churrasco", 15)
print(c1.analise())


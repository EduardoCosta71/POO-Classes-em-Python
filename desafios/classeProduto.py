class Produto:

    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    def etiqueta(self):

        return f"Produto: {self.nome} - Valor: {self.preco:,.2f}"
    

p1 = Produto("PS5", 5_000)
print(p1.etiqueta())

p2 = Produto("Controle PS5", 500)
print(p2.etiqueta())

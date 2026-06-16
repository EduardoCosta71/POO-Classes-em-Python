class Pessoa: # Classe

    """
    Essa classs cria um pessoa, que tem nome idade.
    
    """

    def __init__(self, nome, idade): # Método Construtudor

        # Atributos
        self.nome = nome
        self.idade = idade

    # Método de Instancia
    def aniversario(self):
        
        self.idade = self.idade + 1

    def __str__(self): # Método

        return f"{self.nome} é uma pessoa com {self.idade} idade."
    
    def __getstate__(self):

        return f"Estado: None = {self.nome} ; idade = {self.idade}"
    
    
# Objetos Instanciado

g1 = Pessoa("Maria", 17)
g1.aniversario()
print(g1.__dict__) # Atributo
print(g1.__getstate__()) # Metodo

#print(g1.__doc__)
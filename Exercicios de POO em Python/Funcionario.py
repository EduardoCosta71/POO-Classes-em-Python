class Produto:
    
    def __init__(self, nome, preco, quantidade):
        
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def estoqueAdc(self, valor):
        
        if valor < 0:
            print("Impossivel adicionar número negativo!")
            
        else:
            
            self.quantidade = self.quantidade + valor
            print("Produto adicionado com sucesso!")
            
    
    def estoqueRet(self, valor):
        
        if valor > 0:
            print("Retirada maior que o estoque!")
                    
        else:
            
            self.quantidade = self.quantidade - valor
            print(f"Retirada realizada {self.quantidade}")
                
        
        
    def total(self):
        
       return self.quantidade * self.preco
   
   
produto = Produto("Notebook", 3000, 5)

produto.estoqueAdc(3)   # Estoque: 8
produto.estoqueAdc(-5)  # Erro

produto.estoqueRet(2)   # Estoque: 6
produto.estoqueRet(10)  # Erro
produto.estoqueRet(-2)  # Erro

print(produto.total())
        
    
        
    
        
    
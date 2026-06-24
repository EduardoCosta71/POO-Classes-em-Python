from rich import print
import time 


class Livro:

    def __init__(self, titulo, paginas):

        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: Você acabou de abrir o livro {self.titulo} que tem {self.paginas} páginas no total. Você agora está na página {self.pagina_atual}.")


    def __str__(self):

        return f"Você está na pagina {self.paginas}."


    def avancar_paginas(self, valor = 1):
        
        cont = 0

        for pg in range(0, valor, 1):

            if not self.fimLivro():

                self.pagina_atual += 1

                print(f"Pág{self.pagina_atual} :arrow_forward: ", end='')

                time.sleep(0.2)

                cont += 1

        print(f"[blue]Você avanço {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][blue]")

        if self.fimLivro():
            
            print(f":closed_book: [red]Você chegou ao final do livro {self.titulo}[/red]")


    def fimLivro(self) -> bool:

        if self.pagina_atual == self.paginas:
            return True
        
        else:
            return False

p1 = Livro("Pequeno Príncipe", 9)

p1.avancar_paginas(50)


#ex3

"""class Livro: 

    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True

    def emprestar(self):
        
        if(self.disponivel):
            self.disponivel = False
            print(f"Livro {self.titulo} emprestado com sucesso")
        else:
            print("Este livro já está emprestado, tente novamente!")

    def devolver(self):
        
        if(self.disponivel == False):
            self.disponivel = True
            print(f"Livro {self.titulo} devolvido com sucesso!")

   
livro1 = Livro("A culpa é das estrelas")
livro2 = Livro("A cinco passos de você")
livro1.emprestar()
livro1.emprestar()
livro1.devolver()
livro1.emprestar()"""

#ex4
"""class Pedido:
    def __init__(self, produto, quantidade, preco_unitario):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def descrever(self):
        valor = 0.0
        valor = self.quantidade*self.preco_unitario
        print(f"Valor tottal: {valor}")

produto = input("Digite o nome do produto")
quantidade = float(input("Digite a quantidade do produto"))
preco_unitario = float(input("Digite o preço do produto"))
p1 = Pedido(produto, quantidade, preco_unitario)

p1.descrever()"""

#ex8
class Turma:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.estudantes = []

    def apresentar(self):
        print(f"{self.nome} - {self.ano}")
        
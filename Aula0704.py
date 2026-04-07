def apresentar(self, nome, idade, curso):
     print(f"Olá, meu nome é {nome}, tenho {idade} anos e faço o curso de {curso}.")



from Aula0704p2 import Turma, Aluno



ana = Aluno("Ana", 17, "Info")
enzo = Aluno("Enzo", 17, "Info")
amanda = Aluno("Amanda", 21, "Design")

info2024 = Turma("info2024", 2024)
info2024.estudantes.append(ana)
info2024.estudantes.append(enzo)
info2024.estudantes.append(amanda)
info2024.apresentar()
  

#   """  def __init__(self, nome, idade, curso, notas):
#         self.nome = nome
#         self.idade = idade
#         self.curso = curso
#         self.notas = notas




#     def calcularMedia(self):
#         soma = 0.0
#         for i in range(0, len(self.notas)):
#             soma += self.notas[i]
            
#         media = soma / len(self.notas)
#         return media"""
    
        




    
# """nome = input("Nome: ")
# idade = int(input("Idade: "))
# curso = input("Curso: ")
# aluno1 = Aluno(nome, idade, curso, [2.5, 6, 10])
# aluno1.apresentar
# print(f"A media das notas é: {aluno1.calcularMedia()}")"""
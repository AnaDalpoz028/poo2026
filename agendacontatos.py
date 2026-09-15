from peewee import *
import datetime

db = SqliteDatabase('Agenda.db')

class BaseModel(Model):
    class Meta:
        database = db

class Contatos(BaseModel):
    nome = CharField()
    telefone = CharField()
    data_cadastro = DateTimeField()

    def __str__(self):
        return f"Nome: {self.nome} - Telefone: {self.telefone}"

db.connect()
db.create_tables( [Contatos] )


def exibir_menu():
    print("===== AGENDA DE CONTATOS =====")
    print("1 - Cadastrar contato")
    print("2 - Ver todos os contatos")
    print("3 - Buscar contato pelo nome")
    print("4 - Editar contato pelo ID")
    print("5 - Excluir contato pelo ID")
    print("6 - Sair")


def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
         nome = input("Nome: ")
         telefone = input("Telefone") 
         novo_contato = Contatos.create(nome = nome, telefone = telefone)
        elif opcao == "2":
            selecionar = Contatos.select()
            for contatos in selecionar:
                print(f"Nome: {contatos.nome} - Telefone: {contatos.telefone}")
        elif opcao == "3":
            buscar = input("Digite o nome que deseja buscar:")
            if buscar == contatos.get(Contatos.nome == buscar):
                print(f"Usuário encontrado - {buscar.nome}")
            else:
                print("Usuario não encontrado")
        

      
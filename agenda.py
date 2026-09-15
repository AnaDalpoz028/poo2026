import datetime
from peewee import *

db = SqliteDatabase('agenda.db')

class BaseModel(Model):
    class Meta:
        database = db


class contato(BaseModel):
    nome = CharField()
    telefone = CharField(unique=True)
    data_cadastro = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return f"[{self.id}] {self.nome} - Tel: {self.telefone} (Cadastrado em: {data_formatada})"

    db.connect()
    db.create_tables([contato])








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
            # --- CREATE ---
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            if contato.create(nome=nome, telefone=telefone):
                print(" Contato cadastrado com sucesso!")
            else:
                print(" Erro: Já existe um contato com esse telefone.")

        elif opcao == "2":
            # --- READ ALL ---
            contatos = contato.select()
            if not contatos:
                print("Nenhum contato cadastrado.")
            else:
                print("\n--- Lista de Contatos ---")
                for c in contatos:
                    print(c)  # Chama o método __str__() automaticamente

        elif opcao == "3":
            # --- READ (SEARCH) ---
            busca = input("Digite o nome (ou parte dele): ").strip()
            # O operador % com .contains() faz busca por substring
            resultados = contato.select().where(contato.nome.contains(busca))

            if resultados:
                for c in resultados:
                    print(c)
            else:
                print("Nenhum contato encontrado com esse nome.")

        elif opcao == "4":
            # --- UPDATE ---
            try:
                id_contato = int(input("Digite o ID do contato para editar: "))
                contato = contato.get_or_none(contato.id == id_contato)

                if contato:
                    print(f"Editando: {contato.nome}")
                    novo_nome = input(
                        "Novo nome (pressione Enter para manter o atual): "
                    ).strip()
                    novo_tel = input(
                        "Novo telefone (pressione Enter para manter o atual): "
                    ).strip()

                    if novo_nome:
                        contato.nome = novo_nome
                    if novo_tel:
                        contato.telefone = novo_tel

                    contato.save()  # Salva as alterações no banco
                    print(" Contato atualizado com sucesso!")
                else:
                    print(" Contato não encontrado.")
            except ValueError:
                print(" Por favor, digite um ID numérico válido.")

        elif opcao == "5":
            # --- DELETE ---
            try:
                id_contato = int(
                    input("Digite o ID do contato para excluir: ")
                )
                contato = contato.get_or_none(contato.id == id_contato)

                if contato:
                    contato.delete_instance()  # Remove do banco
                    print(" Contato excluído com sucesso!")
                else:
                    print(" Contato não encontrado.")
            except ValueError:
                print(" Por favor, digite um ID numérico válido.")

        elif opcao == "6":
            print("\nSaindo da agenda... Até logo!")
            db.close()
            break
        else:
            print(" Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
from classes import Jogador, Equipe

lista_jogadores = []
lista_equipes = []

def cadastrar_jogador():
    nome = input("Digite o nome do jogador:")
    nickname = input("Digite o nickname do jogador")
    turma = input("Digite a turma do jogador:")

    novo_jogador = Jogador(nome, nickname, turma)
    lista_jogadores.append(novo_jogador)

    print(f"Novo jogador {novo_jogador.nome} cadastrado com sucesso!")

def cadastrar_equipe():
    nome_equipe = input("Informe o nome da equipe:")
    jogo = input("Digite o jogo:")

    nova_equipe = Equipe(jogo, nome_equipe)
    lista_equipes.append(nova_equipe)

    print(f"Nova equipe {nova_equipe.nome_equipe} cadastrado com sucesso!")

def adicionar_jogador_a_equipe ():
pass


def listar_equipes():
    for i in range(0, len(lista_equipes)):
        print(lista_equipes[i])

def listar_jogadores():
    for i in range (0, len(lista_jogadores)):
        print(lista_jogadores[i])

    


    







print("========================================")
print("CAMPEONATO INTERCLASSE DE E-SPORTS")
print("========================================")
print("1. Cadastrar jogador")
print("2. Cadastrar equipe")
print("3. Adicionar jogador a uma equipe")
print("4. Listar todas as equipes")
print("5. Listar jogadores de uma equipe")
print("6. Buscar jogador por nickname")
print("0. Sair")
print("========================================")
print("Escolha uma opção: ")


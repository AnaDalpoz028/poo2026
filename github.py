import os

print("Configurando email...📩")
comandoEmail = "git config user.email '20251PVAI0030018@estudantes.ifpr.edu.br'"
os.system(comandoEmail)

print("Adicionando modificações...🤖")
comandoAdd = "git add *"
os.system(comandoAdd)

mensagem = input("Mensagem do commit: ")

while(len(mensagem) < 5 ):
    print("Mensagem muito pequena, detalhe mais.🥴")
    mensagem = input("Mensagem do commit: ")

print("Registrando Alterações...⚠️")
comandoCommit = f"git commit -m{mensagem}"
os.system(comandoCommit)

print("Enviando projeto ao github 🛫")
comandoPush = "git push"
os.system(comandoPush)
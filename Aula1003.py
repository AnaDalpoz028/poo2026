#Simplificar código do professor
"""alunos = [""] * 5
for i in range (0, len(alunos)):
    alunos[i] = input("Informe o nome do aluno")

cont = 1
for alu in range (0, len(alunos)):  
    print("Aluno ",cont, alunos[alu])
    cont = cont +1 """

#ex 32

"""nome = input("Digite o nome ")
idade = int(input("Digite a idade"))
sexo = bool(input("Digite o sexo"))

if (sexo == False and idade >= 30):
    print("Você foi aceita!")
elif(sexo == True and idade > 25 ):
    print("Você foi aceito!")  
elif((sexo == True or sexo == False)and (idade > 10 and idade < 15 )):
    print("Você foi aceito!")
else:
    print("Você não foi aceito.")"""

#ex1 lista 2

"""numero = [0] * 10
for i in range (0, len(numero)):
   print(numero[i]) """

#ex2 lista 2
"""num = 1
while(num < 21):
    print(num)
    num = num + 1"""

#ex3 lista 2
"""num1 = int(input("Digite um número"))
num2 = int(input("Digite um número"))



def somaDeValores(a, b):
  soma = a + b
  print("A soma é: ", soma)


somaDeValores(num1, num2)"""

#ex4 lista 2

"""cidades = [""] * 5
cidades[0] = "Paranavaí"
cidades[1] = "Umuarama"
cidades[2] = "Marilena"
cidades[3] = "Maringá"
cidades[4] = "Cianorte"

for i in range (0, len(cidades)):
    print(cidades[i])"""

#ex5 lista 2
"""def verifica_par(a):
    if (a % 2 == 0):
        return True
    else:
        return False

num = int(input("Digite um número"))
verifica_par(num)"""
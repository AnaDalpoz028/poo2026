"""def verifica_par(num):

    if(num % 2 == 0):
       return True

    else: return False

num = int(input("Digite um número"))

if(verifica_par(num)):
    print("O número", num, "é par")
else:
    print("O número", num, "é ímpar")"""

def calcular_desconto(precos, p):
    for i in range (0, len(precos)):
        desconto = precos[i] * (p/100)
        valor = precos[i] - desconto
        precos[i]  = valor
    return precos

indiceProd = 0
produtos = [""] * 10
precos = []
opc = 0
while(opc != 4):
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Aplicar Desconto")
    print("4 - Sair do programa")

    opc = int(input("Digite uma opção (um número)"))
    if(opc == 1):
        print("Cadastrar produto")
        nome = input("Nome do produto: ")
        valor = float(input("Valor do produto: R$"))
        produtos[indiceProd] = nome
        indiceProd += 1
        precos.append(valor) 


    elif(opc == 2):
        print("Listar produtos")
        for a in range (0 , len(precos)):
            print(produtos[a], " - ", precos[a])

    elif(opc == 3):
        print("Aplicar Desconto")
        d = int(input("Digite a porcentagem do desconto:"))
        preco_final = calcular_desconto(precos, d) 
        for i in range(0, len(precos)):
            print(produtos[i], " - ", preco_final[i])
        
        
    elif(opc == 4):
        print("Saindo...")
    else:
        print("Opção inválida\n")



 
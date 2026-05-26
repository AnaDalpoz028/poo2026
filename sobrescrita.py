class Calculadora:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def somar(self, a, b, c = 0):
        soma = a + b + c
        print(soma)

    def subtrair(self, a, b, c = 0):
        subtrai = a - b - c
        print(subtrai)

    def multiplicar(self, a, b, c = 1):
        multiplica = a * b * 1
        print(multiplica)

    def dividir(self, a, b):
        if b == 0:
            print("Não foi possível realizar a divisão")
        else:
            divisao = a / b
            print(divisao)

class CalculadoraCientifica(Calculadora):
    def __init__(self, marca, modelo, ano, funcoes_cientificas):
        super().__init__(marca, modelo, ano)
        self.funcoes_cientificas = funcoes_cientificas

    def potencia(self, base, expoente):
        potencia = base ** expoente
        print(potencia)

    def raiz_quadrada(self, numero):
        if numero < 0:
            print("Não existe raíz quadrada")
        else:
            numero ** 0.5
            print(numero)

print(f"Calculadora Comum")
marca = input("Qual a marca da calculadora?")
modelo = input("Qual o modelo")
ano = input("Qual o ano?")

Calculadora_a = Calculadora(marca, modelo, ano)
n1 = input("Informe um número")
n2 = input("Informe um número")

print(f"Adição: {Calculadora_a.somar(n1, n2)}")
print(f"Subtração: {Calculadora_a.subtrair(n1, n2)}")
print(f"multiplicação: {Calculadora_a.multiplicar(n1, n2)}")
print(f"Divisão: {Calculadora_a.dividir(n1, n2)}")

print("Calculadora Cientifica: ")
marca = input("Marca: ")
modelo = input("Modelo: ")
ano = input("Ano: ")
funcoes = input("Funções cientificas: ")

Calculadora_b = CalculadoraCientifica(marca, modelo, ano, funcoes)

n1 = input("Informe um número para a base")
n2 = input("Informe um número para o expoente")

Calculadora_b.potencia(n1, n2)
Calculadora_b.raiz_quadrada(81)
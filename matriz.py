class Calculo_Matrizes:
    def __init__(self):
        self.linhas = 0
        self.colunas = 0
        self.elementos = 0
        self.matriz = []

    def Ordem_matriz(self):
        print("MATRIZ")
        print("Preciso que informe a ordem da matriz que deseja fazer")
        self.linhas = int(input("Número de linhas"))
        self.colunas = int(input("Número de colunas"))
 

    def Inserir_Elementos(self):
        #for para o número de linhas
        for i in range (self.linhas):
     #cria uma "caixinha" para cada linha
            linha_atual = []

        #for para as colunas
            for j in range(self.colunas):
        #pedir para digitar qual elemento ficará na posição x y
                elementos = int(input(f"Digite o elemento da posição [{i}] [{j}]"))
        #adiciona o elemento na linha
                linha_atual.append(elementos)
    
        self.matriz.append(linha_atual)

        for linha in self.matriz:
             print(linha)   

    def Somar_Elementos(self, matriz_B):
        if self.linhas == matriz_B.linhas and self.colunas == matriz_B.colunas:
            matriz_C = []
            for i in range(self.linhas):
                    linha_atual = []
                    for j in range(self.colunas):
                        soma = self.matriz[i][j] + matriz_B.matriz[i][j]
                    #guardar a soma dentro de uma linha
                    linha_atual.append(soma)
            #guardar a linha dentro da matriz    
            matriz_C.append(linha_atual)

            print("Resultado da soma:")
            for linha in matriz_C:
                print(linha)
        else:
            print("Não foi possível realizar a soma. Verifique se a ordem das matrizes são iguais.")

    def Subtrair_Elementos(self, matriz_B):
        if(self.matriz.linhas == matriz_B.linha and self.matriz.colunas == matriz_B.colunas):
            matriz_C = []
            for i in range(self.linhas):
                    linha_atual = []
                    for j in range(self.colunas):
                        subtracao = self.matriz[i][j] - matriz_B.matriz[i][j]
                    #guardar a subtração dentro de uma linha
                    linha_atual.append(subtracao)
            #guardar a linha dentro da matriz    
            matriz_C.append(linha_atual)

            print("Resultado da subtração:")
            for linha in matriz_C:
                print(linha)
        else:
            print("Não foi possível realizar a subtração. Verifique se a ordem das matrizes são iguais.")
        
        


print("Calculadora de Matrizes")
print("Vamos criar a matriz A:")
matriz_A = Calculo_Matrizes()
matriz_A.Ordem_matriz()
matriz_A.Inserir_Elementos()

print("Vamos criar a matriz B:")
matriz_B = Calculo_Matrizes()
matriz_B.Ordem_matriz()
matriz_B.Inserir_Elementos()

print("Calculos:")
print("1 - Somar")
print("2 - Subtrair")
opcao = int(input("Como deseja calcular as matrizes?"))

if(opcao == 1):
    matriz_A.Somar_Elementos(matriz_B)
elif(opcao == 2):
    matriz_A.Subtrair_Elementos(matriz_B)










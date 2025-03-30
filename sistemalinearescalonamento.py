#Programa para calculo de Matrizes, contendo coeficiente e termos independentes nos metodos de Gauss - escalonamento
matriz = []
independentes = []
linha = int(input('Digite o numero de linhas'))
coluna = int(input('Digite o numero de colunas'))
result = 0

def gerar_matriz(l, c):
    i= 0
    while i < l:
        matriz.append([0]*c)
        i+= 1

def valores(linha, coluna):
    for l in range(linha):
        for c in range(coluna):
            matriz[l][c] = int(input(f'Digite um valor para os coeficientes na casa [{l}][{c}]: '))
            print(matriz)
    for _ in range(coluna):
        valor = int(input(f'Digite os termos independentes: '))
        independentes.append(valor)
            
def calculo(): 
    for i in range(linha - 1): 
        for l in range(i + 1, linha): 
            if matriz[i][i] == 0:
                print("Erro: pivô zero encontrado.")
                return
            fator = matriz[l][i] / matriz[i][i]  
            for c in range(coluna):  
                matriz[l][c] -= fator * matriz[i][c]
            independentes[l] -= fator * independentes[i]  
    verificacao()

def verificacao():
    if independentes[linha-1] == 0 and matriz[linha-1][coluna-1] == 0:
        print("Infinitas soluções")
    if independentes[linha-1] != 0 and matriz[linha-1][coluna-1] == 0:
        print("O sistema é Impossivel(SI)")
    if independentes[linha-1] != 0 and matriz[linha-1][coluna-1] != 0:
        print("Solução Unica")



gerar_matriz(linha,coluna)
valores(linha,coluna)
print(matriz)
calculo()
print(matriz)
print(independentes)

while True:
    print("\nMenu")
    print("1: Escolha de tamanho da matriz")
    print("2: Gerar a matriz")
    print("3: Inserir o valor da matriz dos coeficientes e da matriz independente")
    print("4: Procurar o escalonamento")
    print("5: Calcular o escalonamento")
    print("0: Sair")
    
    escolha = int (input("Escolha uma opção: "))
    
    match escolha:
        case 1:
            linha = int(input('Digite o numero de linhas: '))
            coluna = int(input('Digite o numero de colunas: '))
            print(f"Tamanho da matriz: {linha}X{coluna}")
        case 2:
            gerar_matriz(linha,coluna)
            print(f"Matriz gerada: {matriz}")
        case 3:
            matriz = valores(linha, coluna)
            print("Matriz atualizada:", matriz)
        case 4:
            print("Procurar o escalonamento: ")
            # Quando tu acabar eu add essa parte
        case 5:
            print("Cálcular o Escalonamento: ")
            # Quando tu acabar eu add essa parte tbm
        case 0:
            print("Saindo...")
            break
        case _:
            print("Opção inválida, Utilize uma das opções do menu: ")
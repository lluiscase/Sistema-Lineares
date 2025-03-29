#Programa para calculo de Matrizes, contendo coeficiente e termos independentes nos metodos de Gauss - escalonamento
matriz = []
linha = int(input('Digite o numero de linhas'))
coluna = int(input('Digite o numero de colunas'))

def gerar_matriz(l, c):
    i= 0
    while i < l:
        matriz.append([0]*c)
        i+= 1

def valores(linha, coluna):
    independentes = []
    for l in range(linha):
        for c in range(coluna):
            matriz[l][c] = int(input(f'Digite um valor para os coeficientes na casa [{l}][{c}]: '))
            
            print(matriz)
            '''for _ in range(coluna):
                independentes = int(input(f'Digite os termos independentes [{l}][{c}]: '))
                print(independentes)'''
    return matriz + [independentes]
    
gerar_matriz(linha,coluna)
print(matriz)
matriz = valores(linha,coluna)
print(matriz)

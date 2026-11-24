################################################################
# Descrição: [Ler 20 números inteiros e construir um segundo
#            vetor com o somatório de 1 até cada elemento de A.]
# Parâmetros de entrada: [20 números inteiros.]
# Valores de saída: [Elementos do vetor B.]
# Autor: [Benicio Negro Gonçalves]
################################################################

A = []
B = []

for i in range(20):
    num = int(input("Digite um número inteiro: "))
    A.append(num)

for i in range(20):
    soma = 0

    for j in range(1, A[i] + 1):
        soma = soma + j

    B.append(soma)

print("Elementos do vetor B:")

for i in range(20):
    print(B[i])
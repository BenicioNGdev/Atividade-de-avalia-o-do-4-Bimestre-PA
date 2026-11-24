################################################################
# Descrição: [Ler 15 números reais e construir um segundo vetor
#            aplicando operações conforme os índices de A.]
# Parâmetros de entrada: [15 números reais.]
# Valores de saída: [Elementos do vetor B.]
# Autor: [Benicio Negro Gonçalves]
################################################################

A = []
B = []

for i in range(15):
    num = float(input("Digite um número real: "))
    A.append(num)

for i in range(15):
    if (i + 1) % 2 != 0:
        B.append(A[i] / 2)
    else:
        B.append(A[i] * 1.5)

print("Elementos do vetor B:")

for i in range(15):
    print(B[i])
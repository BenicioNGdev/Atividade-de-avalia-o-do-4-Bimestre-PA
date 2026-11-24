################################################################
# Descrição: [Criar dois vetores com 12 elementos cada, validando
#            os valores inseridos e reunindo-os em um terceiro.]
# Parâmetros de entrada: [12 números válidos para A e 12 para B.]
# Valores de saída: [Elementos do vetor C, contendo 24 valores.]
# Autor: [Benicio Negro Gonçalves]
################################################################

A = []
B = []

for i in range(12):
    num = int(input("Digite um número divisível por 2 ou 3: "))

    while num % 2 != 0 and num % 3 != 0:
        print("Valor inválido!")
        num = int(input("Digite outro número: "))

    A.append(num)

for i in range(12):
    num = int(input("Digite um número que não seja múltiplo de 5: "))

    while num % 5 == 0:
        print("Valor inválido!")
        num = int(input("Digite outro número: "))

    B.append(num)

C = A + B

print("Elementos do vetor C:")

for i in range(24):
    print(C[i])
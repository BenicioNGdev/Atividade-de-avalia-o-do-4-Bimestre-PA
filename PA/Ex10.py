################################################################
# Descrição: [Ler 10 números inteiros e identificar os valores
#            ímpares armazenados no vetor.]
# Parâmetros de entrada: [10 números inteiros.]
# Valores de saída: [Quantidade de números ímpares e percentual
#                   do valor total dos ímpares.]
# Autor: [Benicio Negro Gonçalves]
################################################################

A = []
soma_impares = 0
total_impares = 0

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    A.append(num)

for i in range(10):
    if A[i] % 2 != 0:
        soma_impares = soma_impares + A[i]
        total_impares = total_impares + 1

percentual = (soma_impares / 10) * 100

print("Quantidade de números ímpares:", total_impares)
print("Percentual do valor total dos ímpares:", percentual, "%")
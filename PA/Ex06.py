################################################################
# Descrição: [Ler 20 temperaturas em Celsius e armazená-las em
#            um vetor, identificando a menor, a maior e a média.]
# Parâmetros de entrada: [20 valores reais de temperatura.]
# Valores de saída: [Menor temperatura, maior temperatura
#                   e média das temperaturas.]
# Autor: [Benicio Negro Gonçalves]
################################################################

A = []

for i in range(20):
    temperatura = float(input("Digite uma temperatura em Celsius: "))
    A.append(temperatura)

menor = A[0]
maior = A[0]
soma = 0

for i in range(20):
    soma = soma + A[i]

    if A[i] < menor:
        menor = A[i]

    if A[i] > maior:
        maior = A[i]

media = soma / 20

print("Menor temperatura:", menor)
print("Maior temperatura:", maior)
print("Média das temperaturas:", media)
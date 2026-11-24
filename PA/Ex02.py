################################################################
# Descrição: [Calcular o somatório dos grãos de trigo colocados
#            em um tabuleiro de xadrez, dobrando a quantidade
#            a cada novo quadrado.
# Parâmetros de entrada: [Não possui]
# Valores de saída: [Quantidade total de grãos de trigo
#                   após preencher os 64 quadrados]
# Autor: [Benicio Negro Gonçalves]
################################################################

graos = 1
total = 0

for i in range(64):
    total = total + graos
    graos = graos * 2

print("Total de grãos:", total)
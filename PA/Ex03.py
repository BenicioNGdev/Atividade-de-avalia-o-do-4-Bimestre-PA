################################################################
# Descrição: [Ler valores numéricos e calcular a soma, a média
#            e o total de valores positivos informados.
# Parâmetros de entrada: [Valores numéricos digitados pelo usuário.]
# Valores de saída: [Somatório, média e quantidade de valores
#                   positivos informados.
# Autor: [Benicio Negro Gonçalves]
################################################################

num = float(input("Adicione um numero: "))
soma = 0
total = 0

while num >= 0:
    soma = soma + num
    total = total + 1
    num = float(input("Digite outro numero: "))

if total > 0:
    media = soma / total
    print("Soma:", soma)
    print("Media:", media)
    print("Total de valores:", total)

else:
    print("Informe somente valores de 0 ou maior.")
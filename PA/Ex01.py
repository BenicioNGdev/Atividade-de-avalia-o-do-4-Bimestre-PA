################################################################
# Descrição: [Apresentar os resultados das potências de 3,
#            utilizando laços de repetição]
# Parâmetros de entrada: [Não possui]
# Valores de saída: [Resultados das potências de 3,
#                   do expoente 0 até o 15]
# Autor: [Benicio Negro Gonçalves]
################################################################

resultado = 1

for i in range(16):
    print("3 elevado a", i, "=", resultado)
    resultado = resultado * 3 
################################################################
# Descrição: [Calcular o resultado inteiro da divisão de dois
#            números utilizando laço de repetição.]
# Parâmetros de entrada: [Dividendo e divisor.]
# Valores de saída: [Resultado inteiro da divisão (quociente).]
# Autor: [Benicio Negro Gonçalves]
################################################################

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = 0

while dividendo >= divisor:
    dividendo = dividendo - divisor
    quociente = quociente + 1

print("Resultado inteiro da divisão:", quociente)
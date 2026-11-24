################################################################
# Descrição: [Calcular a área total de uma residência.]
# Parâmetros de entrada: [Nome, largura e comprimento dos cômodos.]
# Valores de saída: [Área individual e área total da residência.]
# Autor: [Benicio Negro Gonçalves]
################################################################

area_total = 0

while True:
    nome = input("Nome do cômodo: ")
    largura = float(input("Largura do cômodo: "))
    comprimento = float(input("Comprimento do cômodo: "))

    area = largura * comprimento

    print("Área do cômodo", nome, ":", area)

    area_total = area_total + area

    resposta = input("Deseja cadastrar outro cômodo? (S/N): ").upper()

    if resposta == "N":
        break

print("Área total da residência:", area_total)
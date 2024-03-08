#Distância Hamming
# Na teoria da informação, a distância de Hamming entre duas cordas de igual comprimento é o número de posições nas quais os símbolos correspondentes são diferentes. De outra forma, mede o número mínimo de substituições necessárias para transformar uma string em outra, ou o número mínimo de erros que poderiam ter transformado uma string em outra.
# A distância de Hamming recebeu o nome de Richard Hamming, que a introduziu em seu artigo fundamental sobre códigos de Hamming, códigos de detecção e correção de erros em 1950.
# É usado em telecomunicações para contar o número de bits invertidos em uma palavra binária de comprimento fixo como uma estimativa de erro e, portanto, às vezes é chamado de distância do sinal. A análise de peso de bits de Hamming é usada em diversas disciplinas, incluindo teoria da informação, teoria da codificação e criptografia.
# Por exemplo, a representação binária do número 9 é 1001 e do número 10 é 1010, portanto a distância Hamming entre eles é 2 porque você só precisa trocar os dois últimos bits 1001 para transformar 1010.
# Entrada
# A entrada consiste em uma linha composta por dois inteiros positivos em base decimal X e Y (0 ≤ X, Y < 264).
# Saida
# A saída possui uma linha contendo a distância de Hamming das representações binárias de X e Y.
# Exemplo 1
# Entrada: 9 10
# Saida: 2
# Exemplo 2
# Entrada: 6 9
# Saida: 4
# Exemplo 3
# Entrada: 7 15
# Saida: 1


def hamming_distance(x, y):

    # Convertendo os números inteiros para suas representações binárias
    binary_x = bin(x)[2:]  # Remove o prefixo '0b' da representação binária
    binary_y = bin(y)[2:]


    # Garantindo que as duas representações binárias tenham o mesmo comprimento
    max_length = max(len(binary_x), len(binary_y))
    binary_x = binary_x.zfill(max_length)
    binary_y = binary_y.zfill(max_length)

    # Calculando a distância de Hamming
    hamming_distance = 0
    for bit_x, bit_y in zip(binary_x, binary_y):
        if bit_x != bit_y:
            hamming_distance += 1

    return hamming_distance



x, y = map(int, input("Digite as coordenadas (x y): ").split())

# Chamando a função para calcular a distância de Hamming e imprimindo o resultado
print("Distância de Hamming:", hamming_distance(x, y))


exemplos = [(9, 10), (6, 9), (7, 15)]
for exemplo in exemplos:
    x, y = exemplo
    print("Entrada:", x, y)
    print("Saída:", hamming_distance(x, y))

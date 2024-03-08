

#Soma de fatoriais
# Dado um número inteiro N (1 ≤ N ≤ 10) e N números F (0 ≤ F ≤ 10), determine a soma do fatorial desses N números.
# Entrada
# A entrada consiste em uma linha contendo um número inteiro N (1 ≤ N ≤ 10) e a segunda linha com N números F (0 ≤ F ≤ 10)
# Saida
# Imprima um único número, a soma do fatorial de cada N números F.
# Exemplo 1
# Entrada: 1 4
# Saida: 24
# Exemplo 2
# Entrada: 2 4 10
# Saida: 3628824
# Exemplo 3
# Entrada: 3 0 1 2
# Saida: 4




def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n-1)


N = int(input("Digite o valor de N, sendo 1 ≤ N  ≤ 10: "))

soma_fatoriais = 0


for i in range(N):
    F = int(input(f"Digite o {i+1}º número: "))
   
    soma_fatoriais += calcular_fatorial(F)

print("A soma dos fatoriais é:", soma_fatoriais)


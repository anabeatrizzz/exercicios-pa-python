# Escreva um programa que leia um número inteiro, calcule e exiba o resultado do quadrado deste número. (usar função da classe Math)

import math
num = int(input("Escreva um numero para saber sua raiz quadrada: "))
quadrado = math.pow(num, 2)
print(f'O quadrado de {num} é {quadrado}')
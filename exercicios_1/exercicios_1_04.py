# Escreva um programa que calcule e exiba o resultado da seguinte expressão matemática: (Dica: O usuário deverá informar os valores para as variáveis A, B e C)
# A² * 5 – C / (B – A % 4)

A = float(input("Dê um valor para A: "))
B = float(input("Dê um valor para B: "))
C = float(input("Dê um valor para C: "))
conta = A ** 2 * 5 - C / (B - A % 4)
print(f'O resultado de sua conta é {conta:.2f}')
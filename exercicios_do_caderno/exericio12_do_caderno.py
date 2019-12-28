"""Desenvolva um programa que receba 20 numeros e mostre na tela o maior e o menor numero digitados."""

ma = me = 0
for c in range(1, 20+1):
    n = int(input("Digite um numero: "))
    if c == 1 or n > ma:
        ma = n
    if c == 1 or n < me:
        me = n
print(f"Maior: {ma}\nMenor: {me}")
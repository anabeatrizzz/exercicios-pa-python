"""Desenvolva um programa que receba 15 numeros e mostre na tela a soma de todos os numeros impares digitados."""

soma = 0
for c in range(1, 15+1):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        soma += 1
print(f"A soma dos numeros impares é {soma}")
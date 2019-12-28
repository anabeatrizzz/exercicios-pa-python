"""Elabore um programa que receba uma quantidade de numeros e mostre na tela a soma desses numeros. O usuario define a quantidade de numeros a ser digitado."""

n = int(input("Quantos numeros deseja somar? "))
soma = 0
while n > 0:
    soma += n
print(f"A soma é {soma}")
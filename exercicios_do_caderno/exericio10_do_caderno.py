"""Desenvolva um programa que receba 10 numeros e mostre na tela a media aritmetica."""

for c in range(1, 10+1):
    v = float(input("Digite um numero: "))
    s += v
    m = s // 10
print(f"A media é {m}")
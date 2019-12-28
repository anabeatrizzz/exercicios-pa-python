"""Elabore um programa que mostre na tela todo os numeros entre 250 e 500."""

for c in range(250, 500+1):
    print(c)

# --- Exercicio10_do_caderno ---
"""Desenvolva um programa que receba 10 numeros e mostre na tela a media aritmetica."""

for c in range(1, 10+1):
    v = float(input("Digite um numero: "))
    s += v
    m = s // 10
print(f"A media é {m}")
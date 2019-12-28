"""Desenvolva um programa que mostre na tela os primeiros 20 termos da sequencia de Fibonacci"""

t1 = 0
t2 = 1
print(f'{t1} -> {t2}')
for c in range(3, 20+1):
    t3 = t1 + t2
    print(" -> {t3}")
    t1 = t2
    t2 = t3
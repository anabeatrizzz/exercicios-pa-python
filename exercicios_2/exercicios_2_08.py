"""Escreva um programa que calcule o fatorial de um número informado pelo usuário.
Dica: O fatorial de um número N é dado pela fórmula: N! = 1 * 2 * 3 * 4 * 5 * ... * N"""

n = int(input('Digite um numero: '))
c = n
f = 1
while c > 0:
	f *= c
	c -= 1
print(f'O fatorial de {n} é {f}')

"""
Escreva um programa que calcule o fatorial de um número informado pelo usuário.
Um método chamado calcularFatorial deverá retornar o resultado final.
Dica: O fatorial de um número N é dado pela fórmula: N! = 1 * 2 * 3 * 4 * 5 * ... * N
"""

def CalcularFatorial(n):
	c = n
	f = 1
	while c > 0:
		f *= c
		c -= 1
	return f


b = int(input('Digite um número: '))
print(f'O fatorial do número digitado é: {CalcularFatorial(b)}')

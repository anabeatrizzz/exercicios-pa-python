"""Escreva um programa que leia dois valores reais e apresente
a diferença do maior para o menor. Um método chamado diferenca
deverá ser implementado para realizar o cálculo e exibir o resultado."""

def Diferenca(a, b):
	me = ma = 0
	if a > b:
		ma = a
		me = b
	if b > a:
		ma = b
		me = a
	conta = ma - me
	return conta


c = float(input('Digite um número: '))
d = float(input('Digite outro número: '))
print(f'A diferença entre os dois números digitados é: {Diferenca(c, d)}')
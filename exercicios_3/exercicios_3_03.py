"""Escreva um programa que leia três valores para os lados de um triângulo (variáveis A, B e C).
Verificar se cada lado é menor que a soma dos outros dois lados.
Se sim, saber de A==B e se B==C, sendo verdade o triângulo é equilátero;
Se não, verificar de A==B ou se A==C ou se B==C, sendo verdade o triângulo é isósceles;
E caso contrário, o triângulo será escaleno.
Caso os lados fornecidos não caracterizarem um triângulo, avisar a ocorrência.
Deverá ser implementado um método para verificar a validade de cada tipo de triângulo.
Estes métodos deverão retornar um valor lógico (true ou false)."""

def Validar(A, B, C):
	a = True
	if A <= 0 or B <= 0 or C <= 0:
		a = False
		print('Nao é possível formar um triângulo.')
	elif C == A == B or B == C:
		a = True
		print('O triângulo é isósceles.')
	elif C != A != B or B != C:
		a = True
		print('O triângulo é escaleno.')
	return a


A = int(input('Digite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
C = int(input('Digite o terceiro valor: '))
print(Validar(A, B, C))

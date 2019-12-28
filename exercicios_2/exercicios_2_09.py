"""Escreva um programa que leia vários números inteiros e ao final informe quantos números pares,
quantos números ímpares, quantos números positivos e quantos números negativos foram digitados pelo usuário.
O programa só deve parar de rodar quando o usuário responder "S" na seguinte pergunta, "Deseja encerrar o programa?".
"""

a = b = c = d = 0
while True:
	for c in range(1, 5+1):
		n = int(input('Digite um numero: '))
		if n % 2 == 0:
			a += 1
		if n % 2 != 0:
			b += 1
		if n > 0:
			c += 1
		if n < 0:
			d += 1
	print(f'\n{a} valor(es) par(es)')
	print(f'{b} valor(es) impar(es)')
	print(f'{c} valor(es) positivo(s)')
	print(f'{d} valor(es) negativo(s)')
	resp = int(input('\nDeseja encerrar o programa?\n1 - Sim\n2- Nao\n'))
	if resp == 1:
		break

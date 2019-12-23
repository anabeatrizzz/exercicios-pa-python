E = 0
C = int(input('Digite seu codigo: '))
N = int(input('Numero de horas trabalhadas: '))
if N > 50:
	E = (N - 50) * 20.00
	N = 50
salario = N * 10.00
print(f'Salario total: {salario}')
print(f'Salario excedente: {E}')
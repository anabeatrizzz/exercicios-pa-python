"""Faça um programa que leia as variáveis C e N, respectivamente código e número de horas trabalhadas de um operário.
Calcule o salário sabendo-se que ele ganha R$ 10,00 por hora.
Quando o número de horas exceder a 50, calcule o excesso de pagamento armazenando-o na variável E,
caso contrário zerar tal variável.
A hora excedente de trabalho vale R$ 20,00.
No final do processamento imprimir o salário total e o salário excedente.
O programa só deve parar de rodar quando o usuário responder "S" na seguinte pergunta, "Deseja encerrar o programa?".
"""

C = int(input('Digite seu codigo: '))
N = int(input('Numero de horas trabalhadas: '))
if N > 50:
	E = (N - 50) * 20.00
	N = 50
salario = N * 10.00
print(f'Salario total: {salario}')
print(f'Salario excedente: {E}')

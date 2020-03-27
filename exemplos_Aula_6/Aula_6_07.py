try:
	numero = int(input("Digite um numero: "))
	resultado = 100 / numero
	print(f'Resultado de 100 / {numero} é {resultado}')
except ValueError:
	print("Formato de numero invalido")
except ZeroDivisionError:
	print("O numero nao pode ser zero")
finally:
	print("Erro inesperado")

soma = 0
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

for c in range(num1, num2+1):
	if c % 2 != 0:
		soma += 1
print(f'A quantidade de números ímpares é: {soma}')
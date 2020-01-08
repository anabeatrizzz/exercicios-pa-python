def RestoPorDois(a):
	return a % 2

num = int(input("Digite um numero: "))
if RestoPorDois(num) == 0:
	print("O numero é par.")
else:
	print("O numero é impar.")
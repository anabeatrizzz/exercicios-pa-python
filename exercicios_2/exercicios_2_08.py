n = int(input('Digite um numero: '))
c = n
f = 1
while c > 0:
	f *= c
	c -= 1
print(f'O fatorial de {n} é {f}')
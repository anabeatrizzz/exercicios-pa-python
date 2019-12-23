imp = ma = me = 0
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
	ma = num1
	me = num2

if num1 < num2:
	ma = num2
	me = num1

for c in range(me, ma+1):
	if c % 2 != 0:
		imp = c
		print(imp)
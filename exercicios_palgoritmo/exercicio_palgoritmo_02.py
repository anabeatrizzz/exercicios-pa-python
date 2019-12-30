"""Elaborar um algoritmo que leia um número.
Se positivo armazene-o em uma variável chamada "A", se for negativo, em uma variável chamada "B".
No final mostrar o resultado das duas variáveis."""

A = B = 0
num = int(input("Digite um numero: "
))
if num  > 0:
	A = num
if num < 0:
	B = num
print(f"A variavel A vale: {A}\nA variavel B vale: {B}")
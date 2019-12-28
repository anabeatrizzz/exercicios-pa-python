# Escreva um programa que leia dois números inteiros, sendo armazenados respectivamente nas variáveis A e B.
# O programa deverá inverter os valores entre as variáveis, de modo que o valor da variável A seja atribuído
# na variável B e vice-versa. Ao final exibir os valores de cada variável.

A = int(input("Digite um numero: "))
B = int(input("Digite outro numero: "))

n = 0
n = A
A = B
B = n

print(f'A = {A}')
print(f'B = {B}')

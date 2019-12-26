# Escreva um programa que calcule a expressão lógica, sendo que o usuário deverá informar os valores (números inteiros)
# para as variáveis.
# ((X >= Y) AND (Z <=X)) OR ((X == W) AND (Y == Z)) OR (NOT(X != W))

X = int(input("Informe um valor para X: "))
Y = int(input("Informe um valor para Y: "))
Z = int(input("Informe um valor para Z: "))
W = int(input("Informe um valor para W: "))

conta = ((X >= Y) and (Z <= X)) or ((X == W) and (Y == Z)) or (not(X != W))

print(conta)

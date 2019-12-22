# Escreva um programa que leia a idade de uma pessoa e deverá ser exibido na tela, se esta pessoa é maior ou menor de idade (considerar 18 anos para maior idade). (Dica: Usar operadores ternários)

idade = int(input("Qual é sua idade? "))
print('Você é', ("maior" if idade >= 18 else "menor"), 'de idade')
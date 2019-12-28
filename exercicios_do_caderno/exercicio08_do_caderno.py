"""Elabore um programa que receba 4 notas e o nome de um aluno.
Calcule a média e mostre na tela se ele está aprovado ou reprovado.
Utilize a média 7 como parâmetro, se for maior ou igual a 7 o aluno está aprovado."""

nome = str(input("Qual é o seu nome? "))
nota1 = float(input("Sua nota em historia: "))
nota2 = float(input("Sua nota em matemática: "))
nota3 = float(input("Sua nota em lingua portuguesa: "))
nota4 = float(input("Sua nota em inglês: "))
media = (nota1 + nota2 + nota3 + nota4) // 4
if media >= 7.00:
    print(f"{nome} está aprovado(a)")
else:
    print(f"{nome} está reprovado(a)")
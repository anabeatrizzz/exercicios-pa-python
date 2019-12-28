"""Elabore um programa que receba o nome e as 4 notas dos alunos, calcule a media e mostre na tela
se o aluno foi aprovado com media maior ou igual a 6.
Após cada processo, pergunte se o usuario quer sair.
Se sim, pare o programa, se não, volte a pedir os dados de mais um aluno."""

nome = str(input("Qual é seu nome? "))
for c in range(1, 4+1):
    nota = float(input("Digite uma nota: "))
    s += nota
    m = s / 4
if m >= 6:
    print(f"Você foi aprovado(a) com media {m}")
else:
    print(f"Você foi reprovado(a) com media {m}")
resp = int(input("Deseja cadastrar outro aluno(a)?\n1 - Sim\n2 - Não"))
while resp == 1:
    nome = str(input("Qual é seu nome? "))
    for c in range(1, 4+1):
        nota = float(input("Digite uma nota: "))
        s += nota
        m = s / 4
    if m >= 6:
        print(f"Você foi aprovado(a) com media {m}")
    else:
        print(f"Você foi reprovado(a) com media {m}")
    resp = int(input("Deseja cadastrar outro aluno(a)?\n1 - Sim\n2 - Não"))
    if resp == 2:
        break

```python
"""
Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação.
Calcular a média de aproveitamento, usando a fórmula:
MA = (Nota1 + Nota2 . 2 + Nota3 . 3 + ME) / 7
A atribuição de conceitos obedece a tabela abaixo:
"""
```
Média de aproveitamento|Conceito
---|---
9,0|A
7,5 e < 9,0|B
6,0 e 7,5|C
4,0 e 6,0|D
< 4,0|E

```pyhton
"""
O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o conceito for A,B ou C e REPROVADO se o conceito for D ou E.
"""
```

```python
idd = int(input("Qual seu numero de identificação? "))
nota1 = float(input("Sua primeira nota: "))
nota2 = float(input("Sua segunda nota: "))
nota3 = float(input("Sua terceira nota: "))

ME = (nota1 + nota2 + nota3) / 3
MA = (nota1 + nota2 * 2 + nota3 * 3 + ME) / 7

con = ''

if MA > 9.00:
	con = 'A'
	print(f"Seu numero de identificação é: {idd}\nSuas notas são {nota1}, {nota2}, {nota3}\nSua média é: {ME}\nSua média de aproveitamento é: {MA:.2f}\nSendo assim, seu conceito é {con} e você está \033[32mAPROVADO(A)\033[m")
elif 7.50 <= MA <= 9.00:
	con = 'B'
	print(f"Seu numero de identificação é: {idd}\nSuas notas são {nota1}, {nota2}, {nota3}\nSua média é: {ME}\nSua média de aproveitamento é: {MA:.2f}\nSendo assim, seu conceito é {con} e você está \033[32mAPROVADO(A)\033[m")
elif 6.00 <= MA <= 7.50:
	con = 'C'
	print(f"Seu numero de identificação é: {idd}\nSuas notas são {nota1}, {nota2}, {nota3}\nSua média é: {ME}\nSua média de aproveitamento é: {MA:.2f}\nSendo assim, seu conceito é {con} e você está \033[32mAPROVADO(A)\033[m")
elif 4.00 <= MA <= 6.00:
	con = 'D'
	print(f"Seu numero de identificação é: {idd}\nSuas notas são {nota1}, {nota2}, {nota3}\nSua média é: {ME}\nSua média de aproveitamento é: {MA:.2f}\nSendo assim, seu conceito é {con} e você está \033[32mAPROVADO(A)\033[m")
elif MA < 4.00:
	con = 'E'
	print(f"Seu numero de identificação é: {idd}\nSuas notas são {nota1}, {nota2}, {nota3}\nSua média é: {ME}\nSua média de aproveitamento é: {MA:.2f}\nSendo assim, seu conceito é {con} e você está \033[31mREPROVADO(A)\033[m")
```
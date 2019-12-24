"""Tendo como dados de entrada a altura e o sexo de uma pessoa,
faça um programa que calcule o peso ideal,
utilizando as seguintes fórmulas: (h = altura)
- Para homens: (72.7*h) - 58
- Para mulheres: (62.1 *h) - 44.7
Um método chamado calcularPesoIdeal deverá ser implementado
para a realização do cálculo, sendo que deverá receber por
parâmetro o sexo e a altura da pessoa."""

def CalcularPesoIdeal(a, g):
	p = 0
	if g.upper() == 'MASCULINO' or g.upper() == "M":
	 p = (72.7 * a) - 58
	if g.upper() == 'FEMININO' or g.upper() == "F":
		p = (62.1 * a) - 44.7
	return p


a = float(input('Informe sua altura: '))
g = str(input('Informe seu gênero: ')).upper()
print(f'O peso ideal para você seria {CalcularPesoIdeal(a, g)}')
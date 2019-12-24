```python
"""Escreva um programa que retorne o número do quadrante (1,2,3 ou 4) através de um método chamado verificaQuadrante, que deverá receber um valor para x e um valor para y (coordenadas)."""
```
# Quadrantes:
![Quadrantes](http://i.imgur.com/vnxAqN5.png)

```python
def VerificaQuadrante(x, y):
	quad = ""
	if x > 0 and y > 0:
		quad = "primeiro quadrante"
	elif x > 0 and y < 0:
		quad = "quarto quadrante"
	elif x < 0 and y < 0:
		quad = "terceiro quadrante"
	elif x < 0 and y > 0:
		quad = "segundo quadrante"
	elif x == 0 and y == 0:
		quad = "origem"
	return quad


x = int(input("Digite um numero para a coordenada x: "))
y = int(input("Digite um numero para a coordenada y: "))
print(f"As coordenadas digitadas estão no(a) {VerificaQuadrante(x, y)}")
```
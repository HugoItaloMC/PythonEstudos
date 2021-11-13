"""
3)
 Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos componentes
deste vetor, armazenando o resultado em outro vetor. Os conjuntos tem 10 elementos cada.
Imprimir todos conjuntos
"""


a = set()
v1 = []
v2 = []
for v in range(0, 10):
    v = float(input("Digite valor real : "))
    a.add(v)
    v **= v
    v1.append(v)
for n in v1:
    v2.append(n)
print(a)
print(v2)

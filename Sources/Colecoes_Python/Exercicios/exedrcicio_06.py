"""
6)
 Faca um programa que receba do usuario um vetor com 10 posicões.
Em seguida devera informar o maior e o menor número digitado
"""


n = []
maior = -9999
menor = 999
for i in range(10):
    i = int(input("Digite valor : "))
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
    else:
        n.append(i)

n.insert(0, maior)
n.insert(1, menor)
print(f"Números digitados : {n}\tMaior número digitado {n[0]}\tMenor número digitado {n[1]}")

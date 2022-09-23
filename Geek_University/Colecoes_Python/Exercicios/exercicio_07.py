"""
7)
 Escreva um programa que leia 10 números inteiros e os armazenem em um vetor.
 Imprima o vetor, o maior elemento e a sua posicão
"""
n = []
maior = 0

for i in range(10):
    i = int(input(f"Digite valor {i+1} : "))
    n.append(i)
    if i > maior:
        maior = i


print(f"Números digitados : {n}\tMaior número digitado {maior} posicão {n.index(maior)}")



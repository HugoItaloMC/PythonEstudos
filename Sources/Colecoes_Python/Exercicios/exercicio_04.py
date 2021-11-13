"""
 4)
 Faca um programa que leia um vetor de 8 posicões e, em seguida, leia também dois valores X e Y
quaisquer correspondentes a duas posicões no vetor. Ao final seu programa deverá escrever a soma
dos valores encontrados nas respectivas posicões X e Y.
"""


v1 = list(range(0, 8))
for n in v1:
    print(n)
print(f"{v1[3]}  {v1[6]}\t{v1[3] + v1[6]}")
"""
5)
 Leia um vetor de 10 posicões, contar e escrever quantos valores pares tem
"""


v = [[]]
for i in range(10):
    i = int(input("Digite valor : "))
    v.append(i)
    if i % 2 == 0:
        v[0].append(i)

print(f"Números digitados {v[1::1]}\ttotal Números pares {len(v[0])} : {v[0]}")
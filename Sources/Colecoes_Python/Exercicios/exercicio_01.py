"""
1) :
 Faca um programa que possua um vetor denominado 'a' que armazene 6 valores inteiros.
O programa deve executar os seguintes passos:
"""
#   A) Atribua os seguintes valores :


a = [1, 0, 5, -2, -5, 7]

#   B) Armazene em uma variável inteira simples a soma dos seguintes valores das posicões :


b = a[0] + a[1] + a[5]
print(b,'\n')


#   C) Modifique o vetor na posicão '4', atribuindo o valor 100 a essa posicão :


a.insert(4, 100)


#   D) Mostre na tela cada valor do vetor 'a' um em cada linha :


for n in a:
    print(n)
'''
Trabalhando com módulos Built'in. Módulos integrados que já vem instalados no Python

Link da Documentacão oficial de todos Módulos Built'in da linguagem Python
https://docs.python.org/pt-br/3/py-modindex.html


'''


from random import randint as rdi # Podemos renomar as funcões ultilizando o alias ' as '
# Exemplos complexo:

try:
   quantidade_loop = int(input("Digite Quantidade de loops: "))
except (ValueError, NameError, ArithmeticError, TypeError) as err:  # Tratando erros Built-in's do Python
    print(f"ERRO : {err}")  # Saída de Erro
else:
    for _ in range(1, quantidade_loop):
        print(rdi(1, quantidade_loop*33), end=f' {input("Digite Seu Token: ")}, -^ \tSeu Token\n')

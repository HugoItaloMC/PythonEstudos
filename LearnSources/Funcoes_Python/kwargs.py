"""
**kwargs

    - Poderíamos chamar este parametro de (**x, **n, **par) mas por convencão da comunidade chamamos de **kwargs
    - Este é só mais um parametro, mas diferente do *args que coloca os valores em uma tuple, o **kwargs exige
que ultilizemos parametros nomeados, e transforma esses parametros em um dict.

    - Nas nossas funcões, podemos ter (NESTA ORDEM):
        - Parametros obrigatórios;
        - *args;
        - Parametros default (não obrigatório);
        - **kwargs
"""


# Exemplo :


def cores_fav(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa.title()} é {cor}\n")


cores_fav(marcos=f'{input(": ")}')


# Exemplo mais complexo :


def cumprimento_esp(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python': return 'Voce recebeu um cumprimento Python'
    elif 'geek' in kwargs: return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem é voce...'


print(cumprimento_esp(geek='Oi'))
print(cumprimento_esp(geek='Python'))
print(cumprimento_esp())


def minha_fun(nome, idade, *args, est_civil=False, **kwargs):
    print(f"{nome} tem {idade} anos")
    print(args)
    est_civil = 'Casado' if est_civil is True else 'Solteiro'
    print(est_civil)
    print(kwargs)


minha_fun('julia', 8)
minha_fun('Renan', 18, 11, 22, 44, est_civil=True)
minha_fun('Carlos', 34, 11, 55, 1001, est_civil=False, curso='Python', profissao='Dev')


# Desempacotando com **kwargs:


def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nome = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nome(**nome))


def soma_total(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
cjt = {1, 2, 3}
dic = dict(a=1, b=2, c=3)


# dic = dict(d=1, e=2, f=3)     # TypeError


soma_total(*lista)
soma_total(*tupla)
soma_total(*cjt)
soma_total(**dic)

# OBS : Os nomes das chaves do dict devem ser os mesmos dos parametros da funcão

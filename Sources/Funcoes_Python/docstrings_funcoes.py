"""
Documentando funcões
    - A solucão na qual a funcão atende deve ser comentada 'docstring'
    - Podemos acessar a docstring de uma funcão ultilizando:
        .__doc__
        help()
"""
def diz_oi():
    """ Uma funcão simples que retorna a palavra 'Oi !' """
    return 'Oi !'

print(f"{help(diz_oi)}",f"\n{diz_oi.__doc__}")   # Retorna a docstring de uma funcão


def expo(n1, pot=2):
    """
    Funcão que retorna por pedrão o quadrado de n1 ou a pot informada no argumento.
    :param n1 : numero que desejamos gerar o exponencial.
    :param pot : Potencia que queremos gerar o exponencial de 'n1' . Por padrão o 2
    :return : Retorna exponencial de 'n1' por 'pot'
    """
    return n1 ** pot


print(expo(2, 4))
print(expo.__doc__)
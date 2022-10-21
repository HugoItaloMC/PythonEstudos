# Forcando tipo de dados com Decorators
def forca_tipo(*tipos):  # Decorador, cabecalho da funcão que é chamada
    def decorator(funcao):  # Funcão Decoradora de outras funcões
        def pattern_converte_tipo(*args, **kwargs):  # Padrão para receber multiplas assinaturas de funcões
            # Lembre-se *args é uma tupla, e tupla são imútaveis
            novo_args = []  # Convertando *args em lista para aplicar métodos
            # iterando sobre parametro do decorador (*tipos) e sobre o da funcão decoradora (*args)
            for (valor, tipo) in zip(args, tipos):  # 1:
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return pattern_converte_tipo
    return decorator


"""
1: A funcao zip() cria conjuntos de tuplas, juntando os valores das posicoes de indices dos iteraveis conforme o tamanho 
dos iteráveis, há primeira tupla que o zip() gera aloca todos os valores da primeira posicão dos iteráveis passados como 
argumentos, e assim sequencialmente até o fim das ocorrências dos iteráveis.
   Os argumentos informados no parametro do Decorator 'forca_tipo' vai ser alinhado com os argumentos passado nos 
parametros da funcão que vai ser decorada utilizando o comando zip() pela iteracão com o 'for', devemos saber quantos 
parametros a funcão há ser decorada vai conter para assim forcarmos o tipo de cada valor dos argumentos na funcão há ser 
decorada. O acumulador 'novo_arg' é instânciado pela iteracão dos iteráveis passados no método zip() forcando o tipo de 
valores nos argumentos passados na funcão há ser decorada.
"""


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for _ in range(vezes):
        print(msg)


@forca_tipo(float, float)
def dividir(a, b):
    return a / b

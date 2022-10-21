"""
  # Preservando Metadados com wraps

  - Metadados, são dados intrísecos em arquivos
  - wraps, são funcões que envolvem elementos com diversas finalidades
"""
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)  # Preservando metadados da funcão decorada
    def logar(*args, **kwargs):
        print(f"Você está chamando {funcao.__name__}")
        print(f"Aqui a documentacao {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """ Soma dois números. """
    return a + b


#  Testando
print(f"Resultado funcão {soma.__name__}: {soma(10, 30)}")
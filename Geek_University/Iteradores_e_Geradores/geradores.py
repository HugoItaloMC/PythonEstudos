"""
Geradores

- Geradores conhecidos como "generators" são iteradores "iterators"

OBS : O contrário não é verdadeirom nem todos iterators é um generator

 - Generators pode ser criados com funcões geradoras ;
 - Funcões geradoras utilizam a palavra reservada yield;
 - Generators podem ser criados com Expressões Geradoras;

 DIFERENCA ENTRE FUNCÕES E GENERATORS FUNCTIONS (Funcões Geradoras)
 ----------------------------------------------------------------------------
 |Funcões                           | Generators Functions                  |
 ----------------------------------------------------------------------------
 |utilizam return                   | utilizam yield                        |
-----------------------------------------------------------------------------
|retorna uma vez                    | podem utilizar yield multiplas vezes  |
-----------------------------------------------------------------------------
|quando executada, retorna um valor | quando executada, retorna generator   |
-----------------------------------------------------------------------------
"""

# Exemplo Generator Function:

def conta_ate(valor_maximo):
    contador = 1
    while contador =< valor_maximo:
        yield contador
        contador += 1
# OBS : Uma funcão geradora não é um generator, ela gera um generator;


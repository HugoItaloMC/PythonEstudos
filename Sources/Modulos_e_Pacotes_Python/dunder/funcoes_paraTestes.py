"""
Documento de testes para entendimento das funcões built'in __name__ e '__main__'
"""


# Declarando funcão

def somaImpar(a):
    total = 0
    for n in a:
        if n % 2 != 0:
            total += + n
    return total


"""
 # Abaixo declaramos que as saídas só devem ocorrer neste arquivo que no caso de uma importacãoo do módulo
as saídas não ocorrerá no arquivo em que foi importado o módulo. Que se a variável __name__ for igual a variável
'__main__' ocorre o escopo onde está sendo ultilizado as funcões declaradas no módulo
"""
if __name__ == '__main__':  # A partir daqui, o bloco só é executado diretamente
    print(somaImpar([n for n in range(100)]))

print(f"{__name__} foi importado")

"""
 Quando o módulo é importado o built'in __name__ na importacão passa a se chamar 'nome_do_arquivo_de_origem' 
quando executado diretamento no módulo de destino em que foi importado
"""
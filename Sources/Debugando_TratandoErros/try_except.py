"""
Bloco Try Except

Ultilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagem de erro inesperada.

Forma geral do bloco :

try:
    /// execucão problemática
except:
    /// o que deve ser feito no caso do erro

"""


# Tratando um erro genérico

try:
    geek()
except:
    print('Algo deu errado na funcão geek()')

# Tente executar a funcão geek(), caso de algum erro, imprima a mensagem !!
"""
Sempre tente tratar o erro de uma forma especifica, especificando. Tratar de forma genérica não
é a melhor opcão
"""

# Tratando o erro de uma forma especifica

try:
    geek()
except NameError:
    print('Algo deu errado na funcão geek()')

try:
    len(5)
except TypeError:
    print("Algo deu errado no processo de execucão")

# Tratando erro de forma especifica, passando mais detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f"Algo deu errado no processo de execucão, erro '{err}'")

# Esta menssagem de erro normalmente ñ é passada para o usuário final, mas armazenadas nos log da aplicacão.

try:
    #len(5)
    geek()
except TypeError as erra:
    print(f"Deu TypeError : {erra}")
except NameError as errb:
    print(f"Deu NameError : {errb}")
except:
    print("Erro Desconhecido !")


# Tratando excessões em funões

def entrada(chave, valor):
    try:
        return chave[valor]
    except:
        return None

dic = {"nome": "carol"}

print(entrada(dic, "nome"))

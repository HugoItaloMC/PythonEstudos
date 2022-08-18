"""
 Faca um programa que o usuário cadastre o nome e o telefone, e digite 'Q'
para finalizar e sair do programa e 'N' para cadastrar novos usuários
"""
def cadastro():
    put = ''.join([line for line in [f"{input('Nome : ')}", f"{input('Telefone: ')}"]])
    return put

if __name__ == '__main__':

    try:
        with open('/home/correia/PycharmProjects/MyPythonSources/LearnSources/leituraEscrita_emArquivos/Exercicios/ManipulandoArquivos_Sec_13/Exercicio13/cadastro.txt'
                , 'w+') as arq:
            while True:
                n = input("Digite 'Q' para sair e 'N' para novo cadastro: ").lower()
                if n != 'q':
                    arq.write(cadastro())
                else:
                    break

    except Exception as err:
        while err:
            n = input("Digite 'Q' para sair e 'N' para novo cadastro: ").lower()
            if n != 'q':
                arq.write(cadastro())
            else:
                break

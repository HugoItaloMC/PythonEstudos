"""
  Faca um programa que receba um vetor de 10 números, converta cada um desses números para binários
e grave a sequências de 0s e 1s em um arquivo de testo. Cada número deve ser gravado em uma linha.

"""
try:
    #   OBS ! : Para formatar uma string em um binário, os caracteres deve ser alfanúmericos [0-9],
    # caracteres literais [a-zA-Z] ñ pode ser convertido para binários.
    vetor_ten = range(1, 11)
    with open(f"{input('Digite Nome do arquivo de para armazenamento: ')}.txt", "w+") as arq:
        for line in vetor_ten:
            arq.write(f"{line:b}\n")
except Exception as err:
    print(f"Error %% {err}")
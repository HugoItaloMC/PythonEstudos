"""
 Faca um programa que receba do usuário um arquivo que contenha o nome e a nota de diversos alunos
(da seguinte forma NOME: JOAO, NOTA: 8), um aluno por linha. Mostre na tela o nome e a nota do aluno
que possui a maior nota.

"""

try:
    with open("notas_alunos.txt", "w+") as arq:
        continue_: str
        continue_ = input('Finalizar ou Continuar (s/n) : ').lower()
        while continue_ != 'n':
            entrada_: object
            entrada_ = {input('Aluno: '): int(input('Nota: '))}
            for key, value in entrada_.items():
                arq.write(f"Aluno : {key} Nota : {value}\n")
            continue_ = input('Finalizar ou Continuar (s/n) : ').lower()
            if continue_ == 'n':
                entrada_max = entrada_[max(entrada_, key=entrada_.get)]
                for key, value in entrada_.items():
                    if entrada_max == value:
                        with open("maior_nota.txt", "w+") as arq_after:
                                arq_after.write(f"Aluno : {key} contém a maior nota : {value}")
except Exception as err:
    print(f"Error %% {err}")

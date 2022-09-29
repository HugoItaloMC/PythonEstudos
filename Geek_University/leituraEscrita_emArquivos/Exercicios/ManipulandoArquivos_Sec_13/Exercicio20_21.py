"""
 Faca um programa que receba uma diciplina e a quantidade de alunos matriculados de um curso, dinamicamente
alocado vai ser os dois vetores o primeiro para armazenar os dados dos alunos e o segundo seu nome e sua
respectiva nota. Se o nome ñ conter 40 caracteres complete com espacos vazios até conter 40 caracteres.

"""

# Iniciando curso e matricula
import re
try:
    aluno_:   list[str]
    entrada_: list[str, int]
    continue_: str
    quit_: str
    re_name = re.compile(r':.*[a-z]', re.I)
    with open("aluno_cadastro_curso.txt", "w+") as arq:
        while True:
            continue_ = input('******\n\n[C]-\tCadastro Curso \n[A]-\tCadastro Alunos \n: ').lower()
            if continue_ == 'c':
                entrada_ = [input('\t**Iniciando Curso ->\nDiciplina: '),
                            int(input('Quantidade de Vagas: '))
                            ]
            elif continue_ == 'a':
                for _ in range(1, entrada_[1]+1):
                   aluno_ = [input('\n%% Cadastro Aluno %%\nNome : '),
                              input('Data de Nascimento : ')
                             ]
                   arq.write(f"Diciplina -> {entrada_[0]}\n%%-\t Dados Aluno %%\n-\tNome : {aluno_[0]} \n-\tData de Nascimento: {aluno_[1]}\n\n")
            quit_ = input('\n\nSair [Q] | Retornar [V] : ')
            if quit_ == 'q':
                break
    with open('aluno_cadastro_curso.txt', "r+") as arq_after:
        arq_after = arq_after.read()
        notas_: object
        with open("notas_alunos.txt", "w+") as arq_fast:
            arq_name = '\n'.join([line.group() for line in re.finditer(re_name, arq_after)]).split('\n')
            for line in arq_name:
                notas_ = {line: int(input(f'** Atribuindo notas\nAluno {line}\n-\tNota : '))}
                for key, value in notas_.items():
                    arq_fast.write(f"\n**\n-\tAluno {key}\n-\tNota: {value}")
                    #  arq_fast.write(f"\n**\n-\tAluno {key}\n-\tNota: {value:b}") Retorna binários de alfanuméricos
except Exception as err:
    print(f"Error %% {err}")

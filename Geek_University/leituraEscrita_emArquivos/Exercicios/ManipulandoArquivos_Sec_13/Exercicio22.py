"""
 Faca um programa que receba como entrada o nome de um arquivo de entrada e um arquivo de saída.
 O arquivo de entrada contém o nome de alunos seguido de 3 (três) inteiros referente as suas notas.
 O arquivo de saída deve conter o nome do aluno e suas respequitivas notas em ordem crescente

"""
try:
    with open("notas_alunos.txt", "w+") as arq:
        continue_: str
        continue_ = input('Finalizar (s/n) : ').lower()
        while continue_ == 'n':
            entrada_: object
            entrada_ = {input('Aluno: '): [int(input('Nota 1 : ')),
                                           int(input('Nota 2 : ')),
                                           int(input('Nota 3 : '))
                                           ]}
            for key, value in entrada_.items():
                arq.write(f"Aluno : {key} Nota : {sorted(value)}\n")
            continue_ = input('Finalizar (s/n) : ').lower()
            if continue_ == 's':
                break
except Exception as err:
    print(f"Error %% {err}")

"""
 Faca um programa que leia a profissão e o tempo de servico em anos de cada um dos 5 funcionários, armazene
os dados em arquivo chamado 'emp.txt'.

"""
try:
    with open("emp.txt", "w+") as arq:
        continue_: str
        continue_ = input('Finalizar (s/n) : ').lower()
        data_now = input('\nData atual \n-\tDD/MM/AAAA : ')
        while continue_ == 'n':
            entrada_: object
            entrada_ = [input('\nColaborador: '),
                        input('Setor : '),
                        float(input('Salario : ')),
                        input('Data Inicio : ')
                        ]
            data_size = int(data_now[6:]) - int(entrada_[3][6:])
            arq.write(f"Funcionario {entrada_[0]} Inicio {entrada_[3]} Tempo de Casa {data_size} anos")
            continue_ = input('Finalizar (s/n) : ').lower()
            if continue_ == 's':
                break
except Exception as err:
    print(f"Error %% {err}")

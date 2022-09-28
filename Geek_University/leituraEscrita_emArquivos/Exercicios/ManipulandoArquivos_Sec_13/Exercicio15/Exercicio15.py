"""
 Faca um programa que receba como entrada o ano corrente e o nome de dois arquivos:
 - Um de entrada e outro de saída. Cada linha do arquivo de entrada contém o nome  de uma pessoa
contento no máximo 40 caracteres e o seu ano de nascimento. O programa deverá ler o arquivo de entrada
gerar o arquivo de saída onde aparece o nome da pessoa seguida da string que representa sua idade.

  - Se a idade for maior que 18 "maior de idade"
  - Se a idade for menos que 18 "menor de idade"
  - Se a idade for igual a 18 "entrando na maior idade"

"""

# Arquivo de entrada



try:
    entrada_ : list[str]
    entrada_ = [input('$$ -> \n Digite data atual: '),
                input('******\n Digite Seu nome: '),
                input(f"***\n Digite sua data de Nascimento: ")]
    data_atual = int(entrada_[0][6:])
    data_nascimento = int(entrada_[2][6:])
    idade_atual = data_atual - data_nascimento

    with open(f"\t{input('(((((.))))) Digite nome do seu arquivo de armazenamento: ')}.txt", 'w+') as arq:
        for line in entrada_:
            if len(line) < 40:
                arq.write(f"{line} ")
except Exception as err:
    print(f"Error ## {err}")
else:
    with open(f"\t{input('(((((.))))) Digite nome do seu arquivo saída: ')}.txt", 'w+') as arq2:
        if idade_atual >= 18:
            arq2.write(f"{entrada_[1]} nasceu em {data_nascimento} tem {idade_atual} anos, maior de idade !!")
        else:
            arq2.write(f"{entrada_[1]} nasceu em {data_nascimento} tem {idade_atual} anos, menor de idade !!")
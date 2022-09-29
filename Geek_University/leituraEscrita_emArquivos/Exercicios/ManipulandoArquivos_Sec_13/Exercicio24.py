"""
 Faca um programa simples de gerenciamento de estoque doméstico, o programa deve conter os seguintes requisitos
 - Cadastro de produtos e quantidades
 - Consulta de produtos 
 - Atualizar quantidade de produtos (update)
"""

try:
    while True:
        import re

        produto_:   list[str]
        tipo_: list[str, int]
        menu_: str
        re_name = re.compile(r'Nome :.*[a-z]', re.IGNORECASE)
        re_size = re.compile(r'Quantidade.*[0-9]', re.IGNORECASE)
        re_struct = re.compile(r'Nome :.*\n-.*\n.*', re.IGNORECASE)
        struct_ =  lambda x: [line.group() for line in re.finditer(re_struct, x)]
        struct_name = lambda x: [line.group() for line in re.finditer(re_name, x)]
        struct_size =lambda x: [line.group() for line in re.finditer(re_size, x)]
        # Cadastro Produtos e quantidades, Segmentos e Variedades:
        menu_ = input('******\n'
                      '[E]-\tIniciar Estoque\n'
                      '[C]-\tConsultar Produto\n'
                      '[X]-\tFechar\n: '
                      ).lower()
        print('\n' * 8)
        (menu_)
        if menu_ == 'x':
            
            break
        while menu_ == 'e' or menu_ == 'p' or menu_ == 's':
            menu_ = input('******\n'
                          '[S]-\tSegmento e Variedades\n'
                          '[P]-\tCadastro Produto\n'
                          '[Q]-\tRetornar\n: '
                          ).lower()
            print('\n' * 8)
            if menu_ == 's':
                tipo_ = [input('\t**Iniciando Estoque ->\nSegmento: '),
                         int(input('Variedades : '))
                         ]
                print('\n' * 8)
            elif menu_ == 'p':
                for _ in range(1, tipo_[1]+1):
                    produto_ = [input('\n%% Cadastro produto %%\nNome : '),
                                input('Data de Validade : '),
                                int(input('Quantidade : '))
                                ]
                    print('\n' * 8)
                    with open("produto_cadastro_produto.txt", "a+") as arq:
                        arq.write(f"Tipo -> {tipo_[0]}\n"
                                  f"-\t%% Produto %%\n"
                                  f"-\tNome : {produto_[0]}\n"
                                  f"-\tQuantidade : {produto_[2]}\n"
                                  f"-\tData de Validade : {produto_[1]}\n\n"
                                  )
            elif menu_ == 'q':
                print('\n' * 8)
                break
        while menu_ == 'c' or menu_ == 'l' or menu_ == 'a' or menu_ == 'b':
            menu_ = input('\n*************\n'
                          '[L]-\tListar Produtos\n'
                          '[A]-\tDados de Produtos\n'
                          '[B]-\tAtualizar Quantidade de Produto(s)\n'
                          '[Q]-\tRetornar\n: '
                          ).lower()
            print('\n' * 8)
            if menu_ == 'l':
                with open('produto_cadastro_produto.txt', "r+") as arq_after:
                    arq_name = struct_name(arq_after.read())
                print(re.sub(r'Nome : ', 'Produto : ', '\n'.join(arq_name)))
            elif menu_ == 'a':
                while True:
                    menu_consulta = input('\n*************\n'
                                          '\t\t%% Consultar Produto(s) %%\n'
                                          '[L]-\tLista Geral\n'
                                          '[A]-\tSelecionar Produto\n'
                                          '[Q]-\tRetornar\n: '
                                          ).lower()
                    print('\n' * 8)
                    if menu_consulta == 'l':
                        with open('produto_cadastro_produto.txt', "r+") as arq_after:
                            arq_name = struct_(arq_after.read())
                        print(re.sub(r'Nome : ', 'Produto : ', '\n'.join(arq_name)))
                    elif menu_consulta == 'a':
                        (...)
                    elif menu_consulta == 'q':
                        print('\n' * 8)
                        break
                    else:
                        print(f'Error %% Invalid Option {menu_consulta.upper()}')
                        print('\n' * 8)
            elif menu_ == 'b':
                (...)
            else:
                break
except Exception as err:
    print(f"Error %% {err}")

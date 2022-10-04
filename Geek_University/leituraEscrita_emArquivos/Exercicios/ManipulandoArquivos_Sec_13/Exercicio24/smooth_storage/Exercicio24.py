"""
 Faca um programa simples de gerenciamento de estoque doméstico, o programa deve conter os seguintes requisitos
 - Cadastro de produtos e quantidades
 - Consulta de produtos 
 - Atualizar quantidade de produtos (update)
"""
import re
import os

category_storage = os.path.join(os.getcwd(), 'product/storage')  # Path da pasta de produtos (nome, quantidade, dataVal)
category_list = os.path.join(os.getcwd(), 'product/cast')

re_name = re.compile(r'[a-z ]', re.IGNORECASE)
re_size = re.compile(r'Quantidade :.*[0-9]', re.IGNORECASE)
re_struct = re.compile(r'Nome :.*\n-.*\n.*', re.IGNORECASE)

struct_ = lambda x: [line.group() for line in re.finditer(re_struct, x)]
struct_name = lambda x: [line.group() for line in re.finditer(re_name, x)]
struct_size =lambda x: [line.group() for line in re.finditer(re_size, x)]

try:
    while True:
        produto_: list[str]
        segmento: list[str, int]
        menu_: str
        # Cadastro Produtos e quantidades, Segmentos e Variedades:
        menu_ = input('\n\t|*********************.\n'
                          '\t|>> SMOOTH STORAGE\t<<|'
                          '\n\t|*********************`\n'
                          '*************************************\n'
                          '[E]-    Iniciar Estoque :        \t|\n'
                          '\tVariedades , Cadastrar Produtos |\n'
                          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                          '[C]-\tConsultar Produtos : \t    |\n'
                          ' Consultar ou atualizar quantidade |\n'
                          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                          '[X]-\t\tFechar :  \t\t |\n'
                          '\t   Finalizar programa    |\n'
                          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                          '-----------------\nDigite uma opcão: '
                          ).lower()
        print('\n' * 100)

        # Condicão de saída da Ordem
        if menu_ == 'x':
            print('\n' * 100)
            break

        # Iniciando Cadastro de Produto
        while menu_ == 'e' or menu_ == 'p' or menu_ == 's':
            menu_ = input('\n************************.\n'
                          'INICIANDO ESTOQUE\t\t-|'
                          '\n************************`\n'
                          '********************************\n'
                          '[P]-\tCadastro Produto : \t    |\n'
                          '\tCadastre produto segmentado |\n'
                          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                          '[Q]-\t\tRetornar :  \t\t |\n'
                          '\tVoltar um para menu anterior |\n'
                          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                          '-----------------\nDigite uma opcão: '
                          ).lower()
            print('\n' * 100)
            if menu_ == 'p':
                os.chdir(category_storage)

                # Declarando Segmento e suas variedades
                segmento = [input('\n************************.\n'
                                 'CADASTRAMENTO DE PRODUTO |'
                                 '\n************************`\n'
                                 '-\t Categoria de Produto\n\t: ').lower(),
                            input('-\tVariedades: ')
                            ]
                # Salvando informacões de produto em um arquivo
                for _ in range(0, len(segmento[1])+1):
                    with open(f"produto_cadastro_{segmento[0]}.txt", "a+") as arq:
                        produto_ = [input('\n\nNome : '),
                                    input('Data de Validade : '),
                                    int(input('Quantidade : '))
                                    ]
                        # Persistência dos dados de produtos !
                        arq.write(f"{{\nProduct :{produto_[0]}\n{produto_[2]}\n{produto_[1]}}}")
                print('\n' * 100)
                os.chdir('..')
                os.chdir(category_list)
                with open('category_list.txt', "a+") as arq_list:
                    arq_list.write(f"{segmento[0]}\n")
                os.chdir('..')
            # Condicão de saída da ordem
            elif menu_ == 'q':
                print('\n' * 100)
                break
        # Ordem de Gerenciamento de Produtos
        while menu_ == 'c' or menu_ == 'l' or menu_ == 'a' or menu_ == 'b':
            menu_ = input('\n************************.\n'
                          'GERENCIANDO MERCADORIAS\t-|'
                          '\n************************`\n'
                          '***********************************\n'
                          '[A]-\tDados de Produtos : \t   |\n'
                          '\tConsultar Produto e seus dados |\n'
                          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                          '[B]-\tAtualizar Quantidade : \t  |\n'
                          '\tExtrair ou inserir quantidade |\n'
                          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' 
                          '[L]-\t   Listar Produtos :  \t|\n'
                          '  Exibindo produtos em estoque |\n'
                          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                          '[Q]-\t\tRetornar :  \t\t|\n'
                          '  Voltar um para menu anterior |\n'
                          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                          '-----------------\nDigite uma opcão: '
                          ).lower()
            print('\n' * 100)
            # Listando Nome de Produtos de Determinado Segmento
            if menu_ == 'l':
                print('\n**********************.\n'
                      'LISTA DE CATEGORIAS\t-|'
                      '\n**********************`\n')
                with open('product/cast/category_list.txt', "r+") as arq_list:
                    arq_list = arq_list.read()
                for position, line in enumerate(arq_list.split('\n')):

                    # Lista de Segmentos
                    print(f"Segmento : {line} Código : {position}")

                # Selecionando Segmento
                cantle = int(input('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                                   '------------------------------'
                                   '\nDigite Código do Segmento : '
                                   ))
                arq_list_cantle = arq_list.split('\n')
                os.chdir(category_storage)
                with open(f"produto_cadastro_{arq_list_cantle[cantle]}.txt", "r+") as arq_select:
                    arq_select = arq_select.read()

                # Retornando produtos de segmento selecionado
                print(arq_select.split('\n'))
            # Ordem de Consulta mais detalhada de produto
            elif menu_ == 'a':
                while True:
                    menu_consulta = input('\n*************\n'
                                          '\t\t%% Consultar Produto(s) %%\n'
                                          '[L]-\tLista Geral\n'
                                          '[A]-\tSelecionar Produto\n'
                                          '[Q]-\tRetornar\n: '
                                          ).lower()
                    print('\n' * 100)

                    # Listando Produtos com mais detalhes
                    if menu_consulta == 'l':
                        print('\n**********************.\n'
                              'LISTA DE CATEGORIAS\t-|'
                              '\n**********************`\n')
                        with open('product/cast/category_list.txt', "r+") as arq_list:
                            arq_list = arq_list.read()
                        for position, line in enumerate(arq_list.split('\n')):

                            # Lista de segmento
                            print(f"Segmento : {line} Código : {position}")

                        # Selecionando segmento
                        cantle = int(input('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                                           '------------------------------'
                                           '\nDigite Código do Segmento : '
                                           ))
                        arq_list_cantle = arq_list.split('\n')
                        os.chdir(category_storage)
                        with open(f"produto_cadastro_{arq_list_cantle[cantle]}.txt", "r+") as arq_select:
                            arq_select = arq_select.read()

                            # Tratamento se arquivo estiver vázio
                            if len(arq_select) == 0:
                                print('Error: Empty File')

                            # Retornando Produtos de segmento selecionado
                            else:
                                arq_name = '\n'.join(struct_name(arq_select))
                                print(arq_name.split())

                    elif menu_consulta == 'a':
                        with open('produto_cadastro_produto.txt', "r+") as arq_after:
                            arq_after = arq_after.read()
                            re_name = re.compile(r'-\t.*[a-z]\n', re.IGNORECASE)
                            struct_name = lambda x: [line.group() for line in re.finditer(re_name, x)]
                            arq_after = re.sub(r'-\t.?: ', '', arq_after)
                            arq_name = struct_name(arq_after)
                            print(arq_name)
                            arq_size = struct_size(arq_after)
                            arq_size = re.sub(r'[^0-9]', '',  '\n'.join(arq_size))
                            arq_obj = {arq_name[line]: arq_size[line] for line in range(0, len(arq_size))}
                            print(arq_obj)

                    # Condicão de saída da ordem
                    elif menu_consulta == 'q':
                        print('\n' * 100)
                        break
                    else:
                        print(f'Error %% Invalid Option {menu_consulta.upper()}')
                        print('\n' * 100)
            elif menu_ == 'b':
                (...)
            else:
                break
except Exception as err:
    print(f"Error %% {err}")
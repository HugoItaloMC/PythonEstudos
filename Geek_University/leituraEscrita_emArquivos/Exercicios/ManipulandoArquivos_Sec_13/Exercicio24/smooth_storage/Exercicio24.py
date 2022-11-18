"""
 Faca um programa simples de gerenciamento de estoque doméstico, o programa deve conter os seguintes requisitos
 - Cadastro de produtos e quantidades
 - Consulta de produtos 
 - Atualizar quantidade de produtos (update)
"""

import os
import json
import jsonpickle

class Produto():

    id_produto: int = 6999


    def __init__(self, nome: str, valor: float, qtd: int, data_validade: str, segmento_produto: str) -> None:
        self.__id: int = Produto.id_produto
        self.__nome: str = nome
        self.__quantidade: int = qtd
        self.__valor: float = valor
        self.__validade: str = data_validade
        self.__segmento: str = segmento_produto
        Produto.id_produto = self.__id + 1

    @property
    def nome_produto(self):
        return self.__nome

    @property
    def produto_quantidade(self):
        return self.__quantidade

    @property
    def data_validade_produto(self):
        return self.__validade

    @property
    def produto_id(self, id_):
        return self.id_produto

    @property
    def segmento_produto(self):
        return self.__segmento


    @property
    def valor_produto(self):
        return self.__valor

    def adicionar_quantidade(self, valor: int) -> None:
        if valor > 0:
            self.produto_quantidade += valor
        else:
            print('Somente Valores Positivos ! ## Error')

    def subtrair_quantidade(self, valor: int) -> None:
        if valor > 0:
            if self.produto_quantidade >= valor:
                self.produto_quantidade -= valor
            else:
                print('Produto Com Estoque Zerado')

    def alterar_nome(self, new_name: str):
        return (...)



if __name__ == '__main__':

    # Path da pasta de produtos (nome, quantidade, dataVal)
    category_storage: os = os.path.join(os.getcwd(), 'product/storage')

    # Path da pasta de segmentos do estoque
    category_list: os = os.path.join(os.getcwd(), 'product/cast')

    try:
        # Cadastrar Produto
        cadastro: object = Produto
        menu_: str
        while True:
            menu_ = input("SMOOTH-STORAGE\n*** Menu ***\n"
                          "[N]-\tCadastrar Novo Produto\n"
                          "[G]-\tConsultar Produto\n"
                          "[M]-\tGerenciar Estoque\n"
                          "[Q]-\tSair\n:").lower()

            if menu_ == 'n':
                print("\t\t *** >SMOOTH-STORAGE< ***\n Cadastro Produto")
                cadastro.nome_produto: str = input('...Nome Produto: ')
                cadastro.quantidade: int = int(input('Quantidade: '))
                cadastro.valor_produto: float = float(input('...Valor: '))
                cadastro.data_validade_produto: str = input('Data Validade: ')
                cadastro.segmento: str = input('...Segmento Produto: ')

                # Mudando de Diretório
                os.chdir(category_storage)

                cadastro_json = json.dumps({'Produtos':[
                    {'nome': cadastro.nome_produto,
                     'valor': cadastro.valor_produto,
                     'estoque': cadastro.quantidade * cadastro.valor_produto}
                ]})
                with open(f"{cadastro.segmento}_produtos.json", "x") as arq_json:
                    json_pickle = jsonpickle.encode(cadastro_json)
                    arq_json.write(json_pickle)

                os.chdir('..')

            elif menu_ == 'g':
                  menu_consulta = input("SMOOTH-STORAGE\n*** Menu-Consultas ***\n"
                          "[A]-\tListar Produtos\n"
                          "[B]-\tBuscar Produto por Nome\n"
                          "[Q]-\tSair\n:").lower()
                  if menu_consulta == 'a':
                      (...)
                  elif menu_consulta == 'b':
                      (...)
                  elif menu_consulta == 'q':
                      pass
                  else:
                      print('Opcão Inválida ## Error !!')

            else:
                break
    except Exception as err:
        print(err)
        print(type(err))
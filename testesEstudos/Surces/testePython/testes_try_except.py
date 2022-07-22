"""
 Ultilizando Python 3.10
 Testes bloco try except
 - Receber Entrada de usuário em um iterável
 - Tratar possíveis erros
 - Ultilizar funcões de módulos importados


# importando o módulo

from Sources.08-Funcoes_Python import funcoes_com_parametroPadrao as fcPp  # Módulos criados nos estudos
from fpdf import FPDF  # Módulo para trabalhar com arquivos PDF


try:
    quantidade_loop = int( input( "Digite Quantidade de loops: " ))  # Recebendo Entrada em um iterável
except (ValueError, NameError, ArithmeticError, TypeError) as err:  # Tratando erros Built-in's do Python
    print( f"ERRO : {err}" )  # Saída de Erro
else:  # Processamento da entrada
    cont = []
    for _ in range( 1, quantidade_loop ):  # Iterando sobre a entrada
        try:  #
            n = 0
            a = int( input( 'Digite Valor 1: ' ) )
            b = int( input( 'Digite Valor 1: ' ) )
            n += fcPp.soma( a, b )
        except (ValueError, NameError, ArithmeticError, TypeError) as err:  # Tratando erros Built-in's do Python
            print( f"ERRO : {err}" )  # Saída de Erro
        print( f'''resulado {n}''' ) if n != 0 else None
        cont.append( n )
finally:
    # Criando um arquivo PDF
    pdf = FPDF()  # Atrinbuindo a funcão FPDF a variável pdf
    pdf.add_page()  # Adicionando quantidade de paginas do arquivo PDF
    pdf.set_font( 'Arial', 'B', 16 )  # Formatando a fonte de escrita do arquivo
    pdf.cell( 40, 10, f'{cont}' )  # Digitando texto, formatando posicionamento
    pdf.output( 'tuto1.pdf', 'F' )  # criando arquivo, arquivo PDF será criado no diretório que se encontra o arquivo .
    cons = 1

"""


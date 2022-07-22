"""
"Este arquivo serve para testar minhas funcões fora dos seus pacotes definidos"


# Funcão para mostrar saída da entrada no console
def saida(n):
    cont = []

    def ensaida():
        nonlocal cont

        cont += n
        return ''.join(cont)
    return ensaida()

print(saida(input(" : ")))

# Funcão para a regra de fibonacci
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print(fib(1000))

# importando o módulo
from Sources.08-Funcoes_Python import funcoes_com_parametroPadrao as fcPp
from fpdf import FPDF

try:
    quantidade_loop = int( input( "Digite Quantidade de loops: " ) )
except (ValueError, NameError, ArithmeticError, TypeError) as err:  # Tratando erros Built-in's do Python
    print( f"ERRO : {err}" )  # Saída de Erro
else:
    cont = []
    for _ in range( 1, quantidade_loop ):
        try:
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



arquivo = open( 'arquivo2.txt', mode='w')
print('Texto Para teste', file=arquivo)
"""
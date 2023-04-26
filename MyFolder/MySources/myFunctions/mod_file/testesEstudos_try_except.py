"

# importando o módulos

from Sources.Funcoes_Python import funcoes_com_parametroPadrao as fcPp  # Módulos criados nos estudos
from fpdf import FPDF  # Módulo para trabalhar com arquivos PDF

# Inicio do bloco de tratamento:

try:
    quantidade_loop = int(input("Digite Quantidade de loops: "))  # Recebendo Entrada em um iterável
except (ValueError, NameError, ArithmeticError, TypeError) as err:  # Tratando erros Built-in's do Python
    print(f"ERRO : {err}")  # Saída de Erro
else:  # Processamento da entrada
    cont = []
    for n1 in range(1, quantidade_loop+1):  # Iterando sobre a entrada
        try:  # Nova execucão, Recebendo Entrada em variáveis locais
            n = 0
            a = int(input('Digite Valor 1: '))
            b = int(input('Digite Valor 1: '))
            n += fcPp.soma(a, b)  # Ultilizando funcão externa
        except (ValueError, NameError, ArithmeticError, TypeError) as err:  # Tratando erros Built-in's do Python
            print(f"ERRO : {err}")  # Saída de Erro
        else:  # Saídas
            print(f'''Loop {n1} ''')
            print(f'''resulado {n}''')
            cont.append(n)
finally:
    # Criando um arquivo PDF
    pdf = FPDF()  # Atrinbuindo a funcão FPDF a variável pdf
    pdf.add_page()  # Adicionando quantidade de paginas do arquivo PDF
    pdf.set_font('Arial', 'B', 16)  # Formatando a fonte de escrita do arquivo
    pdf.cell(40, 10, f'{cont}')  # Digitando texto, formatando posicionamento
    pdf.output('tuto1.pdf', 'F')  # criando arquivo, arquivo PDF será criado no diretório que se encontra o arquivo .
    cons = 1









# ******************************



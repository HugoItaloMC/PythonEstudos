'''
  Ulilizamos o gerenciador de pacotes para módulos externos do Python ' pip '
podemos encontrar todos os modulos externos oficiais em https://pypi.org

  fpdf -> No terminal digite : ' pip install fpdf  ' para instalacão do módulo externo,
fpdf é ultilizado para criacão, manipulacão de arquivos PDF's
link oficial : https://pyfpdf.github.io/fpdf2/index.html

  colorama -> No terminal digite : ' pip install colorama ' para instalacão do módulo externo,
colorama é ultilizado para colorir string's e background do console Python.

'''

# Ultilizando o fpdf :

from fpdf import FPDF  # importando o módulo

# Criando um arquivo PDF
pdf = FPDF()  # Atrinbuindo a funcão FPDF a variável pdf
pdf.add_page()  # Adicionando quantidade de paginas do arquivo PDF
pdf.set_font('Arial', 'B', 16)  # Formatando a fonte de escrita do arquivo
pdf.cell(40, 10, 'Hello World!')  # Digitando texto, formatando posicionamento
pdf.output('tuto1.pdf', 'F')  #  criando arquivo, arquivo PDF será criado no diretório que se encontra o arquivo .py


# ultilizando o colorama :

from colorama import init, Fore, Style, Back

init()  # iniciando o módulo

# Colorindo output's do console
# OBS !  As cores devem ser em caixa alta (BLACK, WHITE, RED, VIOLET, GREEN, etc...)
print(Fore.BLACK+ 'Manipulando Cor do Texto(black) do console Python')
print(Back.WHITE + 'Manipulando cor do fundo "background" (white) do console Python')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)  # A partir daqui reseta o output do console para a padrão do Python
print('Texto voltado ao padrão do console Python')
"""
Debugando com PDB

PDB -> Python Debugger
# DICA DE FORMAS DE DEBUGGAR UM CÓDIGO PYTHON

- 1. Ultilizar a ferramentaqs debugger da IDE (Pycharm).
- 2. Ultilizar o método PBD do Python, OBS 'A partir do Python 3.7 PBD se tornou um built-in.
breackpoint() é o método atual de ultilizar o PBD'.

"""
# Ultilizando breakpoint()


def operacao(n1, n2):  # funcão para dividir dois inteiros
    try:
        return int(n1) / int(n2)  # Convertendo valor de input em inteiros e retornando-os
    except (ValueError, NameError, ZeroDivisionError, TypeError) as err:  # Tratando erros Built-in's do Python
        return f"ERRO : {err}"  # Saída de Erro


# Entrada :
# breakpoint()
print("Resultado: ", operacao(input(f"operacão (divisão)\nDigite Valor: "), input("Digite Valor: ")))

# Ultilizando o import pbd de uma forma otimizada

nome = "Hugo"
#import pdb; pdb.set_trace()
'''
  COMANDOS BÁSICOS PDB :
  - l . Listar onde estamos no código
  - n . próxima linha
  - p . imprime variável  ( p ' nome da variável ')
  
  Ao invés de chamarmos o método no comeco do código como de costume, o importamos no bloco onde desejamos realizar
o debugger, tratar as excecões e apagar a linha do 'import' 
'''
sobreNome = "Italo Correia"
nomeCompleto = nome + ' ' + sobreNome
curso = "Python Profissional"
didatica = "Geek University"
final = nomeCompleto + ' Faz Curso ' + curso + didatica
print(final)

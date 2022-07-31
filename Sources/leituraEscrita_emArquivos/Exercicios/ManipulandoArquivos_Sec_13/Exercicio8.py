"""
  Faca um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo, mas com todas as letras
minúsculas convertidas para maiúscula, Os nomes dos arquivos serão fornecidos pelo usuário, via teclado.
  A funcão que converte para maiúscula as letras minúscula é o upper().

"""
while True:
    with open(f"{input('Digite nome do arquivo de entrada | 0 para sair : ')}", 'w+') as arquivo:  # Criando arquivo com o nome 'arq.txt' com o módulo 'w+' sobrescrita e updates
        while True:
            n = input('Digite dados ou 0 para sair : ')  # Entrada de dados
            if n != '0':  # Caso condicional
                arquivo.write(f"{n}\n")  # Escrevendo entradas de usuário no arquivo
            else:  # Caso de condicão de parada do arquivo
                pass
        with open(f"{input('Digite nome do arquivo de saída | 0 para sair : ')}"+'.txt', 'w+') as arq:
            

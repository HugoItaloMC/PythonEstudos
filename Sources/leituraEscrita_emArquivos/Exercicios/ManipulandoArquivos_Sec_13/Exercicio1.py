"""
  (a) - Crie um arquivo com o nome 'arq.txt'
  (b) - Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere
'0'
  (c) - Feche o arquivo

"""


with open('arq.txt', 'w+') as arquivo:  # Criando arquivo com o nome 'arq.txt' com o módulo 'w+' sobrescrita e updates
    while True:
        n = input('Digite 0 para sair : ')  # Entrada de dados
        if n != '0':  # Caso condicional
            arquivo.write(f"{n}\n")  # Escrevendo entradas de usuário no arquivo
        else:  # Caso de condicão de parada do arquivo
            break

# OBS !  ao ultilizarmos o bloco with o arquivo é fechado internamente fora do bloco

arquivo = open('arq.txt', 'r+')  # Abrindo arquivo para leitura e atualizacão
print(arquivo.read()[::1])
arquivo.seek(0)
print(len(arquivo.read()), 'Caracteres')

# OBS ! A quebra de linha '\n' também conta como caractere
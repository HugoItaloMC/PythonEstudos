"""
  Escrevendo em arquivos

  # OBS !  Ao abrirmos um arquivo para leitura ñ conseguimos escrever nele, e se o abrirmos para
escrita, ñ conseguimos ler o arquivo.
 # OBS !  Ao abrirmos um arquivo para escrita, se ele ñ existir um novo é criado

"""

with open('teste.txt', 'w') as arquivo:
    arquivo.write('Teste de escrita em arquivo\n Outro teste\t Write')
    while True:
        fruta = input('Digite uma fruta, ou Q para sair : ')
        if fruta != 'q' and fruta != 'Q':
            arquivo.write(f"{fruta}\n")
        else:
            break
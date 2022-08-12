"""
  Faca um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo, mas com todas as vogais
convertidas para maiúscula, Os nomes dos arquivos serão fornecidos pelo usuário, via teclado.
  A funcão que converte para maiúscula as letras minúscula é o upper().

"""

# Begin main

if __name__ == '__main__':
    try:
        with open(f"{input('Digite nome do arquivo de entrada com sua extensão : ')}", "r+") as arq:
            arq = arq.read()
            if not len(arq) == 0:
                vogais = 'aeiou'
                try:
                    with open(f"{input('Digite nome do aquivo de saída e sua extensão : ')}", "w+") as after:
                        for line in arq:
                            if line in vogais:
                                line.upper()
                                after.write(line.upper())
                            else:
                                after.write(line)
                except (FileNotFoundError, FileExistsError, TypeError, ValueError, OSError) as err:
                    print(f"Error ## {err}")
            else:
                print(f"Erro ## Arquivo Vazio ##")
    except (FileNotFoundError, FileExistsError, TypeError, ValueError, OSError) as err:
        print(f"Error ## {err}")

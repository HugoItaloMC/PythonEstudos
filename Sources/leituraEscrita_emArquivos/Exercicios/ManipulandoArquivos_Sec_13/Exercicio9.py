"""
  Faca um programa que receba do usuário dois arquivos, e crie um terceiro arquivo com o conteúdo dos dois arquivos
(o conteúdo do primeiro seguido do conteúdo do segundo)

"""

if __name__ == '__main__':
    try:
        with open(f"{input('Digite nome do primeiro arquivo com sua extensão : ')}", "r+") as arq:
            arq = arq.read()
            if not len(arq) == 0:
                try:
                    with open(f"{input('Digite nome do segundo arquivo e sua extensão : ')}", 'r+') as arq2:
                        arq2 = arq2.read()
                        try:
                            with open(f"{input('Digite nome do arquivo de saída e sua extensão : ')}", "w+") as after:
                                for line in arq:
                                    after.write(line)
                                for line in arq2:
                                    after.write(line)
                        except (TypeError, ValueError, FileExistsError, FileNotFoundError, OSError) as err:
                            print(f"Erro ## {err}")
                except (TypeError, ValueError, FileExistsError, FileNotFoundError, OSError) as err:
                    print(f"Erro ## {err}")
            else:
                print(f"Erro ## Arquivo vazio ##")
    except (TypeError, FileExistsError, FileNotFoundError, OSError) as err:
        print(f"Erro ## {err}")

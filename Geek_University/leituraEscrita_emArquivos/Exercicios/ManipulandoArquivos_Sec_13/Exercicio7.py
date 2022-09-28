"""
  Faca um programa que recebe do usuario um arquivo, crie outro arquivo contendo as informacões do primeiro arquivo,
só que o usuário deve escolher qual caractere vai alterar e por qual caractere vai ser substituido:

"""
# from testesEstudos.myFunctions import changeFunction as chFun


# Begin Main:

if __name__ == '__main__':
    # Refature :

    # Put entry file
    try:
        with open(f"{input('Digite nome do arquivo de entrada com sua extensão : ')}", "r+") as arq:
            # read file data
            arq = arq.read()
            if not len(arq) == 0:

                put = input("Digite Busca da Ocorrência : ")  # Search data in entry file
                change = input("Digite substituicão da ocorrência : ")  # Put data in exit file
                try:
                    # Creat exit file
                    with open(f"{input('Digite Nome do arquivo de saída com sua extensão : ')}", "w+") as after:
                        # Begin engine in file
                        for line in arq:
                            after.write(line.replace(put, change))
                except (TypeError, ValueError, FileExistsError, FileNotFoundError) as err:
                    print(f"Erro ## {err}")
            else:
                print("Erro ## Arquivo Vazio ##")
    except (TypeError, ValueError, FileExistsError, FileNotFoundError) as err:
        print(f"Erro ## {err}")
        

"""
# Begin Entry :


### : Previous Engine ### 

arq = open('arq.txt', 'r+')  # Put entry file
arq = arq.read()  # read file data


after = open('arq2.txt', 'w+')  # create exit file
put = input('Digite ocorrência : ')  # search data in file
change = input('Digite substituicão da ocorrência : ')  # Put data in exit file

# End Entry
"""
# End Processamento

"""
 Faca um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém cada
linha do nome de uma cidade e o seu número de habitantes (ocupando 40 caracteres). O programa devera ler o arquivo
gerar o arquivo de saída o onde aparece o nome da cidade mais populosa.

"""
arq = open("cidadesNomes.txt")
arq = arq.read()
arq2 = open("cidadesPopulacao.txt")
arq2 = arq2.read()

cidadesNomes = [line for line in arq]
cidadesNomes = list(filter(lambda size: len(size) > 0, cidadesNomes))
cidadesNomes = ''.join(cidadesNomes)
print(cidadesNomes)

cidadesPopulacao = [line for line in arq2.split()]
cidadesPopulacao = list(filter(lambda size: len(size) > 0, cidadesPopulacao))
#  cidadesPopulacao = ' '.join(cidadesPopulacao)


c = {cidadesNomes.split('\n')[d]: cidadesPopulacao[d] for d in range(0, len(cidadesPopulacao))}


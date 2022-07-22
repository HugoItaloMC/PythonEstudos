"""
 - Definindo funcões :
    - funcões são pequenos trechos de código que realizam tarefas especificas;
    - Já ultilizamo várias funcões sendo elas:
        - print()
        - max()
        - min()
        - sum()
        - count()
        - entre outras;
    - Pode ou não receber uma entrada de dados e retornar uma saída de dados;
    - Muito uteis para executar procedimentos similares repetidas vezes;

 - OBS : Se vc escrever uma funcão que realiza varias tarefas dentro dela,
é bom fazer uma verificacão para que a funcão seja simplificada.
 - Na programacão vc vai ouvir muito um termo tecnico chamado 'DRY' :
Don't repeat yourself : Não repita seu código/vc mesmo

# Exemplo de ultilizacão de funcões:

cores = ['azul', 'amarelo', 'verde', 'branco']
curso = 'Programacão em Python: Essensial'

    # Ultilizando a funcão integrada(built-in) do Python :
        # Exemplos :

print(f"{cores}\n{curso}")  # -- funcão  print()
cores.append('roxo')        # -- funcão .append()
# curso.append('outro curso') AttributeError 'str' object has no attribute 'append'
print(f"\n{cores}\n{curso}")

 - Em Python, a forma geral de definir uma funcão é desta forma:

def nome_da_funcao(parametro_entrada):
    bloco_da_funcao

 - nome_da_funcao : SEMPRE, com letras minúsculas, e se for nome composto, separar por underline (Snake Case);
 - parametro_entrada : Opicionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opicionais ou não;
 - bloco_da_funcao : Também chamado de corpo da funcão ou implementacão é onde o processamento da funcão acontece neste 
bloco pode ter ou não retorno da funcão. 

 - OBS :  Veja que para definirmos uma funcão, ultilizamos
 uma palavra reservada 'def' informando ao Python que estamos definindo
uma funcão e também abrimos o bloco com ' :  ' que é ultilizado para definir blocos.
"""

# Definindo funcão :


def diz_oi():
    print('oi')


"""
OBS : 
 - Veja que dentro de uma funcão podemos ultilizar outras funcões; 
 - Essa funcão só executa 1 tarefa:  'print a palvra oi ' ;
 - A funcão não recebe nem um parametro de entrada;
 - A funcão não retorna nada;
"""
# Ultilizando a funcão:
# Chamada de funcão

diz_oi()

# Definindo funcão:


def cantar_parabens():
    print(f"Parabéns pra voce\n nesta data querida\n muitas felicidades",
    f"\n muitos anos de vida.\n Felicidades ao aniversáriante !!!\n")

# Ultilizando funcão :
# chamada de funcão :

for n in range(5):
    print(n)
    cantar_parabens()

# Em python, podemos criar uma variável do tipo funcão e executar a funcão dentro da variável declarada


cantar = cantar_parabens
cantar()
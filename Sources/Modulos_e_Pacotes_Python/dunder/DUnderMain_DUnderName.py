"""
  Em Python é ultilizado Double Under para se criar funcões, atributos, propriedades e etc ultilizando
Double Under para não gerar conflitos com os nomes desses elementos na programacão.

# Na linguagem C, temos um programa da seguinte forma
int main(){

    return 0;
)

# Na linguagem Java, temos um programa da seguinte forma:

public Static Void main (String[] args){
}


# Em Python se DIRETAMENTE executarmos um módulo na linha de comando, internamente o Python
atribuirá a variável __name__ o valor __main__ indicando que este é o módulo de execucão principal
"""

#  Importando módulo de testes

import funcoes_paraTestes as Fpt

"""
 Todo módulo em execucão principal passa a ser o '__main__' "principal", quando declaramos que 
a variável __name__, que é um built'in do Python, passa a ser igual a '__main__', ou seja, se tornando 
módulo principal "em execucão":  execute o código descrito dentro do bloco;
  Assim no caso de uma importacão de módulo não haverá conflito nas execucões das funcões importadas de um 
módulo externo. Lembrando que módulos nada mais é do que códigos/arquivos '.py' .
"""
if __name__ == '__main__':
    print(Fpt.somaImpar((n for n in range(100))))

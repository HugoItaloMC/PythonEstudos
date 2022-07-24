"""
Repositório Remoto : github.com/HugoItaloMC/PythonEstudos/Comprehensions


Python, versão :  3.10

 Base :
    Curso : Programacão Python Essensial. Didática : Geek University. Plataforma :  udemy.com


Secão 9 ; Comprehensions em Python :

    Set's Comprehensions :

    # exemplos
     :
        numeros = {n for n in range(1, 11)}
        print(numeros)

        numeros = {n ** 2 for n in range(1, 11)}
        print(numeros)

        letras = {letra for letra in 'Teste de Set'}
        print(letras)


.==============================================.
|     " " " " " " " " " " " " " " " " " "      |
|     "  Ordem alfabetica nas variáveis "      |
|     "      globais e locais :         "      |
|     "                                 "      |
|     "       Examples Global :         "      |
|     "                                 "      |
|     "            a = ''               "      |
|     "             b = 0               "      |
|     "             c = True            "      |
|     "                                 "      |
|     "                                 "      |
|     "       Examples Local :          "      |
|     "                                 "      |
|     "        a = range(0, 10)         "      |
|     "                                 "      |
|     "        for b, c in a:           "      |
|     "            for d, in b:         "      |
|     "                print(d)         "      |
|     "            for e in c:          "      |
|     "                print(e)         "      |
|     "                                 "      |
|     "                                 "      |
|     "    Ordem válida para funcões    "      |
|     "      e seus parametros :        "      |
|     "                                 "      |
|     "          Examples:              "      |
|     "                                 "      |
|     "       def d(da, db):            "      |
|     "       return (da + db) * da     "      |
|     " " " " " " " " " " " " " " " " " "      |
.==============================================.

"""
letras = {letra for letra in 'Teste de Set'}
print(letras)
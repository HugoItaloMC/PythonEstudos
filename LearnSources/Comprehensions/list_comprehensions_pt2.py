"""
Repositório Remoto : github.com/HugoItaloMC/PythonEstudos/Sources/Comprehensions


Python, versão :  3.10

 Base :
    Curso : Programacão Python Essensial. Didática : Geek University. Plataforma :  udemy.com


Secão 9 ; Comprehensions em Python :

    List Comprehensions pt2
       - Ultilizando list comprehension podemos gerar novas listas com dados processados a partir de outro
iterável

    # Sintax da list comprehension :

        [dado for dado in iterável]


# Ultilizando list comprehensions como estrutura condicionais

# Exemplos :

# 1

a = list(range(1, 51))

b = [n for n in a if n % 2 == 0]  # Retorna números pares
c = [n for n in a if n % 2 != 0]  # Retorna números impares

print(f"{b}", f"\n{c}")


# Refatorando :
# 1

b = [n for n in a if not n % 2]  # Retorna números pares
c = [n for n in a if n % 2]  # Retorna números impares

print(f"{b}", f"\n{c}")

# 2

b = [n * 2 if n % 2 == 0 else n / 2 for n in a ]  # Retorna números pares e divide os ímpares por 2

print(f"{b}")

"""

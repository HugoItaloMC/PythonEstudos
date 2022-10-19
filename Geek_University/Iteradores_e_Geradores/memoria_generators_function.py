"""
 Teste de memória de generators

"""
# Utilizando lista (Consumo 480MB)
def fib_lista(max):
    """Funcão sequência de fibonacci:"""
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

# Utilizando genaretors (CONSUMO 8,5 MB)
def fib_gen(max):
    a, b, cont = 0, 1, 0
    while cont < max:
        a, b = b, a + b
        yield a
        cont += 1


# Teste
for n in fib_gen(100000):
    print(n)

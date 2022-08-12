"""
Módulo Collections: Deque

Podemos dizer que o módulo Deque é uma lista de alta perfomance.
"""
# import

from collections import deque

# Criando deques:
deq = deque('Teste estudo')
print(deq)
# Adicionando elementos no deque
deq.append('y') # Adiciona no final
print(deq)

deq.appendleft('k') # Adiciona no comeco
print(deq)

# Removendo elementos
print(deq.pop()) # Remove e retorna ultimo elemento
print(deq.popleft()) # Remove e retorna o primeiro elemento

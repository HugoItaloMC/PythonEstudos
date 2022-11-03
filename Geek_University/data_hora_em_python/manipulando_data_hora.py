"""
  Manipulando Data e Hora com Python

  : Python tem um módulo built`in (embutido) para se trabalhar com datas e horas
chamado datetime

"""

import datetime

print(help(datetime))

# REtornando hora recorrente

data_atual = datetime.datetime.now()
print(data_atual)

# convertendo entrdaa de usuário em um tipo de data

data_recebida = '15/09/1999'

foo_data = data_recebida.split('/')
foo_data = datetime.datetime(int(foo_data[2]), int(foo_data[1]), int(foo_data[0]))

print(foo_data)
print(type(foo_data))

# Acesso individual a elementos

print(data_atual.year)
print(data_atual.month)
print(data_atual.day)
print(data_atual.hour)
print(data_atual.minute)
print(data_atual.microsecond)

# Verificando representacao da módulo
# (year, month, hour, minute, second, microsecond=)
print(repr(data_atual))

# Alterando horário utilizando replace()
data_atual = data_atual.replace(hour=16, minute=30, second=0, microsecond=0)
print(data_atual)

# Criando data

evento = datetime.datetime(2023, 1, 1, 0)
print(evento)
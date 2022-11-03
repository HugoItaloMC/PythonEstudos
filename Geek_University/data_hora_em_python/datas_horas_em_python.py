"""
  - Métodos de datas e horas utilizando Python

"""

import datetime
from textblob import TextBlob
import timeit, functools
date_now = datetime.datetime.now()

print(date_now)
print(type(date_now))
print(repr(date_now))

date_today = datetime.datetime.today()

print(date_today)
print(type(date_today))
print(repr(date_today))

# A diferenca entre o today() e o now() é que no now() podemos declarar uma timezone (Fuso Horário)

# Mudancas para ocorrer em a meia noite 00:00 h

data_work = datetime.datetime.combine((date_now + datetime.timedelta(days=1)), datetime.time())
print(data_work)

# Verificando o dia da semana do evento
print(data_work.weekday())

# 0 - Segunda-Feira (monday)
# 1 - Terca-feira (tuesday)
# 2 - Quarta-feira (wednesday)
# 3 - Quinta-feira (thrusday)
# 4 - Sexta-feira (friday)
# 5 - Sabádo (saturday)
# 6 - Domingo (sunday)


if data_work.weekday() == 0:
    print('Vc Nasceu na Segunda Feira')
elif data_work.weekday() == 1:
    print('Vc Nasceu na Terca Feira')
elif data_work.weekday() == 2:
    print('Vc Nasceu na Quarta Feira')
elif data_work.weekday() == 3:
    print('Vc Nasceu na Quinta Feira')
elif data_work.weekday() == 4:
    print('Vc Nasceu na Sexta Feira')
elif data_work.weekday() == 5:
    print('Vc Nasceu na Sábado')
elif data_work.weekday() == 6:
    print('Vc Nasceu na Domingo')

# formatando datas/horas com strftime() (string format time)

data_hoje = datetime.datetime.today()

print(data_hoje)

data_hoje = data_hoje.strftime('%d/%m/%Y')
print(data_hoje)

# Implementando uma funcão utilizando data

def formata_data(data):
    if data.month == 1:
        return f"{data.day} de Janeiro de {data.year}"
    elif data.month == 2:
        return f"{data.day} de Fevereiero de {data.year}"
    elif data.month == 3:
        return f"{data.day} de Marco de {data.year}"
    elif data.month == 4:
        return f"{data.day} de Abril de {data.year}"
    elif data.month == 5:
        return f"{data.day} de Maio de {data.year}"
    elif data.month == 6:
        return f"{data.day} de Junho de {data.year}"
    elif data.month == 7:
        return f"{data.day} de Julho de {data.year}"
    elif data.month == 8:
        return f"{data.day} de Agosto de {data.year}"
    elif data.month == 9:
        return f"{data.day} de Setembro de {data.year}"
    elif data.month == 10:
        return f"{data.day} de Outubro de {data.year}"
    elif data.month == 11:
        return f"{data.day} de Novembro de {data.year}"
    elif data.month == 12:
        return f"{data.day} de Dezembro de {data.year}"
    else:
       raise "Not Valid Type, To type Just like date"

print(formata_data(date_now))


# Método ñ recomendado, Módulo está para ser descontinuado em proximas releases do Python
#def formata_data_shot(data):
 #   return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

#print(formata_data_shot(date_now))

# Conhecendo o strptime()

nascimento = datetime.datetime.strptime('16/07/1993', '%d/%m/%Y')
print(nascimento)

# Somente Hora

almoco = datetime.time(12, 30, 0)
print(almoco)

# Utilizando timeit para marcar tempo de execucão do código

# loop for
tempo_generator = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo_generator)

# List Comprehensions
tempo_comprehensions = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo_comprehensions)

# Utilizando map
tempo_map = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo_map)

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=10000))
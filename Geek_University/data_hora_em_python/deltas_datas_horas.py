"""
 - Trabalhando com Deltas de Datas e horas
  - Quando falamos de Delta de data e hora, estamos nos referindo a diferenca entre dois números, um exemplos
entre 3 e 10 o delta é 7.

"""

import datetime

data_now = datetime.datetime.now()

# Declarando date e um evento
aniversario = datetime.datetime(2023, 10, 2, 0)

# Calculando o Delta
delta_bday = aniversario - data_now
print(f"Faltam {delta_bday.days} dias\n{delta_bday.seconds // 60 // 60} Hora(s)\n...Para o evento")

# Aplicando deltas como regras

regra_pay = datetime.timedelta(days=3)

vencimento_boleto = data_now + regra_pay

print(vencimento_boleto)

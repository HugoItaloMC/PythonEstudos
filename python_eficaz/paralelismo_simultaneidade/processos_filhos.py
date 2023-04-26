"""
 Use subprocess para gerenciar processos filhos

   - Use o modulo nativo subprocess para executar processos-folho e gerenciar
seus fluxos de entrada e saida
   - Os processos-filho rodam em paralelo com o interpretador do Python, pos-
sibilitando maximizar o uso de CPU
  - Use  o  parametro  `timeout`  com  o  metodo  `communicate()` para evitar
deadlocks e processos-filhos travados ("zumbis")

"""

import subprocess
from time import time

# Popen e o construtor que inicia o processo
# O metodo communicate() le a saida do processo filho e espera que ele termine
proc = subprocess.Popen(
    ['echo', 'Hello from the child'],
    stdout=subprocess.PIPE)  # Inicia o processo

out, err = proc.communicate()  # Le a saida do processo filho e espera que ele termine
print(out.decode('utf-8'))

# Os processos filhos rodam de forma independente de seu processo-pai, que e o proprio interpretador do Python
# Seu estado pode ser consultado periodicamente enquanto o Python esta ocupado com outras tarefas.
proc = subprocess.Popen(['sleep', '0.1'])

while proc.poll() is None:
    print("Working ...")

print('Exit Status', proc.poll())

# Desacoplar o processo-filho de seu pai faz com que o processo=pai fique livre para iniciar e manter outros
# processos-filhos em paralelo
# Isso pode ser feito iniciando todos os processos-filho desce o comeco


def run_sleep(period):
    proc = subprocess.Popen(
        ['sleep', str(period)]
    )
    return proc


start = time()
procs: list = list()
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

# Apos todos os processos serem executados verificar saida
for prc in procs:
    proc.communicate()
end = time()
print("Finish in %.3f " % (end - start))

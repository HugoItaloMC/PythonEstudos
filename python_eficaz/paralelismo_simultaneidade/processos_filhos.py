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
import shlex
import os
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

# Desviar dados do programa utilizando PIPES
# criptografar informacoes utilizando processos-filho
# Levando e consideracao que `data`  representa os dados de qualquer fonte
# (SOCKET, DB, INPUT_USER, SendFiles)

COMMAND_SSL = shlex.split(shlex.join(
    ['openssl', 'enc', '-pbkdf2', '-pass', 'env:password']))
COMMAND_SH = shlex.join(shlex.split('netstat -a'))


def first_pipe(data):
    # Utilizaremos uma ferramenta externa de linhas de comandos
    # Criptograficaremos os dados utilizando openssl
    env = os.environ.copy()
    env['password'] = '%s' % os.urandom(15)
    proc = subprocess.Popen(
        COMMAND_SSL,
        env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()  # Garante que o processo receba algum dado na entrada
    proc.stdin.close()
    yield proc


def after_pipe(args):
    with open('info.txt', 'wb') as filerr:
        proc = subprocess.Popen(COMMAND_SH, stdin=args,
                                stdout=subprocess.PIPE, shell=True)
        for line in iter(proc.stdout.readline, b''):
            filerr.write(line)
            yield line
if __name__ == '__main__':
    output_procs = list()
    start = time()
    for _ in range(3):
        data = os.urandom(10)
        procs = first_pipe(data)
        for proc in procs:
            output_procs.append(after_pipe(proc.stdout))

    for lines in output_procs:
        for line in lines:
            print(line.decode('utf-8'))

    # Aguardar processos serem finalizados
    end = time()
    print("Finished in %.3f" % (end - start))
    # max: Finished in 0.800 seg`s | min: Finished in 0.480 seg`s

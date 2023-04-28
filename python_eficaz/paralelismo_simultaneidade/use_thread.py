# Use threads para bloquear I/O e evitar paralelismo

#  As threads do Python nao conseguem rodar bytecode em paralelo nos sistemas
# com mais de um nucleo no CPU por conta da `global interpreter lock (GIL)`

#  Mesmo com a GIL, as threads do Python sao bastantes uteis porque oferecem uma maneira
# bem mais facil de executar multiplas tarefas ao mesmo tempo

#  Use as threads do Python para fazer multiplas chamadas de sistema em paralelo.
# Com isso, podemos disparar operacoes que bloqueiam I/O ao mesmo tempo em que
# o programa principal continua computando outras coisas

from threading import Thread
import select
from time import time


def slow_syscall():
    select.select([], [], [], 0.1)


if __name__ == '__main__':
    start = time()
    threads = list()

    for _ in range(5):
        thread = Thread(target=slow_syscall)
        thread.start()
        threads.append(thread)

    def send_func(send):
        ...

    for line in range(5):
        send_func(line)

    for thread in threads:
        thread.join()

    end = time()
    print('Finished in %3.f' % (end - start))



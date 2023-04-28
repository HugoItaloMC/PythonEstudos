# Use Lock para evitar que as threads iniciem condicoes de corrida nos dados

#  MEsmo que o interpretador do Python tenha uma trava global, ainda e responsabilidade do programador
# proteger seu codigo contra condicoes de corrida nos dados provocados pelas threads do programa

#  Os programas corromperao suas proprias estruturas de dados se for permitido que mais de uma
# thread modique o mesmo objeto sem que haja trava de protecao

#  A classe Lock do modulo nativo threadning e a implementacao padrao
# de travas de exclucao mutua (mutex) no Python

from threading import Thread, Lock
class Counter:
    def __init__(self):
        self.lock = Lock()
        self.count = int()

    def set_count(self, offset):
        with self.lock:
            self.count += offset


def worker(w_index, opp, counter):
    for _ in range(opp):
        # ...
        counter.set_count(1)


def main_thread(func, opp, counter):
    threads = list()
    for line in range(3):
        args = (line, opp, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    opp = 5 ** 10
    counter = Counter()
    main_thread(worker, opp, counter)
    print('Counter should be %d, found %d' % (3 * opp, counter.count))

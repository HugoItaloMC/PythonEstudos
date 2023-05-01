"""
 - Use o polimorfismo de @classmethod para construir objetos genericamente

 >> O Python suporta apenas um construtor por classe, o metodo __init__
 >> Use @classmethos para definir construturoes alternativos para suas classes
 >> Use polimorfismo de método de classe para implementar uma maneira genérica de construir e
   conectar subclasses concretas

"""
# Vamos implementar um programa de map reduce de arquivos em uma pasta
# Gerar nossas classes genericas com @classmethod

import os
from threading import Thread

class InputData(object):
    # Classe comum para representar dados de entrada (path dos arquivos)

    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config: dict):
        # tornando nossa classe generica, para que futuramente ao se criar novas subclasses de InputData nao modifique
        # O programa principal, que conecta todos objetos e seus metodos
        raise NotImplementedError


class PathInputData(InputData):
    # Classe concreta de InputData

    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config: dict):
        # Attr : config :: Dicionario contendo path de arquivos a serem mapedos
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class Worker(object):
    # Classe comum para recebimento e tratamento de dados

    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class: object, config: dict):
        # Attr : config :: dicionario que contem path do arquivo a ser mapeado
        # Attr : input_class :: Objeto contendo metodo de entrada de dados (PathInputData
        worker = []
        for input_data in input_class.generate_inputs(config):
            worker.append(cls(input_data))
        return worker


class LineCountWorker(Worker):
    # Classe concreta de Worker

    def __init__(self):
        super(__class__, self).__init__()

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def server(workes):
    threads = [Thread(target=w.map) for w in workes]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workes[0], workes[1:]

    for worker in rest:
        first.reduce(worker)
    return first.result


if __name__ == '__main__':
    def mapreduce(worker_class: object, input_class: object, config: dict):
        workers = worker_class.create_workers(input_class, config)
        return server(workers)

    config = {'data_dir': os.listdir(os.getcwd())}
    print(config)
    def main():
        mapreduce(LineCountWorker, PathInputData, config)

    main()

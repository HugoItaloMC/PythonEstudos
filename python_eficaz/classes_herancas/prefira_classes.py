"""
 Prefira classes auxiliares ao inves de dicionarios e tuplas para administrar
registros complexos.
  - Evite Criar dicionarios com valores que sejan outros dicionarios
  - Use namestuple para criar containers de dados leves e imutaveis antes de precisar da fexibilidade
de uma classe completa
  - Migre seu codigo de registro para uma hierrarquia de classes auxiliares quando seus dicionarios in-
ternos de estados comecaram a ficar muito complicados
"""

from collections import namedtuple
Grade = namedtuple('Grade', ('pontos', 'peso'))
# WARINIG : Namedtuple nao se pode definir valores default e qualquer um pode acessar os dados por indices e iteradores


class Diciplina:

    # Representando Diciplina com conjunto de notas
    def __init__(self):
        self._notas = list()

    def reportar_materia(self, pontos, peso):
        self._notas.append(Grade(pontos, peso)
                            )

    def avaliar_nota(self):
        total, total_peso = 0, 0
        for grade in self._notas:
            total += grade.pontos * grade.peso
            total_peso += grade.peso
        return total / total_peso

class Estudante:

    # Representando diciplinas cursadas pelo aluno

    def __init__(self):
        self._diciplina = dict()

    def diciplina(self, name: str):
        if name not in self._diciplina:
            self._diciplina[name] = Diciplina()
        return self._diciplina[name]

    def avaliar_nota(self):
        total, count = 0, 0
        for diciplina in self._diciplina.values():
            total += diciplina.avaliar_nota()
            count += 1
        return total / count


class Gradebook:
    # Conteiner para todos os estudantes dinamicamente escolhidos por seus nomes

    def __init__(self):
        self._estudante = dict()

    def estudante(self, name: str):
        if name not in self._estudante:
            self._estudante[name] = Estudante()
        return self._estudante[name]


if __name__ == '__main__':
    boletim = Gradebook()
    luce = boletim.estudante('Luce Martin')
    geografia = luce.diciplina('Geografia')
    geografia.reportar_materia(80, 0.10)

    print(luce.avaliar_nota())
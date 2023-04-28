import subprocess
import shlex
import argparse

# Gerar dados


def sdt_in() -> None:
    begin = 
    EXIT = ['sair', 'exit', 'quit', 'finalizar', 'close'] # CONDICAO DE SAIDA
    while (op := input("Write in: ")) not in EXIT:
        with open("log.txt", 'wb+') as arq:
            arq.write(op.encode())

    def std_out():
        with open("log.txt", 'r') as marq:
            if marq:
                data = "".join([line for line in marq.read()])
                return print(data)
    return std_out()

sdt_in()
# Sub-processos de dados ( Ler os dados, gerar arquivo de saida) utilizando sub-processos

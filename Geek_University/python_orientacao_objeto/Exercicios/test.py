# Test Exercicio02 POO:

from Geek_University.python_orientacao_objeto.Exercicios.exercicio02_poo import Pessoa

class CadastroPessoa(Pessoa):
    pass

def cadastro() -> object:
       user: object = CadastroPessoa
       user.nome: str = input("...Enter Your Name : ")
       user.phone: str = input("...Enter Your Phone : ")
       user.email: str = input("...Enter Your email: ")
       return user.__dict__

if __name__ == '__main__':
        try:
            cadastro()
        except Exception as err:
            print(f"Error #{err}")

"""




class Calculadora:

    def __init__(self, num1: int, num2: int):
        self.n1: int = num1
        self.n2: int = num2


        if isinstance(self.n2 and self.n1, bytes or str):
            self.num1 = int(self.n1)
            self.num1 = int(self.n2)
    def operacao(self):
        raise NotImplementedError


class Soma(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    def operacao(self):
        return self.n1 + self.n2


class Subtracao(Calculadora):

    def __init__(self, n1, n2):
        super().__init__(n1, n2)


    def operacao(self):
        return self.n1 - self.n2

"""
if __name__ == '__main__':

    from chatgpt_mod import gerar_texto, CHAT_WRITES_READ
    from fpdf import FPDF
    try:
         while (prompt := input(':: You  = ')) != 'sair':
             CHAT_WRITES_READ.append(gerar_texto(prompt=prompt))
    except Exception as err:
        print(f"{err} <<< Error")
    else:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(100, 200, txt=f"YOU::  {prompt}")
        pdf.cell(100, 200, f"{CHAT_WRITES_READ.pop()}")
        pdf.output('tudo.pdf', 'F')

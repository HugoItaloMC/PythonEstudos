"""
  Faca um programa que receba um arquivo contendo o nome e precos de diversos produtos
e some o valor da compra!
"""
import re
continue_: str
try:
    with open("compra_carrinho.txt", "w+") as arq:
        continue_ = input('Gostaria de adicionar mais algum item? (y/n) : ').lower()
        while continue_ != 'n':
            if len(arq.read()) == 0:
                compra_: list[str, float]
                compra_ = [input('Digite Item: '),
                           float(input('** PRECO -> $$ : '))
                           ]
                arq.write(f"Item {compra_[0]} Preco {compra_[1]} $$\n")
                f'{continue_}'
            else:
                print("Arquivo ñ está vazio ## -")
except Exception as err:
    print(f"Error %% {type(err)}")
else:
    reg_putAlf = re.compile(r'[0-9\n]?')
    with open('compra_carrinho.txt', "r+") as arq_after:
        arq_after = arq_after.read()
        arq_after_selles = ''.join([line.group() for line in re.finditer(reg_putAlf, arq_after) if line != ''])
        with open('valor_compra.txt', "w+") as arq_total:
            arq_total.write(f"{arq_after}{sum(list(map(float, arq_after_selles.split())))} valor total da compra")

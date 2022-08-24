"""
 Faca um programa que receba um arquivo contendo nome e data de nascimento, e retorne um arquivo
de saída contendo a data de hoje e o nome de cada pessoa com sua idade e data de nascimento

"""

if __name__ == '__main__':
    #from MyFolder.MySources.myFunctions import regexFunction as rgFun
    import re
    with open("nomes.txt", "r+") as arq:
        arq = arq.read()
        date_pattern = re.compile(r"(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/([0-9]{4})")  # DATA NASCIMENTOs
        data_pattern = re.compile(r"([0-9]{9})-([0-9]{2})*")  # CPF
        #arq_date = re.finditer(date_pattern, arq)
        arq_data = re.finditer(data_pattern, arq)
        #arq_date = arq_date.group()
        #for line in list(arq_date):
         #   print(line.group())
        for line in list(arq_data):
            print(line.group())
        arq_date_after = [line.group() for line in re.finditer(date_pattern, arq)]
        print(arq_date_after)
import re

re_name = re.compile(r'Nome :.*[a-z]', re.IGNORECASE)
re_size = re.compile(r'Quantidade.*[0-9]', re.IGNORECASE)
re_struct = re.compile(r'Nome :.*\n-.*\n.*', re.IGNORECASE)
struct_ = lambda x: [line.group() for line in re.finditer(re_struct, x)]
struct_name = lambda x: [line.group() for line in re.finditer(re_name, x)]
struct_size = lambda x: [line.group() for line in re.finditer(re_size, x)]

with open('produto_cadastro_produto.txt', "r+") as arq:
    arq_struct = struct_(arq.read())
    print(re.sub(r'', '', arq_struct))

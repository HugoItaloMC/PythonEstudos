import re

re_name = re.compile(r'[a-z ,]', re.IGNORECASE)
re_size = re.compile(r'\([0-9]\),', re.IGNORECASE)
re_date = re.compile(r'(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/([0-9]{4})|,', re.IGNORECASE)
struct_date = lambda x: [line.group() for line in re.finditer(re_date, x)]
struct_name = lambda x: [line.group() for line in re.finditer(re_name, x)]
struct_size = lambda x: [line.group() for line in re.finditer(re_size, x)]

with open('produto_cadastro_produto.txt', "r+") as arq:
    arq_after = struct_size(arq.read())
    arq_after_later = [line for line in ''.join(arq_after).split(',') if not line == '']
print(arq_after_later)


"""
import re  
    
def putSpace(input):  
    
    
    
    
    words = re.findall('[A-Z][a-z]*', input)  
    
    
    
    result = []  
    for word in words:  
        word = chr( ord (word[0]) + 32) + word[1:]  
        result.append(word)  
    print (' '.join(result))  
    
if __name__ == "__main__":  
    input = 'BruceWayneIsBatman'
    putSpace(input) 
"""
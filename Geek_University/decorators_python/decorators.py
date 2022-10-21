"""
Decoradores (Decorators)

 # O que são decorators ?

   - Decorators são funcões;
   - Decorators envolvem outras funões e aprimoram seus comportamento;
   - Decorators também são exemplos de Higher Order Functions;
   - Decorators tem sua sintaxe própria, usando '@' (Syntact Sugar)
"""

# Decoratos como funcões (não recomendado / sem syntact sugar)

def seja_educado(func):
    def sendo():
        print("\nfoi um prazer conhecer voce")
        func()
        print("tenha um ótimo dia")
    return sendo


def saudacao():
    print("Seja Bem vindo Ao curso")


# Teste 1:
teste = seja_educado(saudacao)
teste()

#  Decorators com Syntact Sugar

@seja_educado
def raiva():
    print("EU TE ODEIO!")


@seja_educado
def dormir():
    print("Quero Dormir !")


# Testando
raiva()
dormir()

"""
Pseudo Exemplo:

.--------------------------------------------.
|Home | Produtos | Servicos | Administrativo |
'--------------------------------------------'

urls'l:
http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/servicos
http://www.suaempresa.com.br/administrativo


def checa_login(request):
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')


def home(request):
    return "Acesso Permitido"


def produtos(request):
    return "Acesso Permitido"


@checa_login
def servicos(request):
    return "Acesso Permitido"


@checa_login
def administrativo(request):
    return "Acesso Permitido"    
"""
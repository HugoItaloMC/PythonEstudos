def comer(food, qualidade):
    if qualidade:
        final = 'quero manter a forma'
    else:
        final = 'Só se vive uma vez'
    return f"Estou comendo {food} {final}"


def dormir(total_descanso):
    if total_descanso < 6:
       return 'Estou cansado dormi pouco'
    else:
        return 'Dormi demais, estou atrasado'

def engracado(pessoa):
    comediante = [
        'Jim Carrey',
        'Bozo'
    ]
    if pessoa in comediante:
        return True
    return False


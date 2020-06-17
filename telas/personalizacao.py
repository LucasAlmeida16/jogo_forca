def cores(cor):
    lista_cores = { 
        'vermelho' : '\033[31m',
        'azul' : '\033[34m',
        'amarelo' : '\033[33m',
        'preto' : '\033[30m',
        'roxo' : '\033[35m',
        'verde' : '\033[32m',
        'ciano' : '\033[36m',
        'limpa' : '\033[m',
        'preto_e_branco' : '\033[7;30;m',
    }
    return print(lista_cores.get(cor))

def separacao(valor):
    return print('-='*valor)

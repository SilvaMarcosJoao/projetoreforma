def titulo(msg: str):
    '''
    Esta função recebe um parâmetro string e exibe
    a string de formatada
    :param msg: recebe uma string 
    :return : não há retorno
    '''
    print('-'*len(msg))
    print(f'{msg}'.center(len(msg)))
    print('-'*len(msg))

def menu(items: list):
    '''
    Esta função recebe um parâmetro do tipo lista
    e exibe cada item dessa lista, sendo os itens as opções do
    menu
    :param items: recebe uma lista
    :return : não há retorno
    '''
    for v in items:
        print(v)
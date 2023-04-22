def validaInt(valor:int) -> int:
    '''
    Esta função recebe um parâmetro qualquer para ser validado
    se é ou não um valor inteiro
    :param valor: recebe um valor 
    :return v: retorna o valor validado
    '''
    while True:
        try:
           numInt = int(input(valor))
        except ValueError:
            print('\033[1;31mValor inválido\033[m')
        except TypeError:
            print('\033[1;31mTipo de valor errado\033[m')
        else:
            return numInt


def validaFloat(valor: float) -> float:
    '''
    Função recebe um parâmetro qualquer a ser validado se é um
    float ou não
    :param valor: recebe um parâmetro
    :return numF: retorna o valor após ser validado
    '''
    try:
        numF = float(input(valor))
    except ValueError:
        print('\033[1;31mPreço inválido\033[m')
    else:
        return numF
        
        
def validaString(texto: str) -> str:
    '''
    Esta função recebe um parâmetro qualquer para ser validado
    se é ou não uma String
    :param texto: recebe uma cadeia de caractere
    :return v: retorna a string após ser validada
    '''
    try:
        caractere = str(input(texto)).strip()
    except (ValueError, TypeError, FloatingPointError):
        print('\033[1;31mErro, valor digitado não é compatível com um texto\033[m')
    
    else:
        return caractere
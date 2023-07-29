from produto import *
from Func_Aparencia import *
from Func_Crud import * 
from Func_Validacoes import *
import os

while True:
    os.system('cls')
    co = Sistema()
    titulo('MENU PRINCIPAL')

    menu(['[1] - Cadastrar Produto', 
          '[2] - Listar Todos Produtos', 
          '[3] - Listar Produtos por Categoria', 
          '[4] - Listar Produto Mais Caro',
          '[5] - Listar Produto',  
          '[6] - Editar Produto', 
          '[7] - Excluir Produto',
          '[8] - Sair'])
    
    while True:
        op = validaInt('Escolha uma opção: ')
        if op >= 1 and op <= 8:
            break
        print('\033[1;35mErro, Opção inválida\033[m')

    if op == 1:
        desc = validaString('Descrição: ')
        forn = validaString('Fornecedor: ')
        qtd = validaInt('Quantidade: ')
        pre = validaFloat('Preço Unitário: R$')
        tot = qtd * pre
        data = validaString('Data da compra: ')
        menu(['[1] - Alvenaria', '[2] - Acabamento'])
        while True:
            idCategoria = validaInt('Qual categoria do produto ?: ')
            if idCategoria == 1 or idCategoria == 2:
                break
            print('\033[1;33mCategoria inválida\033[m')
        prod = Produto(desc, forn, qtd, pre, tot, data, idCategoria)
        co.cadastrar(prod)

    elif op == 2:
        co.listarProdutos()

    elif op == 3:
        menu(['[1] - Alvenaria', '[2] - Acabamento'])
        while True:
            idCategoria = validaInt('Deseja ver os produtos de quais categorias ?: ')
            if idCategoria == 1 or idCategoria == 2:
                break
            print('\033[1;33mCategoria inválida\033[m')
        co.listarPorCategoria(idCategoria)
        
    elif op == 4:
        co.listarPorMaisCaro()

    elif op == 5:
        idProduto = validaInt('Digite o ID do produto: ')
        co.listarProduto(idProduto)

    elif op == 6:
        idProduto = validaInt('Digite o ID do produto que deseja alterar: ')
        co.listarProduto(idProduto)
        desc = validaString('Descrição: ')
        compr = validaString('Fornecedor: ')
        qtd = validaInt('Quantidade: ')
        pre = validaFloat('Preço Unitário: R$')
        tot = qtd * pre
        data = validaString('Data da compra: ')
        menu(['[1] - Alvenaria', '[2] - Acabamento'])
        idCategoria = validaInt('Qual categoria do produto ?: ')
        prod = Produto(desc, compr, qtd, pre, tot, data, idCategoria)
        co.alterarProduto(idProduto, prod)

    elif op == 7:
        idProduto = validaInt('Digite o ID do produto que deseja excluir: ')
        co.excluirProduto(idProduto)

    elif op == 8:
        break
    os.system('pause')
import sqlite3
from produto import *

class Sistema:

    def __init__(self, nomeBanco = 'C:/CRUDGerenciamentoProdutos/DbProdutos.db') -> None:
        self.__status = False
        self.__nomeBanco = nomeBanco
        self.__conexao = self.__nomeBanco

    @property
    def status(self)-> bool:
        return self.__status
    
    @status.setter
    def status(self, status: bool):
        self.__status = status

    def conectar(self):
        '''
        Esta função é responsavel por conectar o banco de dados
        :return: não há retorno
        '''
        try:
            self.__conexao = sqlite3.connect(self.__nomeBanco)
        except(sqlite3.DatabaseError, sqlite3.Error, ConnectionError):
            print('\033[1;31mErro ao conectar com o banco de dados\033[m')
        else:
            self.__status = True
            

    def desconectar(self) -> None:
        '''
        Função responsável por desconectar o banco de dadoss 
        :return : não há retorno
        '''
        try:
            if self.__conexao and self.__status:
                self.__conexao.close()
        except (ConnectionError, sqlite3.Error):
            print('\033[1;32mErro ao desconectar-se\033[m')
        else:
            self.__status = False


    def cadastrar(self, obj:Produto) -> None:
        '''
        Função responsável por cadastrar o objeto do tipo produto
        :param obj: recebe um objeto do tipo Produto
        :return: não há retorno
        '''
        try:
            if self.__status == False:
                self.conectar()
                cursor = self.__conexao.cursor()
                cursor.execute(
                f'''INSERT INTO Produto (descricao, fornecedor, quantidade, precoUnitario, precoTotal, dataCompra, idCategoria) VALUES
                ('{obj.descricao}', '{obj.fornecedor}', '{obj.quantidade}', '{obj.preco}', {obj.total},'{obj.data}', '{obj.idCategoria}') ''')
            self.__conexao.commit()
        except Exception as e:
            print(f'\033[1;33mErro, ao inserir os dados: {e}\033[m')
        else:
            print('\033[1;32mCadastrado com sucesso!\033[m')
        finally:
            self.desconectar()
        

    def listarProdutos(self) -> None:
        '''
        Esta função tem como objetivo exibir a lista de todos os produtos cadastrados
        :return : não há retorno
        '''
        try:
            if self.__status == False:
                self.conectar()
                cursor = self.__conexao.cursor()
                self.produtos = cursor.execute('Select * from Produto').fetchall()
        except(NameError, ConnectionError, TypeError):
                print('\033[1;33mErro ao listar os produtos\033[m')
        else:
            print(f'{"ID":^3}|{"DESCRIÇÃO DO PRODUTO":<25} | {"FORNECEDOR":<15} | {"QTD":^5} | {"PREÇO UNITÁRIO":<12} | {"PREÇO TOTAL":<12} | {"DATA":<12} | {"ID CATEGORIA"}')
            tot = 0
            for p in self.produtos:
                print(f'{p[0]:^3}  {p[1]:<25} {p[2]:<18} {p[3]:<7} R${p[4]:<16} {p[5]:<12} {p[6]:<18} {p[7]}')
                tot+=p[5]
            print()
            print(f'Total Geral: R${tot:.2f}')
        finally:
            self.desconectar()
                
            
    def listarProduto(self, idProduto) -> None:
        try:
            if self.__status == False:
                self.conectar()
                cursor = self.__conexao.cursor()
                self.produto = cursor.execute(f'''SELECT idProduto, descricao, fornecedor, quantidade, precoUnitario, precoTotal, dataCompra, idCategoria from Produto
                WHERE idProduto = ('{idProduto}')''').fetchmany()   
        except(NameError, TypeError, ConnectionError, sqlite3.Error):
            print('\033[1;33mErro ao listar o produto\033[m')
        else:
            if len(self.produto) == 0:
                print('\033[1;33mNão existe produto cadastrado com esse ID\033[m')
            else:
                print(f'{"ID":^3}|{"DESCRIÇÃO DO PRODUTO":<25} | {"FORNECEDOR":<15} | {"QTD":^5} | {"PREÇO UNITÁRIO":<12} | {"PREÇO TOTAL":<12} | {"DATA":<12} | {"ID CATEGORIA"}')
                for pro in self.produto:
                    print(f'{pro[0]:^3}  {pro[1]:<25} {pro[2]:<18} {pro[3]:<7} R${pro[4]:<16} {pro[5]:<12} {pro[6]:<18} {pro[7]}')
                print()
        finally:
            self.desconectar()


    def listarPorCategoria(self, IdCategoria:int) -> None:
        '''
        Esta função recebe um parâmetro inteiro, onde através desse parâmetro, exibimos 
        os produtos por categoria 
        :param IdCategoria: recebe um parâmetro inteiro
        :return: não há retorno
        '''
        try:
            #if self.__status == False:
            self.conectar()
            cursor = self.__conexao.cursor() 
            self.porCategoria = cursor.execute(f'''SELECT idProduto, descricao, fornecedor, quantidade, precoUnitario, precoTotal, dataCompra, categoriaProduto.nomeCategoria 
                from categoriaProduto, Produto  WHERE categoriaProduto.idCategoria = Produto.idCategoria and categoriaProduto.idCategoria = {IdCategoria} ''').fetchall()
        except sqlite3.Error:
            print('\033[1;33mNada foi encontrado\033[m')
        else:
            print(f'{"ID":^3}|{"DESCRIÇÃO DO PRODUTO":<25} | {"FORNECEDOR":<15} | {"QTD":^5} | {"PREÇO UNITARIO":<12} | {"PREÇO TOTAL":<12} | {"DATA":<12} | {"CATEGORIA"}')
            for pC in self.porCategoria:
                print(f'{pC[0]:^3}  {pC[1]:<25} {pC[2]:<18} {pC[3]:<7} R${pC[4]:<16} {pC[5]:<12} {pC[6]:<14} {pC[7]}')
            print()
        finally:
            self.desconectar()
                

    def listarPorMaisCaro(self) -> None:
        '''
        Dentre todos os produtos, exibe o mais caro de acordo
        com o filtro SQL
        a string de formatada
        :return : não há retorno
        '''
        try:
            if self.__status == False:
                self.conectar()
                cursor = self.__conexao.cursor() 
                self.porMaisCaro = cursor.execute(f'''SELECT idproduto, descricao, fornecedor, quantidade, precoUnitario, max(precoTotal), 
                dataCompra, idCategoria from Produto''').fetchmany()
        except (NameError, TypeError, ConnectionError):
            print('\033[1;33mNada foi encontrado\033[m')
        else:
            print(f'{"ID":^3}|{"DESCRIÇÃO DO PRODUTO":<25} | {"FORNECEDOR":<15} | {"QTD":^5} | {"PREÇO UNITÁRIO":<12} | {"PREÇO TOTAL":<12} | {"DATA":<12} | {"CATEGORIA"}')
            for l in self.porMaisCaro:
                print(f'{l[0]:^3}  {l[1]:<25} {l[2]:<18} {l[3]:<7} R${l[4]:<16} {l[5]:<12} {l[6]:<18} {l[7]}')
            print()           
        finally:
            self.desconectar()
            
    def alterarProduto(self, idProduto:int, produto: Produto) -> None:
        '''
        Esta função tem por objetivo alterar os valores cadastrado de um produto especifico, por isso,
        recebe como parâmetro um parâmetro inteiro para verificar se de fato o produto a ser modificado existe.
        Outro parâmetro é um objeto do tipo Produto, que traz novos dados que irão substituir os antigos do produto.
        :param idProduto: recebe um valor inteiro
        :param produto: recebe um objeto do Tipo Produto 
        :return : não há retorno
        '''
        try:
            if self.__status == False:
                self.conectar()
                cursor = self.__conexao.cursor()
                cursor.execute(f'''UPDATE Produto 
                SET descricao =('{produto.descricao}'), 
                fornecedor =('{produto.fornecedor}'), 
                quantidade =('{produto.quantidade}'), 
                precoUnitario =('{produto.preco}'), 
                precoTotal =('{produto.total}'),
                dataCompra =('{produto.data}'), 
                idCategoria =('{produto.idCategoria}')
                WHERE idproduto =('{idProduto}') ''')
                self.__conexao.commit()
                print('\033[1;32mProduto alterado com sucesso!\033[m')
            else:
                print('\033[1;33mNão existe produto cadastrado com esse ID\033[m')
        except sqlite3.DataError as ex:
            print(ex)
        finally:
            self.desconectar()


    def excluirProduto(self, idProduto: int) -> None:
        '''
        Esta função exclui um produto de acordo com o parâmetro inteiro recebido.
        :param idProduto: recebe um valor inteiro 
        :return : não há retorno
        '''
        try:
            if self.__status == False:
                self.conectar()
                cursor = self.__conexao.cursor()
                self.resultado = cursor.execute(f'''SELECT idProduto, descricao, fornecedor, quantidade, precoUnitario, precoTotal, dataCompra, idCategoria from Produto
                WHERE idProduto = ('{idProduto}')''').fetchmany()   
        except sqlite3.DataError as ex:
            print(ex)
        else:
            if len(self.resultado) == 0:
                print('\033[1;33mNão existe produto cadastrado com esse ID\033[m')
            else:
                cursor.execute(f'''DELETE FROM Produto
                WHERE idproduto =('{idProduto}') ''')
                self.__conexao.commit()
                print('\033[1;32mProduto deletado com sucesso!\033[m')
        finally:
            self.desconectar()  
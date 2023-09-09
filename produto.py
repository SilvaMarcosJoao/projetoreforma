import bancoDado

class Produto:
    banco = bancoDado.BancoDados()
    banco.tabelaCategoria()
    banco.tabelaProduto()
    def __init__(self = None, 
                descricao = None, 
                fornecedor = None, 
                quantidade = None, 
                preco = None, 
                total = None, 
                data = None, 
                idCategoria = None) -> None:
        #atributos
        self.__descricao = descricao
        self.__fornecedor = fornecedor
        self.__quantidade = quantidade
        self.__preco = preco
        self.__total = total
        self.__data = data
        self.__idCategoria = idCategoria
        
    #Getters e setters
    def get_descricao(self) -> str:
        return self.__descricao
    
    def set_descricao(self, desc:str) -> None:
        self.__descricao = desc

    def get_fornecedor(self) -> str:
        return self.__fornecedor
    
    def set_fornecedor(self, fornecedor:str) -> None:
        self.__fornecedor = fornecedor

    def get_quantidade(self) -> int:
        return self.__quantidade
    
    def set_quantidade(self, qtd:int) -> None:
        self.__quantidade = qtd

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco:float) -> None:
        self.__preco = preco

    def get_total(self) -> float:
        return self.__total
    
    def set_total(self, tot:float) -> None:
        self.__total = tot
        
    def get_data(self) -> str:
        return self.__data
    
    def set_data(self, data:str) -> None:
        self.__data = data

    def get_idCategoria(self) -> int:
        return self.__idCategoria
    
    def set_idCategoria(self, id:int) -> None:
        self.__idCategoria = id

    def cadastrar(self, desc:str, forne:str, quant:int, preco:float, total:float, data:str, idCategoria:int) -> None:
        """
        Função responsável por cadastrar o produto
        :param: desc, forne, quant, preco, total, data, idCategoria.
        :return: não há retorno
        """
        try:
            self.banco.conectar()
            self.banco.cursor.execute(
                f'''INSERT INTO Produto (descricao, fornecedor, quantidade, precoUnitario, precoTotal, dataCompra, idCategoria) VALUES
                ('{desc}', '{forne}', '{quant}', '{preco}', {total},'{data}', '{idCategoria}') ''')
            self.banco.conexao.commit()
        except Exception as e:
            print(f'\033[1;33mErro, ao inserir os dados: {e}\033[m')
        else:
            print('\033[1;32mCadastrado com sucesso!\033[m')
        finally:
            self.banco.desconectar()

    def listarProdutos(self) -> list:
        """
        Esta função tem como objetivo exibir a lista de todos os produtos cadastrados
        :return: Retorna uma lista com todos os produtos.
        """
        try:
            self.banco.conectar()
            self.produtos = self.banco.cursor.execute(" SELECT * FROM produto").fetchall()
        except(NameError, ConnectionError, TypeError):
                print('\033[1;33mErro ao listar os produtos\033[m')
        else:
            return self.produtos
        finally:
            self.banco.desconectar()
    
    def listarProduto(self, descricaoProduto: str) -> list:
        """
        Procurar um produto específico de acordo com o parâmetro passado.
        :param: descricaoProduto.
        :return: Retorna uma lista com o produto procurado e seus respectivos dados.
        """
        try:
            self.banco.conectar() 
            self.produto = self.banco.cursor.execute(f'''SELECT idProduto, descricao, fornecedor, quantidade, precoUnitario, precoTotal, dataCompra, idCategoria FROM produto
                WHERE  descricao like ('{descricaoProduto[0]}%') ''').fetchall()   
        except(NameError, TypeError, ConnectionError):
            print('\033[1;33mErro ao listar o produto\033[m')
        else:
            return self.produto
        finally:
            self.banco.desconectar()
    
    def listarPorCategoria(self, IdCategoria:int) -> list:
        """
        Esta função recebe um parâmetro inteiro, onde através desse parâmetro, exibimos 
        os produtos por categoria 
        :param: IdCategoria.
        :return: Retorna uma lista com produtos de determinada categoria.
        """
        try:
            self.banco.conectar()
             
            self.porCategoria = self.banco.cursor.execute(f'''SELECT idProduto, descricao, fornecedor, quantidade, precoUnitario, precoTotal, dataCompra, categoriaProduto.nomeCategoria 
                from categoriaProduto, Produto  WHERE categoriaProduto.idCategoria = Produto.idCategoria and categoriaProduto.idCategoria = {IdCategoria} ''').fetchall()
        except:
            print('\033[1;33mNada foi encontrado\033[m')
        else:
            return self.porCategoria
        finally:
            self.banco.desconectar()

    def alterarProduto(self, idProduto:int, desc:str, forne:str, quant:int, preco:float, total:float, data:str, idCategoria:int) -> None:
        """
        Esta função tem por objetivo alterar os valores cadastrado de um produto especifico.
        :param: idProduto, desc, forne, quant, preco, total, data, idCategoria.
        :return: Não há retorno,
        """
        try:
            
            self.banco.conectar()
            self.banco.cursor.execute(f'''UPDATE Produto 
                SET descricao =('{desc}'), 
                fornecedor =('{forne}'), 
                quantidade =('{quant}'), 
                precoUnitario =('{preco}'), 
                precoTotal =('{total}'),
                dataCompra =('{data}'), 
                idCategoria =('{idCategoria}')
                WHERE idproduto = ('{idProduto}') ''')
            self.banco.conexao.commit()
            print('\033[1;32mProduto alterado com sucesso!\033[m')
        except:
            print('Erro')
        finally:
            self.banco.desconectar()
    
    def excluirProduto(self, idProduto: int) -> None:
        """
        Esta função exclui um produto de acordo com o idProduto do recebido.
        :param: idProduto recebe um valor inteiro. 
        :return: Não há retorno.
        """
        try:
            self.banco.conectar()
                
            self.resultado = self.banco.cursor.execute(f'''SELECT idProduto, descricao, fornecedor, quantidade, precoUnitario, precoTotal, dataCompra, idCategoria from Produto
                WHERE idProduto = ('{idProduto}')''').fetchmany()   
        except:
            print('Erro')
        else:
            if len(self.resultado) == 0:
                print('\033[1;33mNão existe produto cadastrado com esse ID\033[m')
            else:
                self.banco.cursor.execute(f'''DELETE FROM Produto
                WHERE idproduto =('{idProduto}') ''')
                self.banco.conexao.commit()
                print('\033[1;32mProduto deletado com sucesso!\033[m')
        finally:
            self.banco.desconectar()
import sqlite3
from produto import *

class BancoDados:
    def __init__(self) -> None:
        self.nomeBanco = 'reformaBanco.db'

    def conectar(self):
        """
        Esta função é responsavel por conectar o banco de dados
        :return: não há retorno
        """
        try:
            self.conexao = sqlite3.connect(self.nomeBanco)
            self.cursor = self.conexao.cursor()
        except(sqlite3.DatabaseError, sqlite3.Error, ConnectionError):
            print('\033[1;31mErro ao conectar com o banco de dados\033[m')
        else:
            print('Conectado com sucesso!')
            

    def desconectar(self) -> None:
        """
        Função responsável por desconectar o banco de dadoss 
        :return : não há retorno
        """
        try:
            self.conexao.close()
        except (ConnectionError, sqlite3.Error):
            print('\033[1;32mErro ao desconectar-se\033[m')
        else:
            print('Desconectado')

    def tabelaCategoria(self) -> None:
        try:
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS categoriaProduto (
                idCategoria	INTEGER NOT NULL UNIQUE,
                nomeCategoria	TEXT(40) NOT NULL,
                PRIMARY KEY(idCategoria AUTOINCREMENT) ); """)
        except Exception(AttributeError, ConnectionError, sqlite3.Error) as erroCategoria:
            print(erroCategoria)

    def tabelaProduto(self) -> None:
        try:
            
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS produto (
                idProduto	INTEGER NOT NULL UNIQUE,
                descricao	TEXT(120) NOT NULL,
                fornecedor	TEXT(50) NOT NULL,
                quantidade	INTEGER NOT NULL,
                precoUnitario	REAL NOT NULL,
                precoTotal	REAL NOT NULL,
                dataCompra	TEXT(10) NOT NULL,
                idCategoria	INTEGER NOT NULL,
                FOREIGN KEY(idCategoria) REFERENCES categoriaProduto(idCategoria),
                PRIMARY KEY(idProduto AUTOINCREMENT) ); """)
        except Exception(AttributeError, ConnectionError, sqlite3.Error) as erroProduto:
            print(erroProduto)

    

db = BancoDados()
db.conectar()
db.tabelaCategoria()
db.tabelaProduto()
db.desconectar()
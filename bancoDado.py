import sqlite3
from produto import *

class BancoDados:
    def __init__(self) -> None:
        
        self.nomeBanco = '..\\projetoreforma\\reformaBanco.db'
        self.conexao = None
        self.cursor = None


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
            print('Descontectado')

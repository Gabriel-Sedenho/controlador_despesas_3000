from src.database.conexao import Conexao
import mysql.connector

class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login:str, senha:str) -> bool:
        con, cur = Conexao().conectar()
        cur.execute("""
INSERT INTO tb_usuarios(login, senha)
VALUES (%s, %s)
""",
[login, senha])
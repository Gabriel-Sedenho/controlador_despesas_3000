import mysql.connector

class Conexao:
    def __init__(Self):
        pass

    @staticmethod
    def conectar() -> list:
        try:
            # conectando ao banco de dados
            conexao = mysql.connector.connect(
                host="127.0.0.1",
                port="3306",
                user="root",
                password="root",
                database="controlador_despesas"
            )
            cursor = conexao.cursor()

            return conexao, cursor
        except Exception as e:
            print(f'ERRO: {e}')
            return None, None
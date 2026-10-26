from src.database.conexao import Conexao


class Categoria:
    def __int__(self):
        pass

    @staticmethod
    def adicionar(categoria: str, login: str) -> int:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("erro ao tentar conectar")
            return None
        try:
            cursor.execute(
                """
                            INSERT INTO tb_categorias(nome_categoria, login)
                            VALUES (%s, %s)
                            """,
                [categoria, login],
            )

            id_categoria = cursor.lastrowid
            conexao.commit()
            conexao.close()
            return id_categoria

        except Exception as e:
            print(f"deu erro aqui: {e}")
            return None

    @staticmethod
    def excluir(id_categoria:int) -> bool:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("erro ao tentar conectar")
            return None
        
        try:
            cursor.execute("""
                            DELETE FROM tb_categorias
                            WHERE id_categoria = '%s';
                            """,
                            [id_categoria])
            conexao.commit()
            conexao.close()
            return True
    
        except Exception as e:
            print(f"deu erro aqui: {e}")
            return False

    @staticmethod
    def recuperar_todos(login:str) -> list:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("erro ao tentar conectar")
            return None
        
        try:
            cursor.execute("select nome_categoria from tb_categorias where login = %s",
                           [login])
            resultado = cursor.fetchone()
            conexao.commit()
            conexao.close()
            return resultado
        
        except Exception as e:
            print(f"deu erro aqui: {e}")
            return None
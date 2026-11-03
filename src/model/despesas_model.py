# excluir: terá o parâmetro id_despesa (int), e retornará um boolean.
# alterar: terá os parâmetros id_despesa (int), id_categoria (int), descricao (String), valor (float) e data (String), e retornará um boolean

from src.database.conexao import Conexao

class Despesas:
    def __init__(self):
        pass

    @staticmethod
    def incluir(id_categoria:int, descricao:str, valor:float, data:str) -> int:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("erro ao conectar")
            return None

        try:
            cursor.execute("""
                            INSERT INTO tb_despesas(id_categoria, descricao_despesa, valor, dt_cadastro)
                            VALUES (%s, %s, %s,%s)
                            """, [id_categoria, descricao, valor, data])

            id_despesa = cursor.lastrowid
            conexao.commit()
            conexao.close()
            return id_despesa
        except Exception as e:
            print(f"deu erro aqui {e}")
            return None
    
    @staticmethod
    def recuperar_todos(login:str) -> list:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("erro ao tentar conectar")
            return None
        
        try:
            cursor.execute("select valor, dt_cadastro, id_categoria, descricao_despesa, from tb_despesas where login = %s",
                           [login])
            resultado = cursor.fetchall()
            conexao.commit()
            conexao.close()
            return resultado
        
        except Exception as e:
            print(f"deu erro aqui: {e}")
            return None
    
    @staticmethod
    def recuperar_por_categoria(login:str, id_categoria:int) -> list:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("erro ao tentar conectar")
            return None

        try:
            cursor.execute("select valor, dt_cadastro, id_categoria, descricao_despesa, from tb_despesas where login = %s and id_categoria = %s",
                           [login], [id_categoria])
            resultado = cursor.fetchall()
            conexao.commit()
            conexao.close()
            return resultado
        
        except Exception as e:
            print(f"deu erro aqui: {e}")
            return None
        
    @staticmethod
    def excluir(id_despesa:int) -> bool:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("erro ao tentar conectar")
            return None
        
        try:
            cursor.execute("""
                            DELETE FROM tb_despesas
                            WHERE id_despesa = '%s';
                            """,
                            [id_despesa])
            conexao.commit()
            conexao.close()
            return True
    
        except Exception as e:
            print(f"deu erro aqui: {e}")
            return False
        
    def alterar(id_despesa:int, login:str, id_categoria:int, data:str, descricao:str, valor:int) -> bool:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("erro ao tentar conectar")
            return None

        try:
            cursor.execute("""
                            UPDATE tb_despesas SET
                                id_categoria = %s,
                                descricao = %s,
                                valor = %s,
                                data = %s
                            WHERE
                                id_despesa = %s
                                AND id_usuario = %s;
                            """,
                            [id_categoria, descricao, valor, data, id_despesa, login])
            
            conexao.commit()
            conexao.close()
            return True
    
        except Exception as e:
            print(f"deu erro aqui: {e}")
            return False
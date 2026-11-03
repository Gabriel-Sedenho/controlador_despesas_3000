
# excluir: terá o parâmetro id_despesa (int), e retornará um boolean.
# alterar: terá os parâmetros id_despesa (int), id_categoria (int), descricao (String), valor (float) e local (String), e retornará um boolean

from src.database.conexao import Conexao

class Despesas:
    def __init__(self):
        pass

    def incluir(id_categoria:int, descricao:str, valor:float, data:str) -> int:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("erro ao conectar")
            return None

        try:
            cursor.execute("""
                            INSERT INTO tb_despesas(id_caegoria, descricao, valor, dt_cadastro)
                            VALUES (%s, %s, %s,%s)
                            """, [id_categoria, descricao, valor, data])

            conexao.commit()
            conexao.close()
            return id_categoria
        except Exception as e:
            print(f"deu erro aqui {e}")
            return None
    
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
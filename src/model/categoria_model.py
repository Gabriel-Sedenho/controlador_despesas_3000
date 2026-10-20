# a classe será chamada Categoria e terá três métodos
# adicionar, que terá um parâmetro chamado categoria(String) e retornará um int e outro chamado login(String) que retornará um int
# recuperar_todos , que terá um parâmetro chamado login(String) e retornará um List[Dict]
# excluir, que terá um parâmetro chamado id_categoria(int) e retornará um boolean

from src.database.conexao import Conexao


class Categoria:
    def __int__(self):
        pass

    @staticmethod
    def adicionar(categoria:str, login:str) -> int:
        conexao, cursor = Conexao().conectar
        if not conexao:
            print("erro ao tentar conectar")
            return None

        
        cursor.execute("""
                        INSERT INTO tb_categorias(nome_categoria, login,)
                        VALUES (%s, %s, %s)
                        """,
                        [categoria, login])
        
        conexao.commit()
        conexao.close()
        return 
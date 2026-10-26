# a classe se chamara Despesa e terá 5 métodos
# incluir: terá os parâmetros id_categoria (int), descricao (String), valor (float) e data (String), e retornará um int.
# recuperar_todos: terá o parâmetro login (String), e retornará uma List[Dict] (ou lista de dicionários).
# recuperar_por_categoria: terá os parâmetros login (String) e id_categoria (int), e retornará uma List[Dict] (ou lista de dicionários).
# excluir: terá o parâmetro id_despesa (int), e retornará um boolean.
# alterar: terá os parâmetros id_despesa (int), id_categoria (int), descricao (String), valor (float) e local (String), e retornará um boolean

from src.database.conexao import Conexao

class Despesas:
    def __init__(self):
        pass

    def incluir(id_categoria:int, descricao:str, valor:float, data:str) -> int:
        pass
import flet as ft

from src.model.usuario_model import Usuario
from src.model.despesa_model import Despesas
from src.model.categoria_model import Categoria

class DespesaCategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/despesascategoria"


        self.width = 800
        self.height = 800
        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.vertical_alignment = "top"
        self.horizontal_alignment = "center"

        self.dados_usuario = pagina.session.store.get("usuario_logado")
        self.username = self.dados_usuario.get("login")
        categorias = Categoria.recuperar_todos(self.username)

        self.lista_despesas = []
        opcoes = []
        for categoria in categorias:
            self.id_categoria = categoria.get("id_categoria")
            nome_categoria = categoria.get("nome_categoria")
            opcoes.append(ft.DropdownOption(key=self.id_categoria, text=nome_categoria))

        titulo = ft.Text(value="Despesas por categoria",
                        color="#CFEEE6",
                        size=30)



        self.campo_categoria = ft.Dropdown(color="#CFEEE6" ,options=opcoes, width=300, on_select=self.ver_despesas_por_categoria)

        tabela = ft.DataTable(columns=[ft.DataColumn(label="id_despesa"),
                                       ft.DataColumn(label="Descrição"),
                                       ft.DataColumn(label="Valor"),
                                       ft.DataColumn(label="Data"),
                                       ft.DataColumn(label="Excluir"),
                                       ], rows=self.lista_despesas, heading_row_color="#28C39D")
        

        self.controls = [titulo, self.campo_categoria,tabela]



    def ver_despesas_por_categoria(self):
        self.lista_despesas.clear()
        despesas = Despesas.recuperar_por_categoria(self.username, self.campo_categoria.value)

        for despesa in despesas:
            id_despesa = despesa.get("id_despesa")
            descricao_despesa = despesa.get("descricao_despesa")
            valor_despesa = despesa.get("valor")
            data = despesa.get("dt_cadastro")

            dados_despesa = ft.DataRow(cells=[ft.DataCell(content=f"{id_despesa}"),
                              ft.DataCell(content=f"{descricao_despesa}"),
                              ft.DataCell(content=f"{valor_despesa}"),
                              ft.DataCell(content=f"{data}"),
                              ft.DataCell(ft.Button(icon=ft.Icons.DELETE, bgcolor="#28C39D", color="#CFEEE6", key=despesa.get("id_despesa"), on_click=self.excluir))
                              ], color="#CFEEE6")
            
            self.lista_despesas.append(dados_despesa)
        self.pagina.update()

    def excluir(self, e):
        id_despesa = e.control.key
        Despesas.excluir(id_despesa)
        self.ver_despesas_por_categoria()
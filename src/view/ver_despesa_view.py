import flet as ft

from src.model.usuario_model import Usuario
from src.model.despesa_model import Despesas
from src.model.categoria_model import Categoria

class DespesaMostrarView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/despesas"

        self.width = 800
        self.height = 600
        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.vertical_alignment = "top"
        self.horizontal_alignment = "center"

        self.dados_usuario = pagina.session.store.get("usuario_logado")
        self.username = self.dados_usuario.get("login")

        self.lista_despesas = []
        
        titulo = ft.Text(value="Despesas",
                        color="#CFEEE6",
                        size=30)

        botao_ver_todos = ft.Button(icon=ft.Icons.UPDATE, bgcolor="#28C39D", color="#CFEEE6", on_click=self.ver_despesas)



        tabela = ft.DataTable(columns=[ft.DataColumn(label="id_despesa"),
                                       ft.DataColumn(label="Descrição"),
                                       ft.DataColumn(label="Valor"),
                                       ft.DataColumn(label="Categoria"),
                                       ft.DataColumn(label="Data"),
                                       ft.DataColumn(label="Excluir"),
                                       ], rows=self.lista_despesas, heading_row_color="#28C39D")

        self.controls = [titulo, botao_ver_todos, tabela]



    def ver_despesas(self):
        self.lista_despesas.clear()
        despesas = Despesas.recuperar_todos(self.username)

        for despesa in despesas:
            id_despesa = despesa.get("id_despesa")
            descricao_despesa = despesa.get("descricao_despesa")
            valor_despesa = despesa.get("valor")
            categoria = despesa.get("id_categoria")
            data = despesa.get("dt_cadastro")

            dados_despesa = ft.DataRow(cells=[ft.DataCell(content=f"{id_despesa}"),
                              ft.DataCell(content=f"{descricao_despesa}"),
                              ft.DataCell(content=f"{valor_despesa}"),
                              ft.DataCell(content=f"{categoria}"),
                              ft.DataCell(content=f"{data}"),
                              ft.DataCell(ft.Button(icon=ft.Icons.DELETE, bgcolor="#28C39D", color="#CFEEE6", key=despesa.get("id_despesa"), on_click=self.excluir))
                              ], color="#CFEEE6")
            
            
            self.lista_despesas.append(dados_despesa)
        self.pagina.update()

    def excluir(self, e):
        id_despesa = e.control.key
        Despesas.excluir(id_despesa)
        self.ver_despesas()
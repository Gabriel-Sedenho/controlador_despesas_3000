import flet as ft

from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesas

class DespesaInserirView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/despesas"

        self.width = 800
        self.height = 600
        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        self.dados_usuario = pagina.session.store.get("usuario_logado")
        self.username = self.dados_usuario.get("login")
        categorias = Categoria.recuperar_todos(self.username)

        lista_categorias = []
        for categoria in categorias:
            opcao = ft.DropdownOption(key=categoria.get("nome_categoria"))
            lista_categorias.append(opcao)

        titulo = ft.Text(value="Inserir Despesa",
                        color="#CFEEE6",
                        size=30)


        self.dropdown = ft.Dropdown(label="Selecione uma categoria", align=self.horizontal_alignment,
                                    options=[
                                        lista_categorias
                                    ])
        self.campo_nova_despesa = ft.TextField(label="Nome da despesa", color="#CFEEE6")
        botao_cadastrar = ft.Button(icon=ft.Icons.ADD, bgcolor="#28C39D", color="#CFEEE6")

        self.controls = [titulo, self.dropdown, self.campo_nova_despesa, botao_cadastrar]
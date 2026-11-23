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
            lista_categorias.append(ft.DropdownOption(key=categoria.get("nome_categoria")))




        # código da tela
        titulo = ft.Text(value="Inserir Despesa",
                        color="#CFEEE6",
                        size=30)
        
        self.dropdown = ft.Dropdown(label="Selecione uma categoria", align=self.horizontal_alignment,
                                    options=[
                                        lista_categorias
                                    ])
        
        self.campo_descricao = ft.TextField(label="Descrição", color="#CFEEE6")

        self.campo_valor = ft.TextField(label="Valor da despesa", color="#CFEEE6", keyboard_type=ft.KeyboardType.NUMBER)

        # self.campo_data = ft.TextField(label="data da despesa", color="#CFEEE6", keyboard_type=ft.KeyboardType.DATETIME)

        self.campo_data = ft.DatePicker()

        botao_cadastrar = ft.Button(icon=ft.Icons.ADD, bgcolor="#28C39D", color="#CFEEE6")

        self.controls = [titulo, self.campo_descricao, self.campo_valor, self.campo_data,botao_cadastrar, ]
        ###

        def adicionar_despesa(self):
            Despesas.incluir(categoria.get("id_categoria"), self.campo_descricao.value, self.campo_valor.value)

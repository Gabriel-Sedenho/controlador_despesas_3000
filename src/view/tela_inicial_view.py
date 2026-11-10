import flet as ft
from src.model.usuario_model import Usuario

class InicioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/inicio"

        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.horizontal_alignment = "center"
        self.width = 800
        self.height = 800

        titulo = ft.Text(value="Tela Inicial", color="#CFEEE6", size=30, font_family="Cascadia Code")

        inserir_despesa = ft.Button(content="Nova despesa", width=150, bgcolor="#28C39D", color="#CFEEE6")
        ver_despesas = ft.Button(content="Ver despesas", width=150, bgcolor="#0F7A62", color="#CFEEE6")

        inserir_categoria = ft.Button(content="Nova categoria", width=150, bgcolor="#28C39D", color="#CFEEE6")
        ver_categorias = ft.Button(content="Ver categorias", width=150, bgcolor="#0F7A62", color="#CFEEE6")

        linha_botoes = ft.Row(controls=[inserir_categoria, ver_categorias, inserir_despesa, ver_despesas], width=600)

        self.controls = [titulo, linha_botoes]
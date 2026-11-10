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
        self.vertical_alignment = "center"
        self.width = 800
        self.height = 800

        titulo = ft.Text(value="Tela Inicial", color="#CFEEE6")

        inserir_despesa = ft.Button(content="Inserir despesa", width=250, bgcolor="#28C39D", color="#CFEEE6")
        ver_despesas = ft.Button(content="Visualizar suas despesas", width=250, bgcolor="#0F7A62", color="#CFEEE6")

        inserir_categoria = ft.Button(content="Inserir categoria", width=250, bgcolor="#28C39D", color="#CFEEE6")
        ver_categorias = ft.Button(content="Vizualizar suas categorias", width=250, bgcolor="#0F7A62", color="#CFEEE6")

        self.controls = [titulo, inserir_despesa, ver_despesas, inserir_categoria, ver_categorias]
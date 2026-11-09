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

        self.controls = [titulo]
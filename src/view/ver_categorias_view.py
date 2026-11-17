import flet as ft

from src.model.usuario_model import Usuario

class CategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/categorias"

        self.width = 800
        self.height = 600
        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#ffffff"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        titulo = ft.Text(value="Categorias",
                        color="#505ab4",
                        size=30)
        
        self.controls = [titulo]
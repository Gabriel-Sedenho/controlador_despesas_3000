import flet as ft

from src.model.usuario_model import Usuario

class DespesaCategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/despesascategoria"

        self.width = 800
        self.height = 600
        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#ffffff"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        titulo = ft.Text(value="Despesas por categoria",
                        color="#505ab4",
                        size=30)
        
        self.controls = [titulo]
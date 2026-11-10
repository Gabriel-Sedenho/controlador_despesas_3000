import flet as ft

from src.model.usuario_model import Usuario

class DespesaMostrarView(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.route = "/despesas"

        self.width = 800
        self.height = 600
        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#ffffff"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        title = ft.Text(value="Despesas",
                        color="#505ab4",
                        size=30,)
        
        self.controls = [title]
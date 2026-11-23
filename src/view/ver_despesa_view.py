import flet as ft

from src.model.usuario_model import Usuario
from src.model.despesa_model import Despesas

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


        titulo = ft.Text(value="Despesas",
                        color="#CFEEE6",
                        size=30)


        

        self.controls = [titulo]


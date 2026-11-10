import flet as ft
from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria

class CategoriaView:
    def __init__(self, pagina:ft.Page):
        super().__init__()
    
        self.pagina = pagina
        self.route = "/categoriacadastro"

        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.horizontal_alignment = "center"
        self.width = 800
        self.height = 800

        titulo = ft.Text(value="Criar nova categoria", color="#CFEEE6", size=30, font_family="Cascadia Code")

        pagina.controls = [titulo]
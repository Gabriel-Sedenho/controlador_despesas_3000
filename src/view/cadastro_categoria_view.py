import flet as ft
from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria

class CadastroCategoriaView:
    def __init__(self, pagina:ft.Page):
        super().__init__()
    
        self.pagina = pagina
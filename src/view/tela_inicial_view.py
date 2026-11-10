import flet as ft
from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesas

class InicioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        async def mudar_cores():  
            self.bgcolor = "#ffffff"
            titulo.color = "#000000"

        self.pagina = pagina

        self.route = "/inicio"

        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.horizontal_alignment = "center"
        self.width = 800
        self.height = 800

        titulo = ft.Text(value="Principal", color="#CFEEE6", size=30, font_family="Cascadia Code")

        botao_modo_claro = ft.Button(content="Mudar pro modo claro", on_click=mudar_cores)


            


        self.controls = [titulo, botao_modo_claro]
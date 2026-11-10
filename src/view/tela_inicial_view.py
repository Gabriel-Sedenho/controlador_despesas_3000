import flet as ft
from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesas

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

        dados_usuario = self.pagina.session.store.get("usuario_logado")
        username = dados_usuario.get("login")
        titulo = ft.Text(value=f"Bem vindo(a) {username}!!!", color="#CFEEE6", size=30, font_family="Cascadia Code")

            


        self.controls = [titulo]
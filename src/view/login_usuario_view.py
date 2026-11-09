import flet as ft
from src.model.usuario_model import Usuario

class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
    
        self.pagina = pagina

        self.route ="/login"

        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#CFEEE6"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.width = 800
        self.height = 800

        titulo = ft.Text(value="Acesse sua conta", color="#0D0E10")

        self.login = ft.TextField(label="Login", border_color="#0D0E10", color="#0D0E10",)

        self.senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, border_color="#0D0E10", color="#0D0E10")

        self.controls = [titulo, self.login, self.senha]
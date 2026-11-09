import flet as ft
from src.model.usuario_model import Usuario

class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()
    
        self.pagina = pagina

        self.route = "/login"

        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.width = 800
        self.height = 800

        titulo = ft.Text(value="Acesse sua conta", color="#F0FFE3")

        self.login = ft.TextField(label="Login", label_style=ft.TextStyle(color="#CFEEE6"), border_color="#F0FFE3", color="#FFFFFF",)

        self.senha = ft.TextField(label="Senha", label_style=ft.TextStyle(color="#CFEEE6"), password=True, can_reveal_password=True, border_color="#F0FFE3", color="#FFFFFF")

        botao_login = ft.Button(content="Entrar", width=250, bgcolor="#28C39D", color="#CFEEE6")

        botao_cadastro = ft.Button(content="Não tem uma conta? Cadastre-se aqui!", width=350, bgcolor="#050607", color="#CFEEE6", on_click=self.ir_para_cadastro)

        self.controls = [titulo, self.login, self.senha, botao_login, botao_cadastro]

    async def ir_para_cadastro(self):
        await self.pagina.push_route("/cadastro")
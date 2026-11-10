import flet as ft
from src.model.usuario_model import Usuario

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/cadastro"

        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.width = 800
        self.height = 800

        titulo = ft.Text(value="Criar nova conta", color="#CFEEE6")

        self.login = ft.TextField(label="Login", label_style=ft.TextStyle(color="#CFEEE6"), border_color="#CFEEE6", color="#FFFFFF",)

        self.senha = ft.TextField(label="Senha", label_style=ft.TextStyle(color="#CFEEE6"), password=True, can_reveal_password=True, border_color="#CFEEE6", color="#FFFFFF")

        botao_cadastro = ft.Button(content="Cadastrar-se", width=250, on_click=self.cadastrar, bgcolor="#28C39D", color="#CFEEE6")

        botao_voltar = ft.TextButton(content="já tem uma conta? Entrar", style=ft.ButtonStyle(color="#CFEEE6"), on_click=self.ir_para_login)

        self.controls = [titulo, self.login, self.senha, botao_cadastro, botao_voltar]
    
    def cadastrar(self):
        usuario = self.login.value
        senha = self.senha.value
        if usuario == "" or senha == "":
            self.pagina.show_dialog(ft.SnackBar(ft.Text(value="Insira seu usuario e senha")))

        elif Usuario().cadastrar(usuario, senha):
            self.pagina.show_dialog(ft.SnackBar(ft.Text(value="Usuario Cadastrado")))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text(value="Falha ao Cadastrar")))

    async def ir_para_login(self):
        await self.pagina.push_route("/login")
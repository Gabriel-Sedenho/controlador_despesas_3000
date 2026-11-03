import flet as ft
from src.model.usuario_model import Usuario

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#ffffff"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.width = 800
        self.height = 800

        titulo = ft.Text(value="Criar nova conta")

        self.login = ft.TextField(label="Login", border_color="#01B7FF")

        self.senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, border_color="#01B7FF")

        botao_cadastro = ft.Button(content="Cadastrar-se", width=250, on_click=self.cadastrar)

        botao_voltar = ft.Button(content="Voltar", width=250)

        self.controls = [titulo, self.login, self.senha, botao_cadastro, botao_voltar]
    
    def cadastrar(self):
        usuario = self.login.value
        senha = self.senha.value
        Usuario().cadastrar(usuario, senha)
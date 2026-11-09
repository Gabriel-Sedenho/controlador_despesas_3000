import flet as ft
from src.model.usuario_model import Usuario

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/cadastro"

        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#CFEEE6"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"
        self.width = 800
        self.height = 800

        titulo = ft.Text(value="Criar nova conta", color="#0D0E10")

        self.login = ft.TextField(label="Login", border_color="#0D0E10", color="#0D0E10",)

        self.senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, border_color="#0D0E10", color="#0D0E10")

        botao_cadastro = ft.Button(content="Cadastrar-se", width=250, on_click=self.cadastrar, bgcolor="#5FD34A", color="#0D0E10")

        botao_voltar = ft.Button(content="Voltar para login", width=250, bgcolor="#5FD34A", color="#0D0E10")

        self.controls = [titulo, self.login, self.senha, botao_cadastro, botao_voltar]
    
    def cadastrar(self):
        usuario = self.login.value
        senha = self.senha.value
        if Usuario().cadastrar(usuario, senha):
            self.pagina.show_dialog(ft.SnackBar(ft.Text(value="Deu certo")))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text(value="deu errado")))
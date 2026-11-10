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

        titulo = ft.Text(value="Controlador de Despesas 3000!!!", color="#F0FFE3", size=30)

        subtitulo = ft.Text(value="Acesse sua conta para usar o app", color="#F0FFE3")

        self.login = ft.TextField(label="Login", label_style=ft.TextStyle(color="#CFEEE6"), border_color="#F0FFE3", color="#FFFFFF",)

        self.senha = ft.TextField(label="Senha", label_style=ft.TextStyle(color="#CFEEE6"), password=True, can_reveal_password=True, border_color="#F0FFE3", color="#FFFFFF")

        botao_entrar = ft.Button(content="Entrar", width=250, bgcolor="#28C39D", color="#CFEEE6", on_click=self.entrar)

        botao_cadastro = ft.TextButton(content="Não tem uma conta? Cadastre-se aqui!", style=ft.ButtonStyle(color="#CFEEE6"), on_click=self.ir_para_cadastro)

        self.controls = [titulo, subtitulo, self.login, self.senha, botao_entrar, botao_cadastro]

    async def entrar(self):
        usuario = self.login.value
        senha = self.senha.value

        res = Usuario().verificar(usuario, senha)

        if res:
            self.pagina.session.set("usuario_logado", res.get(usuario)) 
            await self.pagina.push_route("/inicio")
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text(value="Login ou senha incorretos")))
    
    async def ir_para_cadastro(self):
        await self.pagina.push_route("/cadastro")
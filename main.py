import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView


def main(pagina:ft.Page):
    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)

    def roteamento(e=None):
        pagina.views.clear()
        if pagina.route == "/login":
            pagina.views.append(tela_login_usuario)
        elif pagina.route == "/cadastro":
            pagina.views.appedn(tela_cadastro_usuario)

        pagina.update
        
    
    


ft.run(main)
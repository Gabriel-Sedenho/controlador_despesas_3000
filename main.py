import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.tela_inicial_view import InicioView


def main(pagina:ft.Page):
    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)
    tela_inicio = InicioView(pagina)

    def roteamento(e=None):
        pagina.views.clear()
        if pagina.route == "/login":
            pagina.views.append(tela_login_usuario)
        elif pagina.route == "/cadastro":
            pagina.views.append(tela_cadastro_usuario)
        elif pagina.route == "/inicio":
            pagina.views.append(tela_inicio)
        pagina.update

        
    pagina.on_route_change = roteamento
    roteamento()

    pagina.views.append(tela_login_usuario)
    


ft.run(main)
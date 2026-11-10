import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.tela_inicial_view import InicioView
from src.view.categoria_view import CadastroCategoriaView
from src.view.categoria import CategoriaView
from src.view.despesa import DespesaView
from src.view.despesa_view import DespesaMostrarView

def main(pagina:ft.Page):
    def navegacao(e):
        item_clicado = e.control.selected_index
        if item_clicado == 0:
            pagina.navigate("/categoriaview")
        if item_clicado ==1:
            pagina.navigate("/categoria")
        if item_clicado ==2:
            pagina.navigate("/despesas")
        if item_clicado ==3:
            pagina.navigate("/despesasview")
        if item_clicado ==4:
            pagina.navigate("/login")

    # tentando estilizar a barra de navegação de acordo com a paleta de cores da pagina
    pagina.theme = ft.Theme(
      navigation_bar_theme=ft.NavigationBarTheme(
        label_text_style={
          # Cor da letra quando o item NÃO está selecionado
          ft.ControlState.DEFAULT: ft.TextStyle(
            color="#CFEEE6", size=12
          ),
          # Cor da letra quando o item ESTÁ selecionado
          ft.ControlState.SELECTED: ft.TextStyle(
            color="#28C39D", size=14, weight=ft.FontWeight.BOLD
          ),
        }
      )
    )

    barra_navegação = ft.NavigationBar(destinations=[ft.NavigationBarDestination(icon=ft.Icons.CATEGORY, label="Categoria"),
                                                    ft.NavigationBarDestination(icon=ft.Icons.ADD_TASK, label="Nova despesa"),
                                                    ft.NavigationBarDestination(icon=ft.Icons.TASK_ALT, label="Todas as despesas"),
                                                    ft.NavigationBarDestination(icon=ft.Icons.TASK_SHARP, label="Despesas por categoria"),
                                                    ft.NavigationBarDestination(icon=ft.Icons.EXIT_TO_APP, label="Sair"),
                                                         ], on_change=navegacao, bgcolor="#0C3B2E", )
    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)
    tela_login_usuario.navigation_bar = barra_navegação
    tela_inicio = InicioView(pagina)
    cadastro_categoria = CadastroCategoriaView(pagina)
    categoria = CategoriaView(pagina)
    


    def roteamento(e=None):
        pagina.views.clear()
        if pagina.route == "/login":
            pagina.views.append(tela_login_usuario)
        elif pagina.route == "/cadastro":
            pagina.views.append(tela_cadastro_usuario)
        elif pagina.route == "/inicio":
            pagina.views.append(tela_inicio)
        elif pagina.route == "/categoriacadastro":
            pagina.views.append(cadastro_categoria)
        pagina.update

        
    pagina.on_route_change = roteamento
    roteamento()

    pagina.navigate("/login")
    


ft.run(main)
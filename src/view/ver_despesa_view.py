import flet as ft

from src.model.usuario_model import Usuario
from src.model.despesa_model import Despesas

class DespesaMostrarView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/despesas"

        self.width = 800
        self.height = 600
        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.vertical_alignment = "top"
        self.horizontal_alignment = "center"

        self.dados_usuario = pagina.session.store.get("usuario_logado")
        self.username = self.dados_usuario.get("login")

        self.lista_despesas = []

        titulo = ft.Text(value="Despesas",
                        color="#CFEEE6",
                        size=30)

        botao_ver_todos = ft.Button(content="ver todas as despesas", on_click=self.atualizar_todas)

        coluna = ft.Column(controls=self.lista_despesas)
        

        self.controls = [titulo, botao_ver_todos, coluna]

    def atualizar_todas(self):
        despesas = Despesas.recuperar_todos(self.username)

        for despesa in despesas:
            despesa_mostrada = despesa.get("descricao_despesa, dt_cadastro, valor")
            texto = ft.Text(value=despesa_mostrada, color="#0F7A62")
            botao = ft.Button(icon=ft.Icons.DELETE, bgcolor="#28C39D", color="#CFEEE6", key=despesa.get("id_despesa"), on_click=self.excluir)
            linha = ft.Row(controls=[texto, botao])
            
            self.lista_despesas.append(linha)

            self.pagina.update()
        
        self.pagina.update()

    def excluir(self, e):
        id_despesa = e.control.key
        Despesas.excluir(id_despesa)
        self.atualizar_todas
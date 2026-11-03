import flet as ft

class CadastrouUsuarioView(ft.View):
    def init(self, pagina:ft.Page):
        super().__init__()

        titulo = ft.Text(value="Criar nova conta")

        pagina.controls = [titulo]
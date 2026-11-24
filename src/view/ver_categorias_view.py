import flet as ft

from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria

class CategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()


        self.pagina = pagina
        self.route = "/categorias"

        self.width = 800
        self.height = 800
        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.vertical_alignment = "top"
        self.horizontal_alignment = "center"

        self.dados_usuario = pagina.session.store.get("usuario_logado")
        self.username = self.dados_usuario.get("login")

        titulo = ft.Text(value="Categorias",
                        color="#CFEEE6",
                        size=30)
        
        self.campo_nova_categoria = ft.TextField(label="Nome da categoria", color="#CFEEE6")

        botao_cadastrar = ft.Button(icon=ft.Icons.ADD, bgcolor="#28C39D", color="#CFEEE6", on_click=self.cadastrar_categoria, )

        linha = ft.Row(controls=[self.campo_nova_categoria, botao_cadastrar], width=400)
        
        self.lista_categorias = []

        titulo_categorias = ft.Text(value="Suas categorias", color="#CFEEE6", size=30)

        botao_atualizar = ft.Button(icon=ft.Icons.UPDATE, bgcolor="#28C39D", color="#CFEEE6", on_click=self.atualizar_lista_categorias)

        coluna = ft.Column(controls=self.lista_categorias)


        self.controls = [titulo, linha, titulo_categorias, botao_atualizar, coluna]

        
    def cadastrar_categoria(self):

        nome = self.campo_nova_categoria.value

        resultado = Categoria.adicionar(nome, self.username)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text(value="Categoria Cadastrada")))
            self.lista_categorias.clear()
            self.atualizar_lista_categorias()

        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text(value="Falha ao cadastrar")))
    
    def atualizar_lista_categorias(self):
        self.lista_categorias.clear()
        categorias = Categoria.recuperar_todos(self.username)

        for categoria in categorias:
            nome_categoria = categoria.get("nome_categoria")
            texto = ft.Text(value=nome_categoria, color="#0F7A62")
            botao = ft.Button(icon=ft.Icons.DELETE, bgcolor="#28C39D", color="#CFEEE6", key=categoria.get("id_categoria"), on_click=self.excluir)
            linha = ft.Row(controls=[texto, botao])
            
            self.lista_categorias.append(linha)

            self.pagina.update()

    def excluir(self, e):
        id_categoria = e.control.key
        Categoria().excluir(id_categoria)
        self.atualizar_lista_categorias()
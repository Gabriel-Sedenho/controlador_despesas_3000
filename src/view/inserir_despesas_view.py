import flet as ft

from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesas

class DespesaInserirView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/cadastrodespesas"

        self.width = 800
        self.height = 600
        self.title = "Controlador Despesas 3000"
        self.bgcolor = "#0D0E10"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        self.dados_usuario = pagina.session.store.get("usuario_logado")
        self.username = self.dados_usuario.get("login")
        categorias = Categoria.recuperar_todos(self.username)

        opcoes = []
        for categoria in categorias:
            opcoes.append(ft.DropdownOption(key=categoria.get("id_categoria"), text=categoria.get("nome_categoria")))

        
        ### código da tela ###
        titulo = ft.Text(value="Inserir Despesa",
                        color="#CFEEE6",
                        size=30)
        
        
        self.campo_descricao = ft.TextField(label="Descrição", color="#CFEEE6")

        self.campo_valor = ft.TextField(label="Valor da despesa", color="#CFEEE6", keyboard_type=ft.KeyboardType.NUMBER)

        self.campo_data = ft.TextField(label="data da despesa", color="#CFEEE6", keyboard_type=ft.KeyboardType.DATETIME)

        self.campo_categoria = ft.Dropdown(color="#CFEEE6" ,options=
            opcoes)

        botao_cadastrar = ft.Button(icon=ft.Icons.ADD, bgcolor="#28C39D", color="#CFEEE6")



        self.controls = [titulo, self.campo_descricao, self.campo_valor, self.campo_data, self.campo_categoria, botao_cadastrar]
        ### / ####

        # def adicionar_despesa(self):
        #     Despesas.incluir(, self.campo_descricao.value, self.campo_valor.value)

from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivy.uix.image import Image
from kivymd.uix.button import MDIconButton
from kivy.app import App



#=======================================================================================================================
# Tela com os jogos do nível Primario (Fundamental I)
class TelaJogar_Primario(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Fundo
        self.bg_image = Image(source='fundoapp.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg_image)

        # Engrenagem
        self.theme_button = MDIconButton(
            icon='cog',
            pos_hint={'right': 1, 'top': 1},
            on_release=self.toggle_theme
        )
        layout.add_widget(self.theme_button)

        # Título
        titulo = MDLabel(
            text="Primário\nSelecione o jogo que deseja jogar:",
            font_size=50,
            font_style='H4',
            halign="center",
            pos_hint={"center_x": 0.5, "top": 0.95},
            size_hint=(0.8, 0.2),
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        layout.add_widget(titulo)


        # Botão de voltar
        self.back_button = MDIconButton(
            icon='arrow-left', # Recomendo usar 'arrow-left' ou 'chevron-left' para setas de voltar
            pos_hint={'x': 0, 'top': 1},
            on_release=self.voltar
        )
        layout.add_widget(self.back_button) # <-- Mude aqui!


        # Parâmetros dos botões
        spacing_x = 0.3
        spacing_y = 0.2
        start_x = 0.2
        start_y = 0.7

        labels = [
            "Operações", "Frações", "Sudoku",
            "Memória", "Relógio", "Pares",
            "Contar", "Formas", "Quiz"
        ]

        imagens = [
            "matematicando.png", "fracoes.png", "desafios_logo.png",
            "memoria_logo.png", "relogio_logo.png", "pares_logo.png",
            "contar_logo.png", "formas_logo.png", "quiz_logo.png"
        ]

        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                pos = {
                    "center_x": start_x + j * spacing_x,
                    "center_y": start_y - i * spacing_y
                }

                # Botão com imagem
                card = MDCard(
                    size_hint=(0.15, 0.15),
                    pos_hint=pos,
                    on_release=lambda instance, idx=index: self.aciona_jogo(idx),
                    radius=[20, 20, 20, 20],
                    elevation=0,
                    md_bg_color=(0, 0, 0, 0),
                    ripple_behavior=True
                )

                img = Image(
                    source=imagens[index],
                    allow_stretch=True,
                    keep_ratio=True,
                    size_hint=(0.8, 0.8),
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )

                card.add_widget(img)
                layout.add_widget(card)

                # Rótulo
                label = MDLabel(
                    text=labels[index],
                    halign="center",
                    pos_hint={
                        "center_x": start_x + j * spacing_x,
                        "center_y": (start_y - i * spacing_y) - 0.09
                    },
                    size_hint=(0.15, 0.15),
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1)
                )
                layout.add_widget(label)

        self.add_widget(layout)

    def aciona_jogo(self, index):
        if index == 0:
            self.ir_para_modonormal()
        elif index == 1:  # Álgebra
            self.ir_para_fracoes()
        elif index == 2:  # Sudoku
            self.manager.current = "sudoku"
        else:
            print(f"Botão {index} pressionado.")

    def ir_para_modonormal(self):
        self.manager.current = "primario"

    def ir_para_fracoes(self):
        self.manager.current = "fracoes"

    def toggle_theme(self, *args):
        app = App.get_running_app()
        theme_cls = app.theme_cls
        theme_cls.theme_style = "Dark" if theme_cls.theme_style == "Light" else "Light"
        app.current_theme = theme_cls.theme_style
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

    def voltar(self, instance):
        self.manager.current = "seleciona"
#=======================================================================================================================

#=======================================================================================================================
# Tela com os jogos do nível Fundamental II
class TelaJogar_Fundamental(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Fundo
        self.bg_image = Image(source='fundoapp.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg_image)

        # Engrenagem
        self.theme_button = MDIconButton(
            icon='cog',
            pos_hint={'right': 1, 'top': 1},
            on_release=self.toggle_theme
        )
        layout.add_widget(self.theme_button)

        # Título
        titulo = MDLabel(
            text="Fundamental\nSelecione o jogo que deseja jogar:",
            font_size=50,
            font_style='H4',
            halign="center",
            pos_hint={"center_x": 0.5, "top": 0.95},
            size_hint=(0.8, 0.2),
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        layout.add_widget(titulo)

        # Botão de voltar
        self.back_button = MDIconButton(
            icon='arrow-left', # Recomendo usar 'arrow-left' ou 'chevron-left' para setas de voltar
            pos_hint={'x': 0, 'top': 1},
            on_release=self.voltar
        )
        layout.add_widget(self.back_button) # <-- Mude aqui!

        # Parâmetros dos botões
        spacing_x = 0.3
        spacing_y = 0.2
        start_x = 0.2
        start_y = 0.7

        labels = [
            "Operações", "Álgebra", "Fraçõse",
            "Memória", "Relógio", "Pares",
            "Contar", "Formas", "Quiz"
        ]

        imagens = [
            "matematicando.png", "algebra.png", "fracoes.png",
            "memoria_logo.png", "relogio_logo.png", "pares_logo.png",
            "contar_logo.png", "formas_logo.png", "quiz_logo.png"
        ]

        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                pos = {
                    "center_x": start_x + j * spacing_x,
                    "center_y": start_y - i * spacing_y
                }

                # Botão com imagem
                card = MDCard(
                    size_hint=(0.15, 0.15),
                    pos_hint=pos,
                    on_release=lambda instance, idx=index: self.aciona_jogo(idx),
                    radius=[20, 20, 20, 20],
                    elevation=0,
                    md_bg_color=(0, 0, 0, 0),
                    ripple_behavior=True
                )

                img = Image(
                    source=imagens[index],
                    allow_stretch=True,
                    keep_ratio=True,
                    size_hint=(0.8, 0.8),
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )

                card.add_widget(img)
                layout.add_widget(card)

                # Rótulo
                label = MDLabel(
                    text=labels[index],
                    halign="center",
                    pos_hint={
                        "center_x": start_x + j * spacing_x,
                        "center_y": (start_y - i * spacing_y) - 0.09
                    },
                    size_hint=(0.15, 0.15),
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1)
                )
                layout.add_widget(label)

        self.add_widget(layout)

    def aciona_jogo(self, index):
        if index == 0:
            self.ir_para_modonormal()
        elif index == 1:  # Álgebra
            self.ir_para_algebra()
        elif index == 2:  # Sudoku
            self.ir_para_fracoes()
        else:
            print(f"Botão {index} pressionado.")

    def ir_para_modonormal(self):
        self.manager.current = "fundamental"

    # Em TelaJogar_Fundamental
    def ir_para_algebra(self):
        self.manager.current = "algebra"
        algebra = self.manager.get_screen("algebra")
        # CORREÇÃO APLICADA AQUI:
        algebra.definir_dificuldade("Fundamental")

    def ir_para_fracoes(self):
        fracoes = self.manager.get_screen("fracoes")
        fracoes.definir_dificuldade("Fundamental")
        self.manager.current = "fracoes"

    def toggle_theme(self, *args):
        app = App.get_running_app()
        theme_cls = app.theme_cls
        theme_cls.theme_style = "Dark" if theme_cls.theme_style == "Light" else "Light"
        app.current_theme = theme_cls.theme_style
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

    def voltar(self, instance):
        self.manager.current = "seleciona"
#=======================================================================================================================

#=======================================================================================================================
# Tela com os jogos do nível Ensino Médio
class TelaJogar_Medio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Fundo
        self.bg_image = Image(source='fundoapp.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg_image)

        # Engrenagem
        self.theme_button = MDIconButton(
            icon='cog',
            pos_hint={'right': 1, 'top': 1},
            on_release=self.toggle_theme
        )
        layout.add_widget(self.theme_button)

        # Título
        titulo = MDLabel(
            text="Ensino Médio\nSelecione o jogo que deseja jogar:",
            font_size=50,
            font_style='H4',
            halign="center",
            pos_hint={"center_x": 0.5, "top": 0.95},
            size_hint=(0.8, 0.2),
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        layout.add_widget(titulo)

        # Botão de voltar
        self.back_button = MDIconButton(
            icon='arrow-left',
            pos_hint={'x': 0, 'top': 1},
            on_release=self.voltar
        )
        layout.add_widget(self.back_button)

        spacing_x = 0.3
        spacing_y = 0.2
        start_x = 0.2
        start_y = 0.7

        labels = [
            "Operações", "Álgebra", "Frações",
            "Memória", "Relógio", "Pares",
            "Contar", "Formas", "Quiz"
        ]

        imagens = [
            "matematicando.png", "algebra.png", "abc.png",
            "memoria_logo.png", "relogio_logo.png", "pares_logo.png",
            "contar_logo.png", "formas_logo.png", "quiz_logo.png"
        ]

        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                pos = {
                    "center_x": start_x + j * spacing_x,
                    "center_y": start_y - i * spacing_y
                }

                # Botão com imagem
                card = MDCard(
                    size_hint=(0.15, 0.15),
                    pos_hint=pos,
                    on_release=lambda instance, idx=index: self.aciona_jogo(idx),
                    radius=[20, 20, 20, 20],
                    elevation=0,
                    md_bg_color=(0, 0, 0, 0),
                    ripple_behavior=True
                )

                img = Image(
                    source=imagens[index],
                    allow_stretch=True,
                    keep_ratio=True,
                    size_hint=(0.8, 0.8),
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )

                card.add_widget(img)
                layout.add_widget(card)

                # Rótulo
                label = MDLabel(
                    text=labels[index],
                    halign="center",
                    pos_hint={
                        "center_x": start_x + j * spacing_x,
                        "center_y": (start_y - i * spacing_y) - 0.09
                    },
                    size_hint=(0.15, 0.15),
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1)
                )
                layout.add_widget(label)

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = "seleciona"

    def aciona_jogo(self, index):
        if index == 0:
            self.ir_para_modonormal()
        elif index == 1:  # Álgebra
            self.ir_para_algebra()
        else:
            print(f"Botão {index} pressionado.")

    def ir_para_modonormal(self):
        self.manager.current = "medio"

    def ir_para_fracoes(self):
        self.manager.current = "fracoes"
        fracoes = self.manager.get_screen("fracoes")
        fracoes.definir_dificuldade("Medio")

    # Em TelaJogar_Medio
    def ir_para_algebra(self):
        self.manager.current = "algebra"
        # CORREÇÃO APLICADA AQUI (descomentar e corrigir o nome):
        algebra = self.manager.get_screen("algebra")
        algebra.definir_dificuldade("Medio")

    def toggle_theme(self, *args):
        app = App.get_running_app()
        theme_cls = app.theme_cls
        theme_cls.theme_style = "Dark" if theme_cls.theme_style == "Light" else "Light"
        app.current_theme = theme_cls.theme_style
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"
#=======================================================================================================================



#CLASSES ABAIXO SÃO PARA ESCOLHA DO NÍVEL DO MATEMATICANDO
#Acho que posso simplificar numa única classe que só mudará a variável dificuldade mesmo
class Primario(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        self.bg_image = Image(source='fundoapp.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg_image)

        self.theme_button = MDIconButton(
            icon='cog',
            pos_hint={'right': 1, 'top': 1},
            on_release=self.toggle_theme
        )
        layout.add_widget(self.theme_button)

        title = MDLabel(
            text="Fundamental I",
            halign="center",
            font_style="H4",
            size_hint=(0.8, None),
            height=50,
            pos_hint={"center_x": 0.5, "top": 0.9},
            text_color=(1, 0.8, 0, 1),
        )
        layout.add_widget(title)

        # Título da seção de rodadas
        rodadas_text = MDLabel(
            text="Quantas rodadas você deseja\n jogar em cada nível?",
            halign="center",
            font_size="20",
            size_hint=(0.6, None),
            height=50,
            pos_hint={"center_x": 0.3, "top": 0.8},
        )
        layout.add_widget(rodadas_text)

        # Botões de escolha de rodadas (lado esquerdo)
        self.button_3 = self.create_rodada_button("3 Rodadas", 0.7, 3)
        self.button_6 = self.create_rodada_button("6 Rodadas", 0.625, 6)
        self.button_10 = self.create_rodada_button("10 Rodadas", 0.55, 10)
        self.button_3.pos_hint["center_x"] = 0.3
        self.button_6.pos_hint["center_x"] = 0.3
        self.button_10.pos_hint["center_x"] = 0.3
        layout.add_widget(self.button_3)
        layout.add_widget(self.button_6)
        layout.add_widget(self.button_10)

        # Título da seção de operações
        operacoes_text = MDLabel(
            text="Escolha a operação:",
            halign="center",
            font_size="20",
            size_hint=(0.6, None),
            height=50,
            pos_hint={"center_x": 0.7, "top": 0.8},
        )
        layout.add_widget(operacoes_text)

        # Botões de operação (lado direito)
        self.op_soma = self.create_operacao_button("+ Soma", 0.7, "soma")
        self.op_subtracao = self.create_operacao_button("- Subtração", 0.625, "subtracao")
        self.op_multiplicacao = self.create_operacao_button("× Multiplicação", 0.55, "multiplicacao")
        self.op_divisao = self.create_operacao_button("÷ Divisão", 0.475, "divisao")
        self.op_soma.pos_hint["center_x"] = 0.7
        self.op_subtracao.pos_hint["center_x"] = 0.7
        self.op_multiplicacao.pos_hint["center_x"] = 0.7
        self.op_divisao.pos_hint["center_x"] = 0.7
        layout.add_widget(self.op_soma)
        layout.add_widget(self.op_subtracao)
        layout.add_widget(self.op_multiplicacao)
        layout.add_widget(self.op_divisao)

        # Botão iniciar (liberado quando rodada e operação forem escolhidas)
        self.calculos_button = MDRaisedButton(
            text="Iniciar Partida",
            size_hint=(0.3, 0.1),
            height=50,
            font_size="24sp",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.ir_calculos_fundamental_i,
            md_bg_color=(0.5, 0.5, 0.5, 1),
            text_color=(1, 1, 1, 0.5),
            disabled=True
        )
        layout.add_widget(self.calculos_button)

        # Botão voltar
        voltar_button = MDRaisedButton(
            text="Voltar",
            size_hint=(0.3, 0.1),
            height=50,
            font_size="24sp",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_release=self.voltar_tela_inicial,
            md_bg_color=(0.5, 0.5, 0.5, 1),
            text_color=(1, 1, 1, 1),
        )
        layout.add_widget(voltar_button)

        self.add_widget(layout)

        # Variáveis de estado
        self.botao_selecionado = None
        self.operacao_selecionada = None

    def voltar_tela_inicial(self, instance):
        self.manager.current = "normal"

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        if hasattr(self, 'bg_image'):
            self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"



    def create_rodada_button(self, text, center_y, rodadas_value):
        return MDRaisedButton(
            text=text,
            size_hint=(0.2, 0.05),
            height=50,
            font_size="24sp",
            pos_hint={"center_y": center_y},
            on_release=lambda x: self.definir_rodadas(rodadas_value),
            md_bg_color=(0.2, 0.6, 0.8, 1),
            text_color=(1, 1, 1, 1),
        )

    def create_operacao_button(self, text, center_y, operacao_value):
        return MDRaisedButton(
            text=text,
            size_hint=(0.35, 0.05),
            height=50,
            font_size="20sp",
            pos_hint={"center_y": center_y},
            on_release=lambda x: self.definir_operacao(operacao_value),
            md_bg_color=(0.4, 0.4, 0.6, 1),
            text_color=(1, 1, 1, 1),
        )

    def definir_rodadas(self, rodadas_value):
        self.valor_rodadas = rodadas_value
        self.botao_selecionado = {
            3: self.button_3,
            6: self.button_6,
            10: self.button_10
        }[rodadas_value]

        for btn in [self.button_3, self.button_6, self.button_10]:
            btn.md_bg_color = (0.2, 0.6, 0.8, 1)
        self.botao_selecionado.md_bg_color = (0, 0.8, 0.4, 1)

        self.verificar_pronto()

    def definir_operacao(self, operacao_value):
        self.operacao_selecionada = operacao_value

        botoes = {
            "soma": self.op_soma,
            "subtracao": self.op_subtracao,
            "multiplicacao": self.op_multiplicacao,
            "divisao": self.op_divisao
        }

        for btn in botoes.values():
            btn.md_bg_color = (0.4, 0.4, 0.6, 1)
        botoes[operacao_value].md_bg_color = (0, 0.8, 0.4, 1)

        self.verificar_pronto()

    def verificar_pronto(self):
        if hasattr(self, 'valor_rodadas') and self.operacao_selecionada:
            self.calculos_button.disabled = False
            self.calculos_button.md_bg_color = (0, 0.6, 0, 1)
            self.calculos_button.text_color = (1, 1, 1, 1)

    def ir_calculos_fundamental_i(self, instance):
        self.manager.current = "game1"
        game1 = self.manager.get_screen("game1")
        game1.define_dificul("primario")
        game1.confirma_rodadas(self.valor_rodadas)
        game1.escolha_modo("normal")
        game1.define_operacao(self.operacao_selecionada.lower())
        game1.inicia_nivel(1)

    def toggle_theme(self, *args):
        app = App.get_running_app()
        theme_cls = app.theme_cls
        if theme_cls.theme_style == "Light":
            theme_cls.theme_style = "Dark"
            app.current_theme = "Dark"
        else:
            theme_cls.theme_style = "Light"
            app.current_theme = "Light"

        # Atualiza o fundo com base no novo tema
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

class Fundamental(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        self.bg_image = Image(source='fundoapp.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg_image)

        self.theme_button = MDIconButton(
            icon='cog',
            pos_hint={'right': 1, 'top': 1},
            on_release=self.toggle_theme
        )
        layout.add_widget(self.theme_button)

        title = MDLabel(
            text="Fundamental II",
            halign="center",
            font_style="H4",
            size_hint=(0.8, None),
            height=50,
            pos_hint={"center_x": 0.5, "top": 0.9},
            text_color=(1, 0.8, 0, 1),
        )
        layout.add_widget(title)

        rodadas_text = MDLabel(
            text="Quantas rodadas você deseja\n jogar em cada nível?",
            halign="center",
            font_size="20",
            size_hint=(0.6, None),
            height=50,
            pos_hint={"center_x": 0.3, "top": 0.8},
        )
        layout.add_widget(rodadas_text)

        self.button_3 = self.create_rodada_button("3 Rodadas", 0.7, 3)
        self.button_6 = self.create_rodada_button("6 Rodadas", 0.625, 6)
        self.button_10 = self.create_rodada_button("10 Rodadas", 0.55, 10)
        for btn in [self.button_3, self.button_6, self.button_10]:
            btn.pos_hint["center_x"] = 0.3
            layout.add_widget(btn)

        operacoes_text = MDLabel(
            text="Escolha a operação:",
            halign="center",
            font_size="20",
            size_hint=(0.6, None),
            height=50,
            pos_hint={"center_x": 0.7, "top": 0.8},
        )
        layout.add_widget(operacoes_text)

        self.op_soma = self.create_operacao_button("+ Soma", 0.7, "soma")
        self.op_subtracao = self.create_operacao_button("- Subtração", 0.625, "subtracao")
        self.op_multiplicacao = self.create_operacao_button("× Multiplicação", 0.55, "multiplicacao")
        self.op_divisao = self.create_operacao_button("÷ Divisão", 0.475, "divisao")
        for btn in [self.op_soma, self.op_subtracao, self.op_multiplicacao, self.op_divisao]:
            btn.pos_hint["center_x"] = 0.7
            layout.add_widget(btn)

        self.calculos_button = MDRaisedButton(
            text="Iniciar Partida",
            size_hint=(0.3, 0.1),
            height=50,
            font_size="24sp",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.ir_calculos_fundamental,
            md_bg_color=(0.5, 0.5, 0.5, 1),
            text_color=(1, 1, 1, 0.5),
            disabled=True
        )
        layout.add_widget(self.calculos_button)

        voltar_button = MDRaisedButton(
            text="Voltar",
            size_hint=(0.3, 0.1),
            height=50,
            font_size="24sp",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_release=self.voltar_tela_inicial,
            md_bg_color=(0.5, 0.5, 0.5, 1),
            text_color=(1, 1, 1, 1),
        )
        layout.add_widget(voltar_button)

        self.add_widget(layout)
        self.botao_selecionado = None
        self.operacao_selecionada = None

    def voltar_tela_inicial(self, instance):
        self.manager.current = "jogar"

    def toggle_theme(self, *args):
        app = App.get_running_app()
        theme_cls = app.theme_cls
        if theme_cls.theme_style == "Light":
            theme_cls.theme_style = "Dark"
            app.current_theme = "Dark"
        else:
            theme_cls.theme_style = "Light"
            app.current_theme = "Light"

        # Atualiza o fundo com base no novo tema
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

    def create_rodada_button(self, text, center_y, rodadas_value):
        return MDRaisedButton(
            text=text,
            size_hint=(0.2, 0.05),
            height=50,
            font_size="24sp",
            pos_hint={"center_y": center_y},
            on_release=lambda x: self.definir_rodadas(rodadas_value),
            md_bg_color=(0.2, 0.6, 0.8, 1),
            text_color=(1, 1, 1, 1),
        )

    def create_operacao_button(self, text, center_y, operacao_value):
        return MDRaisedButton(
            text=text,
            size_hint=(0.35, 0.05),
            height=50,
            font_size="20sp",
            pos_hint={"center_y": center_y},
            on_release=lambda x: self.definir_operacao(operacao_value),
            md_bg_color=(0.4, 0.4, 0.6, 1),
            text_color=(1, 1, 1, 1),
        )

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        if hasattr(self, 'bg_image'):
            self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

    def definir_rodadas(self, rodadas_value):
        self.valor_rodadas = rodadas_value
        self.botao_selecionado = {
            3: self.button_3,
            6: self.button_6,
            10: self.button_10
        }[rodadas_value]
        for btn in [self.button_3, self.button_6, self.button_10]:
            btn.md_bg_color = (0.2, 0.6, 0.8, 1)
        self.botao_selecionado.md_bg_color = (0, 0.8, 0.4, 1)
        self.verificar_pronto()

    def definir_operacao(self, operacao_value):
        self.operacao_selecionada = operacao_value
        botoes = {
            "soma": self.op_soma,
            "subtracao": self.op_subtracao,
            "multiplicacao": self.op_multiplicacao,
            "divisao": self.op_divisao
        }
        for btn in botoes.values():
            btn.md_bg_color = (0.4, 0.4, 0.6, 1)
        botoes[operacao_value].md_bg_color = (0, 0.8, 0.4, 1)
        self.verificar_pronto()

    def verificar_pronto(self):
        if hasattr(self, 'valor_rodadas') and self.operacao_selecionada:
            self.calculos_button.disabled = False
            self.calculos_button.md_bg_color = (0, 0.6, 0, 1)
            self.calculos_button.text_color = (1, 1, 1, 1)

    def ir_calculos_fundamental(self, instance):
        self.manager.current = "game1"
        game1 = self.manager.get_screen("game1")
        game1.define_dificul("fundamental")
        game1.confirma_rodadas(self.valor_rodadas)
        game1.escolha_modo("normal")
        game1.define_operacao(self.operacao_selecionada.lower())
        game1.inicia_nivel(1)

class Medio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        self.bg_image = Image(source='fundoapp.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg_image)

        self.theme_button = MDIconButton(
            icon='cog',
            pos_hint={'right': 1, 'top': 1},
            on_release=self.toggle_theme
        )
        layout.add_widget(self.theme_button)

        title = MDLabel(
            text="Ensino Médio",
            halign="center",
            font_style="H4",
            size_hint=(0.8, None),
            height=50,
            pos_hint={"center_x": 0.5, "top": 0.9},
            text_color=(1, 0.8, 0, 1),
        )
        layout.add_widget(title)

        rodadas_text = MDLabel(
            text="Quantas rodadas você deseja \njogar em cada nível?",
            halign="center",
            font_size="20",
            size_hint=(0.6, None),
            height=50,
            pos_hint={"center_x": 0.3, "top": 0.8},
        )
        layout.add_widget(rodadas_text)

        self.button_3 = self.create_rodada_button("3 Rodadas", 0.7, 3)
        self.button_6 = self.create_rodada_button("6 Rodadas", 0.625, 6)
        self.button_10 = self.create_rodada_button("10 Rodadas", 0.55, 10)
        for btn in [self.button_3, self.button_6, self.button_10]:
            btn.pos_hint["center_x"] = 0.3
            layout.add_widget(btn)

        operacoes_text = MDLabel(
            text="Escolha a operação:",
            halign="center",
            font_size="20",
            size_hint=(0.6, None),
            height=50,
            pos_hint={"center_x": 0.7, "top": 0.8},
        )
        layout.add_widget(operacoes_text)

        self.op_soma = self.create_operacao_button("+ Soma", 0.7, "soma")
        self.op_subtracao = self.create_operacao_button("- Subtração", 0.625, "subtracao")
        self.op_multiplicacao = self.create_operacao_button("× Multiplicação", 0.55, "multiplicacao")
        self.op_divisao = self.create_operacao_button("÷ Divisão", 0.475, "divisao")
        for btn in [self.op_soma, self.op_subtracao, self.op_multiplicacao, self.op_divisao]:
            btn.pos_hint["center_x"] = 0.7
            layout.add_widget(btn)

        self.calculos_button = MDRaisedButton(
            text="Iniciar Partida",
            size_hint=(0.3, 0.1),
            height=50,
            font_size="24sp",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.ir_calculos_fundamental,
            md_bg_color=(0.5, 0.5, 0.5, 1),
            text_color=(1, 1, 1, 0.5),
            disabled=True
        )
        layout.add_widget(self.calculos_button)

        voltar_button = MDRaisedButton(
            text="Voltar",
            size_hint=(0.3, 0.1),
            height=50,
            font_size="24sp",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_release=self.voltar_tela_inicial,
            md_bg_color=(0.5, 0.5, 0.5, 1),
            text_color=(1, 1, 1, 1),
        )
        layout.add_widget(voltar_button)

        self.add_widget(layout)
        self.botao_selecionado = None
        self.operacao_selecionada = None

    def voltar_tela_inicial(self, instance):
        self.manager.current = "jogar"


    def toggle_theme(self, *args):
        app = App.get_running_app()
        theme_cls = app.theme_cls
        if theme_cls.theme_style == "Light":
            theme_cls.theme_style = "Dark"
            app.current_theme = "Dark"
        else:
            theme_cls.theme_style = "Light"
            app.current_theme = "Light"

        # Atualiza o fundo com base no novo tema
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

    def create_rodada_button(self, text, center_y, rodadas_value):
        return MDRaisedButton(
            text=text,
            size_hint=(0.2, 0.05),
            height=50,
            font_size="24sp",
            pos_hint={"center_y": center_y},
            on_release=lambda x: self.definir_rodadas(rodadas_value),
            md_bg_color=(0.2, 0.6, 0.8, 1),
            text_color=(1, 1, 1, 1),
        )

    def create_operacao_button(self, text, center_y, operacao_value):
        return MDRaisedButton(
            text=text,
            size_hint=(0.35, 0.05),
            height=50,
            font_size="20sp",
            pos_hint={"center_y": center_y},
            on_release=lambda x: self.definir_operacao(operacao_value),
            md_bg_color=(0.4, 0.4, 0.6, 1),
            text_color=(1, 1, 1, 1),
        )

    def definir_rodadas(self, rodadas_value):
        self.valor_rodadas = rodadas_value
        self.botao_selecionado = {
            3: self.button_3,
            6: self.button_6,
            10: self.button_10
        }[rodadas_value]
        for btn in [self.button_3, self.button_6, self.button_10]:
            btn.md_bg_color = (0.2, 0.6, 0.8, 1)
        self.botao_selecionado.md_bg_color = (0, 0.8, 0.4, 1)
        self.verificar_pronto()

    def definir_operacao(self, operacao_value):
        self.operacao_selecionada = operacao_value
        botoes = {
            "soma": self.op_soma,
            "subtracao": self.op_subtracao,
            "multiplicacao": self.op_multiplicacao,
            "divisao": self.op_divisao
        }
        for btn in botoes.values():
            btn.md_bg_color = (0.4, 0.4, 0.6, 1)
        botoes[operacao_value].md_bg_color = (0, 0.8, 0.4, 1)
        self.verificar_pronto()

    def verificar_pronto(self):
        if hasattr(self, 'valor_rodadas') and self.operacao_selecionada:
            self.calculos_button.disabled = False
            self.calculos_button.md_bg_color = (0, 0.6, 0, 1)
            self.calculos_button.text_color = (1, 1, 1, 1)

    def ir_calculos_fundamental(self, instance):
        self.manager.current = "game1"
        game1 = self.manager.get_screen("game1")
        game1.define_dificul("medio")
        game1.confirma_rodadas(self.valor_rodadas)
        game1.escolha_modo("normal")
        game1.define_operacao(self.operacao_selecionada.lower())
        game1.inicia_nivel(1)


    def toggle_theme(self, *args):
        app = App.get_running_app()
        theme_cls = app.theme_cls
        if theme_cls.theme_style == "Light":
            theme_cls.theme_style = "Dark"
            app.current_theme = "Dark"
        else:
            theme_cls.theme_style = "Light"
            app.current_theme = "Light"

        # Atualiza o fundo com base no novo tema
        self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"

    def on_pre_enter(self, *args):
        app = App.get_running_app()
        if hasattr(self, 'bg_image'):
            self.bg_image.source = "escuro.png" if app.current_theme == "Dark" else "fundoapp.png"
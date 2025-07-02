# gui.py
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.core.text import LabelBase
from kivy.app import App

from kivy.uix.image import Image
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDIconButton

#=======================================================================================================================
# Classe que vai organizar os temas do jogo, escuro ou claro
class ThemeManagerMixin:
    layout = FloatLayout()
    def setup_background_and_theme_button(self, layout):
        self.bg_image = Image(source='fundoapp.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg_image)


        self.theme_button = MDIconButton(
            icon="cog",
            pos_hint={"right": 1, "top": 1},
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            on_release=self.toggle_theme
        )
        layout.add_widget(self.theme_button)

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


    def atualizar_fundos(self):
        app = App.get_running_app()
        theme = app.current_theme
        manager = self.manager if hasattr(self, 'manager') else None
        if manager:
            for screen in manager.screens:
                if hasattr(screen, 'bg_image'):
                    screen.bg_image.source = "escuro.png" if theme == "Dark" else "fundoapp.png"
#=======================================================================================================================



LabelBase.register(name="Lemonada", fn_regular="arial.ttf")

#=======================================================================================================================
# Tela inicial, com as opções jogar, e sair e serão adicionados "desenvolvedores" e "Como jogar"
class TelaInicial(Screen, ThemeManagerMixin):
    def __init__(self, **kwargs):
        
        # Informações Básicas
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.setup_background_and_theme_button(layout)

        title = MDLabel(
            text="MATEMATICANDO",
            halign="center",
            font_style="H3",
            size_hint=(0.8, None),
            height=30,
            pos_hint={"center_x": 0.5, "top": 0.9},
            theme_text_color="Custom",
            text_color=(1, 0.8, 0, 1),  # Dourado
            font_name="Lemonada"
        )
        layout.add_widget(title)
        self.animate_title(title)


        # Botões de menu
        layout.add_widget(self.create_button("JOGAR", 0.6, self.ir_para_selecao, (0, 0.6, 0, 1)))
        layout.add_widget(self.create_button("SAIR", 0.2, self.sair_app, (1, 0.3, 0.3, 1)))

        self.add_widget(layout)


    def animate_title(self, label):
        anim = Animation(opacity=0.7, duration=1) + Animation(opacity=1, duration=1)
        anim.repeat = True
        anim.start(label)

    def create_button(self, text, center_y, callback, color, width=0.3):
        return MDRaisedButton(
            text=text,
            size_hint=(width, 0.1),
            height=50,
            font_size="24sp",
            pos_hint={"center_x": 0.5, "center_y": center_y},
            on_release=lambda x: callback(),
            md_bg_color=color,
            text_color=(1, 1, 1, 1)
        )

    # Funções dos botões
    def ir_para_selecao(self):
        self.manager.current = "seleciona"

    def sair_app(self):
        App.get_running_app().stop()
#=======================================================================================================================


#=======================================================================================================================
# Tela que vai selecionar o nível e consequentemente os jogos que irão aparecer, no caso, depende do nível escolhido
class Seleciona_Nivel(Screen, ThemeManagerMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.layout=FloatLayout()
        self.setup_background_and_theme_button(layout)

        title = MDLabel(
            text="Selecione o nível dos jogos que deseja:",
            halign="center",
            font_style="H4",
            size_hint=(0.8, None),
            height=30,
            pos_hint={"center_x": 0.5, "top": 0.9},
            theme_text_color="Custom",
            text_color=(1, 0.8, 0, 1),  # Dourado
            font_name="Lemonada"
        )
        layout.add_widget(title)
        self.animate_title(title)

        # Botões de menu
        layout.add_widget(self.create_button("Primário", 0.65, self.ir_para_jogar_p, (0, 0.6, 0, 1)))
        layout.add_widget(self.create_button("Fundamental", 0.5, self.ir_para_jogar_f, (0, 0.6, 0, 1)))
        layout.add_widget(self.create_button("Ensino Médio", 0.35, self.ir_para_jogar, (0, 0.6, 0, 1)))

        # Botão de voltar
        back_button = MDIconButton(
            icon='arrow-left',
            pos_hint={'x': 0, 'top': 1},
            on_release=self.voltar
        )
        layout.add_widget(back_button)

        self.add_widget(layout)

    def animate_title(self, label):
        anim = Animation(opacity=0.7, duration=1) + Animation(opacity=1, duration=1)
        anim.repeat = True
        anim.start(label)

    def create_button(self, text, center_y, callback, color, width=0.3):
        return MDRaisedButton(
            text=text,
            size_hint=(width, 0.1),
            height=50,
            font_size="24sp",
            pos_hint={"center_x": 0.5, "center_y": center_y},
            on_release=lambda x: callback(),
            md_bg_color=color,
            text_color=(1, 1, 1, 1)
        )

    # Funções dos botões
    def ir_para_jogar_p(self):
        self.manager.current = "jogar_p"

    # Funções dos botões
    def ir_para_jogar_f(self):
        self.manager.current = "jogar_f"

    # Funções dos botões
    def ir_para_jogar(self):
        self.manager.current = "jogar"

    def voltar(self, instance):
        self.manager.current = "inicial"
#=======================================================================================================================



#=======================================================================================================================
# Importa apenas o necessário
from jogar import TelaJogar_Primario, Fundamental, Medio, Primario, TelaJogar_Medio, TelaJogar_Fundamental
from calculo import calculoI, TelaFimDeJogo
from algebra import AlgebraGameScreen, TelaFimAlgebra
from fracoes import FracoesGameScreen, TelaFimFracoes
#=======================================================================================================================


#=======================================================================================================================
# Classe que organiza a passagem de telas, devem ser importadas as classes do arquivo e aqui deve ser atribuído um nome
class AppGUI:
    def build_gui(self):
        sm = ScreenManager()
        sm.add_widget(TelaInicial(name="inicial"))
        sm.add_widget(TelaJogar_Primario(name="jogar_p"))
        sm.add_widget(TelaJogar_Fundamental(name="jogar_f"))
        sm.add_widget(TelaJogar_Medio(name="jogar"))
        sm.add_widget(Primario(name="primario"))
        sm.add_widget(Fundamental(name="fundamental"))
        sm.add_widget(Medio(name="medio"))
        sm.add_widget(calculoI(name="game1"))                   #Tela do jogo matematicando
        sm.add_widget(AlgebraGameScreen(name="algebra"))        #Tela do jogo de algebra
        sm.add_widget(TelaFimAlgebra(name="fim_algebra"))
        sm.add_widget(Seleciona_Nivel(name="seleciona"))
        sm.add_widget(TelaFimDeJogo(name="fim_de_jogo"))
        sm.add_widget(FracoesGameScreen(name="fracoes"))        #Tela do jogo das frações
        sm.add_widget(TelaFimFracoes(name="fim_fracoes"))
        return sm
#=======================================================================================================================

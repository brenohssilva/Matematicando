from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.core.text import LabelBase
from kivy.app import App
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivymd.uix.card import MDCard
from kivy.clock import Clock

LabelBase.register(name="Lemonada", fn_regular="arial.ttf")
LabelBase.register(name="ComicNeue", fn_regular="ComicNeue-Regular.ttf")

# Classe que organiza tema e fundo
class ThemeManagerMixin:
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
        theme_cls.theme_style = "Dark" if theme_cls.theme_style == "Light" else "Light"
        app.current_theme = theme_cls.theme_style
        self.bg_image.source = "escuro.png" if theme_cls.theme_style == "Dark" else "fundoapp.png"

    def atualizar_fundos(self):
        app = App.get_running_app()
        theme = app.current_theme
        manager = self.manager if hasattr(self, 'manager') else None
        if manager:
            for screen in manager.screens:
                if hasattr(screen, 'bg_image'):
                    screen.bg_image.source = "escuro.png" if theme == "Dark" else "fundoapp.png"



from kivy.uix.behaviors import ButtonBehavior
class BotaoImagem(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_stretch = True
        self.keep_ratio = False




# Registra a fonte de giz
class TelaInicial(Screen, ThemeManagerMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.setup_background(layout)

        # Título estilo giz colorido
        self.title_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 0.7, 1),  # Amarelo giz
            font_style="H4",
            font_name="ChalkFont",
            size_hint=(1, None),
            height=80,
            pos_hint={"center_x": 0.5, "top": 0.95}
        )
        layout.add_widget(self.title_label)
        self.digita_texto(self.title_label, "MATEMATICANDO")

        # Botão JOGAR (azul)
        jogar = MDRaisedButton(
            text="JOGAR",
            md_bg_color=(0, 0, 0, 0),
            text_color=(0.5, 0.7, 1.0, 1),  # Azul giz
            line_color=(0.5, 0.7, 1.0, 1),
            font_name="ChalkFont",
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            font_size=28,
            size_hint=(0.35, 0.1)
        )
        jogar.bind(on_release=lambda *args: [self.tocar_som_giz(), self.ir_para_selecao()])
        layout.add_widget(jogar)

        # Botão INFORMAÇÕES (verde)
        info = MDRaisedButton(
            text="INFORMAÇÕES",
            md_bg_color=(0, 0, 0, 0),
            text_color=(0.6, 1.0, 0.6, 1),  # Verde giz
            line_color=(0.6, 1.0, 0.6, 1),
            font_name="ChalkFont",
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            font_size=28,
            size_hint=(0.35, 0.1)
        )
        info.bind(on_release=lambda *args: [self.tocar_som_giz(), self.mostrar_info()])
        layout.add_widget(info)

        # Botão DESENVOLVEDORES (rosa)
        devs = MDRaisedButton(
            text="DESENVOLVEDORES",
            md_bg_color=(0, 0, 0, 0),
            text_color=(1.0, 0.6, 0.8, 1),  # Rosa giz
            line_color=(1.0, 0.6, 0.8, 1),
            font_name="ChalkFont",
            font_size=28,
            pos_hint={"center_x": 0.5, "center_y": 0.25},
            size_hint=(0.35, 0.1)
        )
        devs.bind(on_release=lambda *args: [self.tocar_som_giz(), self.mostrar_dev()])
        layout.add_widget(devs)

        self.add_widget(layout)

    def setup_background(self, layout):
        background = Image(
            source="quadro.png",  # imagem do quadro
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        layout.add_widget(background)

    def digita_texto(self, label, texto, i=0):
        if i <= len(texto):
            label.text = texto[:i]
            Clock.schedule_once(lambda dt: self.digita_texto(label, texto, i+1), 0.05)

    def tocar_som_giz(self):
        som = SoundLoader.load("giz_riscando.wav")
        if som:
            som.play()

    def ir_para_selecao(self):
        self.manager.current = "seleciona"

    def mostrar_dev(self):
        print("NÃO IMPLEMENTADO AINDA")

    def mostrar_info(self):
        print("NÃO IMPLEMENTADO AINDA")


LabelBase.register(name="ChalkFont", fn_regular="ChalkBoard.ttf")


#classe do quadro



class Seleciona_Nivel(Screen, ThemeManagerMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.setup_background_and_theme_button(layout)

        title = MDLabel(
            text="Selecione o nível dos jogos que deseja:",
            halign="center",
            font_style="H4",
            size_hint=(0.8, None),
            height=30,
            pos_hint={"center_x": 0.5, "top": 0.9},
            theme_text_color="Custom",
            text_color=(1, 0.8, 0, 1),
            font_name="ComicNeue"
        )
        layout.add_widget(title)
        self.animate_title(title)

        layout.add_widget(self.create_card_button("Primário", 0.65, self.ir_para_jogar_p, (0.2, 0.6, 1, 1)))
        layout.add_widget(self.create_card_button("Fundamental", 0.5, self.ir_para_jogar_f, (0.3, 0.7, 0.3, 1)))
        layout.add_widget(self.create_card_button("Ensino Médio", 0.35, self.ir_para_jogar, (0.6, 0.3, 0.6, 1)))

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

    def create_card_button(self, text, center_y, callback, color, width=0.3):
        card = MDCard(
            size_hint=(width, 0.1),
            pos_hint={"center_x": 0.5, "center_y": center_y},
            md_bg_color=color,
            radius=[20],
            elevation=10,
            ripple_behavior=True
        )

        label = MDLabel(
            text=text,
            halign="center",
            valign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_size="20sp",
            font_name="ComicNeue"
        )

        card.add_widget(label)
        card.on_release = lambda *a: callback()
        return card

    def ir_para_jogar_p(self):
        self.manager.transition = SlideTransition(direction="left", duration=0.4)
        self.manager.current = "jogar_p"

    def ir_para_jogar_f(self):
        self.manager.transition = SlideTransition(direction="left", duration=0.4)
        self.manager.current = "jogar_f"

    def ir_para_jogar(self):
        self.manager.transition = SlideTransition(direction="left", duration=0.4)
        self.manager.current = "jogar"

    def voltar(self, instance):
        self.manager.transition = SlideTransition(direction="right", duration=0.4)
        self.manager.current = "inicial"

# Organizador de telas
from jogar import TelaJogar_Primario, Fundamental, Medio, Primario, TelaJogar_Medio, TelaJogar_Fundamental
from calculo import calculoI, TelaFimDeJogo
from algebra import AlgebraGameScreen, TelaFimAlgebra
from fracoes import FracoesGameScreen, TelaFimFracoes

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
        sm.add_widget(calculoI(name="game1"))
        sm.add_widget(AlgebraGameScreen(name="algebra"))
        sm.add_widget(TelaFimAlgebra(name="fim_algebra"))
        sm.add_widget(Seleciona_Nivel(name="seleciona"))
        sm.add_widget(TelaFimDeJogo(name="fim_de_jogo"))
        sm.add_widget(FracoesGameScreen(name="fracoes"))
        sm.add_widget(TelaFimFracoes(name="fim_fracoes"))
        return sm

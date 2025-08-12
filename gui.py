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
from kivy.uix.behaviors import ButtonBehavior

LabelBase.register(name="Lemonada", fn_regular="arial.ttf")
LabelBase.register(name="ComicNeue", fn_regular="ComicNeue-Regular.ttf")

# Classe que organiza tema e fundo
class ThemeManagerMixin:
    def setup_background_and_theme_button(self, layout):
        self.bg_image = Image(source='fundoapp.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg_image)

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


class BotaoImagem(ButtonBehavior, Image):
    def __init__(self, imagem, on_press_action, **kwargs):
        super().__init__(**kwargs)
        self.source = imagem
        self.allow_stretch = True
        self.keep_ratio = False
        self.size_hint = (0.4, 0.12)
        self.on_press_action = on_press_action
        self.bind(on_release=self.on_press_action)

class TelaInicial(Screen, ThemeManagerMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.setup_background(layout)

        app = App.get_running_app()
        
        if not hasattr(app, 'sound_on'):
            app.sound_on = True

        
        self.title_card = MDCard(
            orientation="vertical",
            size_hint=(0.85, None),
            height=110,
            md_bg_color=(60/255, 20/255, 100/255, 0.65),  
            radius=[24],
            elevation=12,
            padding=[20, 10, 20, 10],
            pos_hint={"center_x": 0.5, "top": 0.95},
        )

        self.title_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 0.95, 0.8, 1),  
            font_style="H3",
            font_name="ComicNeue",  
            size_hint=(1, 1),
            valign="middle",
        )

        self.title_card.add_widget(self.title_label)
        layout.add_widget(self.title_card)
        self.digita_texto(self.title_label, "MATEMATICANDO")

        # Botão JOGAR
        botao_jogar = BotaoImagem(
            imagem="jogar.png",
            on_press_action=lambda *a: [self.tocar_som_giz(), self.ir_para_selecao()],
            pos_hint={"center_x": 0.5, "center_y": 0.65}
        )
        layout.add_widget(botao_jogar)

        # Botão INFORMAÇÕES
        botao_info = BotaoImagem(
            imagem="infos.png",
            on_press_action=lambda *a: [self.tocar_som_giz(), self.mostrar_info()],
            pos_hint={"center_x": 0.5, "center_y": 0.45}
        )
        layout.add_widget(botao_info)

        # Botão DESENVOLVEDORES
        botao_devs = BotaoImagem(
            imagem="devs.png",
            on_press_action=lambda *a: [self.tocar_som_giz(), self.mostrar_dev()],
            pos_hint={"center_x": 0.5, "center_y": 0.25}
        )
        layout.add_widget(botao_devs)

        self.add_widget(layout)

    def setup_background(self, layout):
        background = Image(
            source="fundoapp.png",  
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

    
    def on_enter(self, *args):
        app = App.get_running_app()
        # Carrega o som de fundo se ainda não foi carregado
        if not hasattr(app, 'background_music') or app.background_music is None:
            app.background_music = SoundLoader.load('stardew_valley.mp3') # Certifique-se de ter este arquivo
        
        if app.background_music:
            app.background_music.loop = True # Faz o som tocar em loop
            if app.sound_on and app.background_music.state != 'play':
                app.background_music.play()

    # Método chamado quando a tela deixa de ser a tela atual
    def on_leave(self, *args):
        app = App.get_running_app()
        if hasattr(app, 'background_music') and app.background_music and app.background_music.state == 'play':
            app.background_music.stop() # Para o som de fundo ao sair da tela inicial

    # Som botao
    def tocar_som_giz(self):
        # Garante que o som só é reproduzido se estiver ligado globalmente
        app = App.get_running_app()
        if hasattr(app, 'sound_on') and app.sound_on:
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

class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_stretch = True
        self.keep_ratio = True  

# classe do quadro
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

        btn_primario = ImageButton(
            source="primario.png",
            size_hint=(0.5, 0.18),
            pos_hint={"center_x": 0.5, "center_y": 0.68},
            on_release=lambda *args: self.ir_para_jogar_p()
        )
        layout.add_widget(btn_primario)

        btn_fundamental = ImageButton(
            source="fundamental.png",
            size_hint=(0.5, 0.18),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=lambda *args: self.ir_para_jogar_f()
        )
        layout.add_widget(btn_fundamental)

        btn_medio = ImageButton(
            source="medio.png",
            size_hint=(0.5, 0.18),
            pos_hint={"center_x": 0.5, "center_y": 0.32},
            on_release=lambda *args: self.ir_para_jogar()
        )
        layout.add_widget(btn_medio)

        # Variável para controlar o estado do som (ligado/desligado)
        # Inicializa o estado do som do aplicativo globalmente
        app = App.get_running_app()
        if not hasattr(app, 'sound_on'): 
            app.sound_on = True 
        self.sound_click = SoundLoader.load('stardew_valley.mp3') # Carrega o som do clique do botão

        # Botão de voltar
        back_button = MDIconButton(
            icon='arrow-left',
            pos_hint={'x': 0, 'top': 1},
            on_release=self.voltar
        )
        layout.add_widget(back_button)

        # Botão de som com cor e tamanho ajustados
        self.sound_button = MDIconButton(
            icon='volume-high' if app.sound_on else 'volume-off', 
            pos_hint={'x': 0.93, 'top': 1},
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1), 
            icon_size=35, # Tamanho do ícone em pixels (ajuste como preferir)
            on_release=self.toggle_sound_icon 
        )
        layout.add_widget(self.sound_button)

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

    def toggle_sound_icon(self, instance):
        app = App.get_running_app()
        if app.sound_on:
            # Se o som estava ligado, desliga e muda o ícone para 'volume-off'
            app.sound_on = False
            self.sound_button.icon = 'volume-off'
            print("Som Desligado")
            # Para o som de fundo quando o som geral é desligado
            if hasattr(app, 'background_music') and app.background_music:
                app.background_music.stop()
        else:
            # Se o som estava desligado, liga e muda o ícone para 'volume-high'
            app.sound_on = True
            self.sound_button.icon = 'volume-high'
            print("Som Ligado")
            # Toca o som de fundo quando o som geral é ligado, se não estiver tocando
            if hasattr(app, 'background_music') and app.background_music and app.background_music.state != 'play':
                app.background_music.play()

        # Toca o som de clique do botão, independentemente do estado global de som
        if self.sound_click:
            self.sound_click.play()


# Organizador de telas
from jogar import TelaEscolhaNivel, TelaJogar, JogosPrimario, JogosFundamental, JogosMedio
from calculo import calculoI, TelaFimDeJogo
from algebra import AlgebraGameScreen, TelaFimAlgebra
from fracoes import FracoesGameScreen, TelaFimFracoes


class AppGUI:
    def build_gui(self):
        sm = ScreenManager()
        sm.add_widget(TelaInicial(name="inicial"))
        sm.add_widget(TelaJogar(name="jogar_p", dificuldade="Primário", jogos=JogosPrimario.get()))
        sm.add_widget(TelaJogar(name="jogar_f", dificuldade="Fundamental", jogos=JogosFundamental.get()))
        sm.add_widget(TelaJogar(name="jogar", dificuldade="Médio", jogos=JogosMedio.get()))
        sm.add_widget(TelaEscolhaNivel(name="primario", dificuldade="primario", titulo="Fundamental I", tela_voltar="jogar"))
        sm.add_widget(TelaEscolhaNivel(name="fundamental", dificuldade="fundamental", titulo="Fundamental II", tela_voltar="jogar"))
        sm.add_widget(TelaEscolhaNivel(name="medio", dificuldade="medio", titulo="Ensino Médio", tela_voltar="jogar"))
        sm.add_widget(calculoI(name="game1"))
        sm.add_widget(AlgebraGameScreen(name="algebra"))
        sm.add_widget(TelaFimAlgebra(name="fim_algebra"))
        sm.add_widget(Seleciona_Nivel(name="seleciona"))
        sm.add_widget(TelaFimDeJogo(name="fim_de_jogo"))
        sm.add_widget(FracoesGameScreen(name="fracoes"))
        sm.add_widget(TelaFimFracoes(name="fim_fracoes"))
        return sm

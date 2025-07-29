from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.core.text import LabelBase
import random

LabelBase.register(name="ComicNeue", fn_regular="ComicNeue-Regular.ttf")

class CardBotao(MDRaisedButton):
    def __init__(self, texto, on_press_func, **kwargs):
        super().__init__(
            text=texto,
            on_release=lambda x: on_press_func(texto),
            size_hint=(1, 1),
            font_size="20sp",
            md_bg_color=random.choice([
                (1.0, 111 / 255, 64 / 255, 1),
                (0.36, 0.8, 0.96, 1),
                (0.85, 0.53, 0.97, 1),
                (0.59, 0.43, 0.91, 1),
            ]),
            text_color=(1, 1, 1, 1),
            font_name="ComicNeue",
            elevation=6,
            **kwargs
        )

class TelaCruzadinha(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "cruzadinha_estilizada"
        self.inputs = []
        self.gabarito = []

        self.bg_image = Image(source='fundoapp.png', allow_stretch=True, keep_ratio=False,
                              size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.add_widget(self.bg_image)

        self.main_layout = FloatLayout()
        self.add_widget(self.main_layout)

        self.top_layout = MDBoxLayout(orientation='horizontal', padding=[dp(10), dp(10)], spacing=dp(10),
                                      size_hint=(1, 0.1), pos_hint={"top": 1})
        self.btn_voltar = MDIconButton(icon="arrow-left", on_release=self.voltar)
        self.pontuacao_label = MDLabel(text="Pontuação: 0", halign="right", font_style="H6",
                                       theme_text_color="Custom", text_color=(1, 1, 1, 1), font_name="ComicNeue")
        self.top_layout.add_widget(self.btn_voltar)
        self.top_layout.add_widget(self.pontuacao_label)
        self.main_layout.add_widget(self.top_layout)

        self.grid = MDGridLayout(cols=5, rows=5, spacing=dp(5), padding=dp(5),
                                 size_hint=(0.95, 0.7), pos_hint={"center_x": 0.5, "top": 0.9})
        self.main_layout.add_widget(self.grid)

        self.base_layout = MDBoxLayout(orientation='horizontal', spacing=dp(20), padding=dp(20),
                                       size_hint=(1, 0.2), pos_hint={'y': 0})
        self.btn_verificar = CardBotao("Verificar", self.verificar_respostas)
        self.btn_limpar = CardBotao("Limpar", self.limpar_respostas)
        self.btn_nova = CardBotao("Nova cruzadinha", self.nova_cruzadinha)

        self.base_layout.add_widget(self.btn_verificar)
        self.base_layout.add_widget(self.btn_limpar)
        self.base_layout.add_widget(self.btn_nova)
        self.main_layout.add_widget(self.base_layout)

        self.gerar_cruzadinha()

    def gerar_operacao_valida(self, op, forcar_valor=None):
        if op == "+":
            a = random.randint(2, 30)
            b = random.randint(2, 30)
            return a, b, a + b
        elif op == "-":
            a = random.randint(10, 40)
            b = random.randint(1, a)
            return a, b, a - b
        elif op == "×":
            if forcar_valor is not None:
                # Queremos que a * b = forcar_valor
                # Escolhe um divisor aleatório de forcar_valor
                divisores = [i for i in range(1, forcar_valor + 1) if forcar_valor % i == 0]
                a = random.choice(divisores)
                b = forcar_valor // a
                return a, b, forcar_valor
            else:
                a = random.randint(2, 10)
                b = random.randint(2, 10)
                return a, b, a * b
        elif op == "÷":
            b = random.randint(2, 10)
            res = random.randint(2, 10)
            a = b * res
            return a, b, res


    def gerar_cruzadinha(self):
        self.inputs.clear()
        self.gabarito.clear()
        self.grid.clear_widgets()

        layout = [
            ["VAL", "÷", "", "=", "VAL"],
            ["-", None, "×", None, "×"],
            ["", None, "", None, ""],
            ["=", None, "=", None, "="],
            ["VAL", "+", "VAL", "=", ""]
        ]

        matriz = [[None for _ in range(5)] for _ in range(5)]

        # 1) Primeira linha: a ÷ b = res
        a1, b1, res1 = self.gerar_operacao_valida("÷")
        matriz[0][0] = a1
        matriz[0][2] = b1
        matriz[0][4] = res1

        # 2) Linha 5: soma
        a2, b2, res2 = self.gerar_operacao_valida("+")
        matriz[4][0] = a2
        matriz[4][2] = b2
        matriz[4][4] = res2

        # 3) Coluna 1:  a1 - x = a2  → x = a1 - a2
        matriz[2][0] = a1 - a2

        # 4) Coluna 3: multiplicação → usa res1 como um dos fatores, faz: res1 × x = ?
        mult_a = res1
        mult_b = random.randint(2, 10)
        mult_res = mult_a * mult_b
        matriz[2][2] = mult_a
        matriz[2][4] = mult_b
        matriz[4][2] = mult_res  # já foi preenchido na linha 5, mas pode ser sobrescrito com valor correto

        # Monta a grade com widgets
        for i in range(5):
            for j in range(5):
                val = layout[i][j]
                dado = matriz[i][j]
                if val is None:
                    self.grid.add_widget(MDCard(md_bg_color=(0, 0, 0, 0), radius=[dp(4)], elevation=0, size_hint=(1, 1)))
                elif val == "":
                    campo = TextInput(multiline=False, halign="center", font_size=24, size_hint=(1, 1),
                                      background_color=(1, 1, 1, 0.9), foreground_color=(0, 0, 0, 1))
                    self.inputs.append(campo)
                    self.gabarito.append(str(dado))
                    self.grid.add_widget(campo)
                elif val in ["+", "-", "×", "÷", "="]:
                    lbl = MDLabel(text=val, halign="center", valign="middle", font_style="H6",
                                  theme_text_color="Custom", text_color=(1, 1, 1, 1))
                    lbl.bind(size=lbl.setter('text_size'))
                    self.grid.add_widget(lbl)
                elif val == "VAL":
                    lbl = MDLabel(text=str(dado), halign="center", valign="middle", font_style="H6",
                                  theme_text_color="Custom", text_color=(1, 1, 1, 1))
                    lbl.bind(size=lbl.setter('text_size'))
                    self.grid.add_widget(lbl)


    def verificar_respostas(self, texto):
        pontuacao = 0
        for campo, resposta_correta in zip(self.inputs, self.gabarito):
            resposta = campo.text.strip().replace(",", ".")  # Corrige vírgula para ponto

            try:
                if int(float(resposta)) == int(float(resposta_correta)):
                    pontuacao += 10
                    campo.background_color = (0.6, 1, 0.6, 0.8)  # Verde
                else:
                    campo.background_color = (1, 0.6, 0.6, 0.8)  # Vermelho
            except:
                campo.background_color = (1, 0.6, 0.6, 0.8)

        self.pontuacao_label.text = f"Pontuação: {pontuacao}"



    def limpar_respostas(self, texto):
        for campo in self.inputs:
            campo.text = ""
            campo.background_color = (1, 1, 1, 0.9)

    def nova_cruzadinha(self, texto):
        self.limpar_respostas(texto)
        self.gerar_cruzadinha()
        self.pontuacao_label.text = "Pontuação: 0"

    def voltar(self, instance):
        print("Voltando para o menu")

class AppCruzadinhaMD(MDApp):
    def build(self):
        return TelaCruzadinha()

if __name__ == "__main__":
    AppCruzadinhaMD().run()

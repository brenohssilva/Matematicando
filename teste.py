import random
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

# =============================================================================
# CLASSE DA TELA DO JOGO "GRADE DE MULTIPLICAÇÃO"
# =============================================================================
class GridGameScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'grid_game'

        # Variáveis de estado do jogo
        self.correct_answer = 0
        self.current_question = 1
        self.total_questions = 10

        # --- Estrutura Principal da UI ---
        main_layout = MDBoxLayout(orientation='vertical', padding=dp(10), spacing=dp(20))
        main_layout.md_bg_color = get_color_from_hex("#3450A1")

        # 1. Cabeçalho (Progresso)
        self.progress_label = MDLabel(
            text=f"{self.current_question}/{self.total_questions}",
            halign='center',
            font_style='H5',
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(40)
        )
        main_layout.add_widget(self.progress_label)

        # 2. Card Principal (Notepad)
        notepad_card = MDCard(
            size_hint=(0.9, 1), # Ocupa mais espaço vertical
            pos_hint={'center_x': 0.5},
            padding=dp(15),
            radius=[20],
            md_bg_color=get_color_from_hex("#F1F6F9")
        )

        # <<< AQUI ESTÁ A CORREÇÃO >>>
        # A grade agora tem 4 linhas e 4 colunas, totalizando 16 espaços.
        grid_layout = MDGridLayout(cols=4, rows=4, spacing=dp(5))

        # Criando os widgets de Label para a grade
        self.cell_tl = self.create_cell_label()
        self.cell_tr = self.create_cell_label()
        self.prod_r1 = self.create_product_label()
        self.cell_bl = self.create_cell_label()
        self.cell_br = self.create_cell_label()
        self.prod_r2 = self.create_product_label()
        self.prod_c1 = self.create_product_label()
        self.prod_c2 = self.create_product_label()

        # Adicionando widgets na ordem correta
        # Linha 1
        grid_layout.add_widget(self.cell_tl)
        grid_layout.add_widget(MDLabel(text='x', halign='center', font_style='H4'))
        grid_layout.add_widget(self.cell_tr)
        grid_layout.add_widget(self.prod_r1)

        # Linha 2 (símbolos de multiplicação e igualdade)
        grid_layout.add_widget(MDLabel(text='x', halign='center', font_style='H4'))
        grid_layout.add_widget(MDLabel())
        grid_layout.add_widget(MDLabel(text='x', halign='center', font_style='H4'))
        grid_layout.add_widget(MDLabel(text='=', halign='center', font_style='H4'))

        # Linha 3
        grid_layout.add_widget(self.cell_bl)
        grid_layout.add_widget(MDLabel(text='=', halign='center', font_style='H4'))
        grid_layout.add_widget(self.cell_br)
        grid_layout.add_widget(self.prod_r2)

        # Linha 4 (símbolos de igualdade e produtos das colunas)
        grid_layout.add_widget(MDLabel(text='=', halign='center', font_style='H4'))
        grid_layout.add_widget(MDLabel())
        grid_layout.add_widget(MDLabel(text='=', halign='center', font_style='H4'))
        grid_layout.add_widget(MDLabel()) # Célula vazia no canto

        notepad_card.add_widget(grid_layout)

        # Adicionando os produtos das colunas por baixo do grid principal
        bottom_products_layout = MDGridLayout(cols=4, size_hint_y=None, height=dp(50))
        bottom_products_layout.add_widget(self.prod_c1)
        bottom_products_layout.add_widget(MDLabel())
        bottom_products_layout.add_widget(self.prod_c2)
        bottom_products_layout.add_widget(MDLabel())
        notepad_card.add_widget(bottom_products_layout)

        main_layout.add_widget(notepad_card)

        # 3. Botões de Resposta
        self.answer_buttons_layout = MDGridLayout(
            cols=2,
            size_hint_y=None,
            height=dp(150),
            padding=dp(20),
            spacing=dp(20)
        )
        main_layout.add_widget(self.answer_buttons_layout)

        self.add_widget(main_layout)
        self.generate_puzzle()

    def create_cell_label(self, is_question=False):
        card = MDCard(
            md_bg_color=get_color_from_hex("#DDE6ED" if not is_question else "#F8BDEB"),
            radius=[10],
            elevation=1
        )
        label = MDLabel(halign='center', font_style='H4', theme_text_color="Primary")
        card.add_widget(label)
        return card

    def create_product_label(self):
        label = MDLabel(halign='center', font_style='H5', text="= ??")
        return label

    def generate_puzzle(self):
        self.progress_label.text = f"{self.current_question}/{self.total_questions}"
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        c = random.randint(2, 12)
        d = random.randint(2, 12)
        cells = {'tl': a, 'tr': b, 'bl': c, 'br': d}
        products = {'r1': a * b, 'r2': c * d, 'c1': a * c, 'c2': b * d}
        hidden_cell_key = random.choice(list(cells.keys()))
        self.correct_answer = cells[hidden_cell_key]
        for key, value in cells.items():
            label_widget = getattr(self, f"cell_{key}")
            label_widget.children[0].text = str(value) if key != hidden_cell_key else "?"
            label_widget.md_bg_color = get_color_from_hex("#F8BDEB" if key == hidden_cell_key else "#DDE6ED")
        self.prod_r1.text = f"= {products['r1']}"
        self.prod_r2.text = f"= {products['r2']}"
        self.prod_c1.text = f"= {products['c1']}"
        self.prod_c2.text = f"= {products['c2']}"
        options = {self.correct_answer}
        while len(options) < 4:
            wrong_option = random.randint(max(1, self.correct_answer - 10), self.correct_answer + 10)
            if wrong_option != self.correct_answer:
                options.add(wrong_option)
        shuffled_options = list(options)
        random.shuffle(shuffled_options)
        self.answer_buttons_layout.clear_widgets()
        for option in shuffled_options:
            btn = MDRaisedButton(text=str(option), size_hint=(1, 1), font_style="H5", md_bg_color=get_color_from_hex("#A084E8"), on_release=self.check_answer)
            self.answer_buttons_layout.add_widget(btn)

    def check_answer(self, button):
        if int(button.text) == self.correct_answer:
            print("Resposta Correta!")
            button.md_bg_color = get_color_from_hex("#65B741")
        else:
            print("Resposta Errada!")
            button.md_bg_color = get_color_from_hex("#D83F31")
        for btn in self.answer_buttons_layout.children:
            btn.disabled = True
        self.current_question += 1
        if self.current_question > self.total_questions:
            print("Fim de Jogo!")
            Clock.schedule_once(lambda dt: self.manager.get_screen('menu').on_enter() if self.manager else None, 2)
        else:
            Clock.schedule_once(lambda dt: self.generate_puzzle(), 2)

# =============================================================================
# CLASSE PRINCIPAL DO APP DE TESTE
# =============================================================================
class GridTestApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(GridGameScreen(name='grid_game'))
        sm.add_widget(MDScreen(name='menu'))
        return sm

if __name__ == '__main__':
    GridTestApp().run()
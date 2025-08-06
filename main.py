from kivymd.app import MDApp
from gui import AppGUI

class MobileApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_theme = "Light"

    def build(self):
        self.theme_cls.theme_style = self.current_theme
        self.theme_cls.primary_palette = "Teal"
        gui = AppGUI()
        return gui.build_gui()

if __name__ == "__main__":
 MobileApp().run()
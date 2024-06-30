from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/homeFiles/home.kv")

class Home(BoxLayout):
    def __init__(self, wm, **kwargs):
        super().__init__(**kwargs)
        self.wm = wm

    def go_to_login(self):
        self.wm.current = 'login'

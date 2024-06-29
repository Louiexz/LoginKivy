from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/homeFiles/home.kv")

class Home(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def go_to_login(self):
        self.manager.current = 'login'

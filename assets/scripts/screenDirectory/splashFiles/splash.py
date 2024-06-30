from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/splashFiles/splash.kv")

class Splash(BoxLayout):
    def __init__(self, wm, **kwargs):
        super().__init__(**kwargs)
        self.wm = wm

        Clock.schedule_once(lambda dt:self.trigger_login(dt), 6)
    
    def trigger_login(self, dt): self.wm.current = "login"
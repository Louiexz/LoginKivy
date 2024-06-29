from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from assets.scripts.screenDirectory.loginFiles.login import Login
from assets.scripts.screenDirectory.homeFiles.home import Home

class LoginScreen(Screen, Login):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Login.__init__(self, **kwargs)  # Initialize Login functionality

class HomeScreen(Screen, Home):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Home.__init__(self, **kwargs)  # Initialize Home functionality

class WindowManager(ScreenManager):
    pass

class ScreenApp(App):
    def build(self):
        wm = WindowManager()
        wm.add_widget(LoginScreen(name='login'))
        wm.add_widget(HomeScreen(name='home'))
        wm.current = 'login'  # Set 'home' screen as the initial screen
        return wm

    def on_start(self): self.title = "Alerta Furto"

if __name__ == '__main__':
    ScreenApp().run()

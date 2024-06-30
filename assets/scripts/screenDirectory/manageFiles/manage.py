from kivy.uix.screenmanager import ScreenManager, Screen
from assets.scripts.screenDirectory.splashFiles.splash import Splash
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

class SplashScreen(Screen, Splash):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Splash.__init__(self, **kwargs)

class WindowManager(ScreenManager): pass
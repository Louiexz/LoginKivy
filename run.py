from assets.scripts.screenDirectory.manageFiles.manage import *
from kivy.app import App

class ScreenApp(App):
    def build(self):
        self.title = "Alerta Furto"
        
        wm = ScreenManager()
        wm.add_widget(SplashScreen(name='splash', wm=wm))
        wm.add_widget(LoginScreen(name='login', wm=wm))
        wm.add_widget(HomeScreen(name='home', wm=wm))
        
        # Set 'home' screen as the initial screen
        wm.current = 'splash'
        
        return wm

if __name__ == '__main__':
    ScreenApp().run()

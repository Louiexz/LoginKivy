from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from tratarJson import Users
from account import Email
from kivy.uix.image import Image

class LoginScreen(BoxLayout):
    def pegaDados(self): return [self.ids[x].text for x in ["usuario", "senha", "email"]]

    def on_entrar(self):
        if Users.validUser(self.pegaDados()): print("Usuário válido!")
        else: print("Usuário inválido, cadastre-se!")

    def on_esqueci_senha(self):
        dados = self.pegaDados()

        if Users.validUser(dados):
            try:
                if Email.redefinirSenha(dados): print("Código enviado com sucesso!")
            except Exception as a: print(f'Email não enviado por: {a} motivo')

    def on_novo_usuario(self):
        if Users.registerUser(self.pegaDados()): print('Usuário já registrado!')
        else: print('Usuário registrado com sucesso!')

class LoginApp(App):
    image_source = "./img/alerta.png"

    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    LoginApp().run()

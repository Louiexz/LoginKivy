from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/loginFiles/login.kv")

from ...functs.tratarJson import Users
from ...functs.account import Email

class Login(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def go_to_home(self):
        self.manager.current = 'home'
    
    def pegaDados(self):
        return [self.ids[x].text for x in ["usuario", "senha", "email"]]

    def on_entrar(self):
        if Users.validUser(self.pegaDados()): print("Usuário válido!")
        else: print("Usuário inválido, cadastre-se!")

    def on_forgot_password(self):
        dados = self.pegaDados()

        if Users.validUser(dados):
            try:
                if Email.redefinirSenha(dados): print("Código enviado com sucesso!")
            except Exception as a: print(f'Email não enviado por: {a} motivo')
        else: print("Preencha todos os campos.")
    
    def on_new_user(self):
        retorno = Users.registerUser(self.pegaDados())

        if retorno == True: print('Usuário já registrado.')
        elif retorno == "erro": print("Preencha todos os campos.")
        else: print('Usuário registrado com sucesso.')
        
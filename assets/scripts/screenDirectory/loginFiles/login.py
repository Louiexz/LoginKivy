from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file("assets/scripts/screenDirectory/loginFiles/login.kv")

from ...functs.tratarJson import Users
from ...functs.account import Email

class Login(BoxLayout):
    def __init__(self, wm, **kwargs):
        super().__init__(**kwargs)
        self.wm = wm
    
    def pega_dados(self):
        return [self.ids[x].text for x in ["usuario", "senha", "email"]]
    
    def on_entrar(self):
        if Users.valid_user(self.pega_dados()):
            print("Usuário válido!")
            self.wm.current = 'home'
        
    def on_valid(self): pass

    def on_forgot_password(self):
        dados = self.pega_dados()

        if Users.valid_user(dados):
            try:
                if Email.redefinir_senha(dados): print("Código enviado com sucesso!")
            except Exception as a: print(f'Email não enviado por: {a} motivo')
        else: print("Preencha todos os campos.")
    
    def on_new_user(self):
        retorno = Users.register_user(self.pega_dados())

        if retorno == True: print('Usuário já registrado.')
        elif retorno == "erro": print("Preencha todos os campos.")
        else: print('Usuário registrado com sucesso.')
        
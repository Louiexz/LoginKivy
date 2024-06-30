import json
from email_validator import validate_email, EmailNotValidError

filename = 'assets/json/users.json'

class Users:
    _listaDados = [[]]
    
    @classmethod
    def load_data(cls, filename=filename):
        try:
            with open(filename, 'r') as f_obj: cls._listaDados = json.load(f_obj)
        except (FileNotFoundError, json.JSONDecodeError): cls._listaDados = []
        finally: return cls._listaDados

    @classmethod
    def save_data(cls):
        with open(filename, 'w') as f_obj: json.dump(cls._listaDados, f_obj, indent=2)

    @classmethod
    def valid_user(cls, dados):
        validacao = False

        if not any(dados[0] in entry or dados[2] in entry for entry in cls.load_data()): pass
        else: validacao = True

        return validacao
    
    @classmethod
    def valid_email(cls, email):
        try:
            emailinfo = validate_email(email, check_deliverability=False)
            return emailinfo.normalized
        except EmailNotValidError as e: return ""
        
    @classmethod
    def register_user(cls, dados):
        if cls.valid_user(dados): return True
        
        else:
            dados[2] = cls.valid_email(dados[2])
            if "" in dados: return "erro"
            else:
                cls._listaDados.append(dados) 

                cls.save_data()
                return False

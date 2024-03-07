import json

filename = 'users.json'

class Users:
    _listaDados = []
    
    @classmethod
    def loadData(cls):
        try:
            with open(filename, 'r') as f_obj:
                cls._listaDados = json.load(f_obj)
        except (FileNotFoundError, json.JSONDecodeError): cls._listaDados = []
        finally: return cls._listaDados

    @classmethod
    def saveData(cls):
        with open(filename, 'w') as f_obj:
            json.dump(cls._listaDados, f_obj, indent=2)

    @classmethod
    def validUser(cls, dados):
        validacao = False

        if not any(dados[0] in entry or dados[2] in entry for entry in cls.loadData()): pass
        else: validacao = True

        return validacao

    @classmethod
    def registerUser(cls, dados):
        if cls.validUser(dados): return True
        else:
            cls._listaDados.append(dados)
            cls.saveData()
            return False

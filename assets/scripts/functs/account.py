import smtplib
import random
from email.mime.text import MIMEText
from .tratarJson import Users

filename = "assets/json/conta.json"

class Email:
	@classmethod
	def conecta_mail(cls):
		data = Users.load_data(filename=filename)

		if data:
			servidor = smtplib.SMTP('smtp.gmail.com', 587)
			servidor.starttls()
			servidor.login(data["admin"][0], data["admin"][1])

			return servidor
		else: return False

	@classmethod
	def envia_mail(cls, dados):
		servidor = cls.conecta_mail()

		if servidor:
			servidor.sendmail(dados[0], dados[1], dados[2])
			cls.sairServidor(servidor)
		else: print("Registre uma conta remetente")
	
	@classmethod
	def sair_servidor(cls, servidor): servidor.quit()

	@classmethod
	def gera_codigo(cls):
		codigo = [random.randint(0, 9) for _ in range(6)]
		return ''.join(map(str, codigo))

	@classmethod
	def redefinir_senha(cls, dados):
		msg = MIMEText(f"""Olá, {dados[0]}!\n
Seu código para recuperação de senha:\n
\t\t-- {cls.geraCodigo()} --\n\n
Link para redefinição:\n\n
Caso você não tenha pedido a redefinição de senha, ignore este aviso.""")

		msg['Subject'] = 'Código para recuperação de senha'
		msg['To'] = f'{dados[2]}'
		msg['From'] = 'seuemail@exemplo.com'

		return cls.envia_mail([msg['From'], msg['To'], msg.as_string()])

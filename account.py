import smtplib
import random
from email.mime.text import MIMEText

#senha = "suasenhaaqui"

class Email:
	@classmethod
	def conectaEmail(cls, mail=False, senha=False):
		if mail:
			servidor = smtplib.SMTP('smtp.gmail.com', 587)
			servidor.starttls()
			servidor.login(mail, senha)

			return servidor
		else: return False

	@classmethod
	def enviaEmail(cls, dados):
		servidor = cls.conectaEmail()#"seuemailaqui")

		if servidor:
			servidor.sendmail(dados[0], dados[1], dados[2])
			cls.sairServidor(servidor)
		else: print("Registre uma conta remetente")
	
	@classmethod
	def sairServidor(cls, servidor): servidor.quit()

	@classmethod
	def geraCodigo(cls):
		codigo = [random.randint(0, 9) for _ in range(6)]
		return ''.join(map(str, codigo))

	@classmethod
	def redefinirSenha(cls, dados):
		msg = MIMEText(f"""Olá, {dados[0]}!\n
Seu código para recuperação de senha:\n
\t\t-- {cls.geraCodigo()} --\n\n
Link para redefinição:\n\n
Caso você não tenha pedido a redefinição de senha, ignore este aviso.""")

		msg['Subject'] = 'Código para recuperação de senha'
		msg['To'] = f'{dados[2]}'
		msg['From'] = 'seuemail@exemplo.com'

		return cls.enviaEmail([msg['From'], msg['To'], msg.as_string()])

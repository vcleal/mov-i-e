import  smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailHandler(object):
	"""EmailHandler"""
	def __init__(self, fromaddr, toaddr, body='Movement detected',
	 smtpServer='smtp.gmail.com', port=587,):
		self.smtpServer = smtpServer
		self.port = port
		self.fromaddr = fromaddr
		self.toaddr = toaddr
		self.msg = MIMEMultipart()
		self.msg['From'] = fromaddr
		self.msg['To'] = toaddr
		self.msg['Subject'] = "mov-i-e notification"
		self.msg.attach(MIMEText(body,'plain'))
		self.passwd = getpass.getpass("Email password:")

	def connect(self):
		try:
			server = smtplib.SMTP(self.smtpServer, self.port)
			server.starttls()
			server.login(self.fromaddr, self.passwd)
			server.sendmail(self.fromaddr, self.toaddr, self.msg.as_string())
		except smtplib.SMTPException:
			raise
		finally:
			server.quit()
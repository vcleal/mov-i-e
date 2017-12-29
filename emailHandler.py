import  smtplib
import getpass

class EmailHandler(object):
	"""EmailHandler"""
	def __init__(self, fromaddr, toaddr, msg='Notification',
	 smtpServer='smtp.gmail.com', port=587,):
		self.smtpServer = smtpServer
		self.port = port
		self.fromaddr = fromaddr
		self.toaddr = toaddr
		self.msg = msg
		self.passwd = getpass.getpass()

	def connect(self):
		try:
			server = smtplib.SMTP(self.smtpServer, self.port)
			server.starttls()
			server.login(self.fromaddr, self.passwd)
			server.sendmail(self.fromaddr, self.toaddr, self.msg)
		except smtplib.SMTPException:
			raise
		finally:
			server.quit()
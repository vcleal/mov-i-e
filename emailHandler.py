import  smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from time import sleep

class EmailHandler(object):
	"""EmailHandler"""
	def __init__(self, fromaddr, toaddr, body='Movement detected',
	 smtpServer='smtp.gmail.com', port=587,):
		self.email = 1
		self.smtpServer = smtpServer
		self.port = port
		self.fromaddr = fromaddr
		self.toaddr = toaddr
		self.passwd = getpass.getpass("Email password:")
		self.body = body
		self.msg = body
	
	def setMsg(self,count):
		self.msg = MIMEMultipart()
		self.msg['From'] = self.fromaddr
		self.msg['To'] = self.toaddr
		self.msg['Subject'] = "mov-i-e notification"
		self.msg.attach(MIMEText(self.body,'plain'))
		fp = open('capture/screenshot%d.png' % count,'rb')
		self.msg.attach(MIMEImage(fp.read()))
		fp.close()

	def connect(self,count):
		self.setMsg(count)
		try:
			server = smtplib.SMTP(self.smtpServer, self.port)
			server.starttls()
			server.login(self.fromaddr, self.passwd)
			server.sendmail(self.fromaddr, self.toaddr, self.msg.as_string())
		except smtplib.SMTPException:
			raise
		finally:
			server.quit()

	def inc(self):
		self.email += 1

	def reset(self):
		self.email = 1
		sleep(2)
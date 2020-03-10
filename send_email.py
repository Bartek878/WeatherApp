from configurator import Config
config = Config()
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

class MailSender:

    def __init__(self):
        pass

    def send_mail(self):

        username = input('Podaj swoj adres email: ')
        password = input('Podaj swoje hasło: ')
        receiver = input('Podaj adres email na który chcesz wysłać plik: ')
        email_from = username
        email_to = receiver
        fileToSend = config.file_ok2

        message = MIMEMultipart()
        message["From"] = email_from
        message["To"] = email_to
        message["Subject"] = config.mail_subject
        message.preamble = "plik"

        ctype, encoding = mimetypes.guess_type(fileToSend)

        maintype, subtype = ctype.split("/", 1)

        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
        message.attach(attachment)

        server = smtplib.SMTP("poczta.o2.pl:25")
        server.starttls()
        server.login(username,password)
        server.sendmail(email_from, email_to, message.as_string())
        server.quit()

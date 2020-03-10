from configurator import Config
config = Config()
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class MailSender:

    def __init__(self):
        pass

    def send_mail(self):

        username = input('Podaj swoj adres email: ')
        password = input('Podaj swoje hasło: ')
        receiver = input('Podaj adres email na który chcesz wysłać plik: ')
        email_from = username
        email_to = receiver
        dir_path = str(pathlib.Path().absolute())
        files = ["Obecna Pogoda.png", "obraz.png", "Pogoda.xlsx"]

        message = MIMEMultipart()
        message["From"] = email_from
        message["To"] = email_to
        message["Subject"] = config.mail_subject
        message.preamble = "plik"

        body = MIMEText('Results attached.', 'html', 'utf-8')
        message.attach(body)  # add message body (text or html)

        for f in files:  # add files to the message
            file_path = os.path.join(dir_path, f)
            attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
            attachment.add_header('Content-Disposition', 'attachment', filename=f)
            message.attach(attachment)

        server = smtplib.SMTP("poczta.o2.pl:25")
        server.starttls()
        server.login(username,password)
        server.sendmail(email_from, email_to, message.as_string())
        server.quit()
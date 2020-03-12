from configurator import Config
config = Config()

from UserInputs import InputProvider
inputProvider = InputProvider()

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

        username = config.user_mail
        password = config.user_password
        receiver = config.mail_receiver
        email_from = username
        email_to = receiver
        dir_path = str(pathlib.Path().absolute())
        files = [config.file_excel, config.file_png, config.file_png2]

        message = MIMEMultipart()
        message["From"] = email_from
        message["To"] = email_to
        message["Subject"] = config.mail_subject

        body = MIMEText(config.mail_body, 'html', 'utf-8')
        message.attach(body)  # add message body (text or html)

        for f in files:  # add files to the message
            file_path = os.path.join(dir_path, f)
            attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
            attachment.add_header('Content-Disposition', 'attachment', filename=f)
            message.attach(attachment)

        try:
            server = smtplib.SMTP("poczta.o2.pl:25")
            server.starttls()
            server.login(username,password)
            server.sendmail(email_from, email_to, message.as_string())
            server.quit()
        except Exception:
            print('Niestety podales zle dane do logowanie, wprowadz je ponownie: ')
            config.user_mail = inputProvider.ask_for_login()
            config.user_password = inputProvider.ask_for_password()
            config.mail_receiver = inputProvider.ask_for_receiver_mail()
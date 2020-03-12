class InputProvider:

    def __init__(self):
        pass

    def ask_for_city(self):
        self.city = input('Enter the city for which you want to know the weather: ')

    def ask_for_login(self):
        self.user_mail = input('Enter your email address: ')

    def ask_for_password(self):
        self.user_password = input('Enter your password: ')

    def ask_for_receiver_mail(self):
        self.mail_receiver = input('Enter the email address to which you want to send the file: ')
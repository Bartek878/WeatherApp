import pathlib

class Config(object):
    selected_city = input('Podaj miasto, dla którego chcesz poznać pogodę: ')
    user_mail = input('Podaj swoj adres email: ')
    user_password = input('Podaj swoje hasło: ')
    mail_receiver = input('Podaj adres email na który chcesz wysłać plik: ')
    file_raw = str(pathlib.Path().absolute()) + '\pogoda_raw.csv'
    file_ok = str(pathlib.Path().absolute()) + '\pogoda_ok.csv'
    file_ok2 = str(pathlib.Path().absolute()) + '\pogoda_ok2.csv'
    file_ok3 = str(pathlib.Path().absolute()) + '\pogoda_ok3.csv'
    file_ok3_r = str(pathlib.Path().absolute()) + "\pogoda_ok3.csv"
    file_excel = str(pathlib.Path().absolute()) + '\Pogoda.xlsx'
    file_png = str(pathlib.Path().absolute()) + '\Pogoda_wykres.png'
    file_png2 = str(pathlib.Path().absolute()) + '\Obecna Pogoda.png'
    header_names = ["Godzina", "Temperatura", "Temp. Odczuwalna", "Prognoza", "Wiatr kier.", "Wiatr pr", "Wiatr pr max", "Zachmurzenie", "Opady", "Wilgotność"]
    chart_title = 'Pogoda godzinowa na najbliższe 120h'
    chart_Y_axis_name = 'Temperatura (°C)'
    mail_subject = 'Dane pogodowe z AccuWeather.'
    mail_body = '\
    Witam,\n\
    <br>\n\
    <br>W załączniku przesyłam pliki dla obecnej prognozy pogody:\n\
    <br>1. Pogoda.xlsx - plik Excel w pogodą na najbliższe 120h w formie tabeli,\n\
    <br>2. Pogoda_wykres.png - plik png z pogoda na najbliższe 120h w formie wykresu,\n\
    <br>3. Obecna_Pogoda.png - zrzut ekranu prosto z serwisu pogodowego na najbliższe 16h.\n\
    <br>\n\
    <br>Pozdrawiam,\n\
    <br>Bartek.'
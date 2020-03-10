import pathlib
class Config(object):
    file_raw = str(pathlib.Path().absolute()) + '\pogoda_raw.csv'
    file_ok = str(pathlib.Path().absolute()) + '\pogoda_ok.csv'
    file_ok2 = str(pathlib.Path().absolute()) + '\pogoda_ok2.csv'
    file_ok3 = str(pathlib.Path().absolute()) + '\pogoda_ok3.csv'
    file_ok3_r = str(pathlib.Path().absolute()) + "\pogoda_ok3.csv"
    file_excel = str(pathlib.Path().absolute()) + '\Pogoda.xlsx'
    file_png = str(pathlib.Path().absolute()) + '\Pogoda_wykres.png'
    header_names = ["Godzina", "Temperatura", "Temp. Odczuwalna", "Prognoza", "Wiatr kier.", "Wiatr pr", "Wiatr pr max", "Zachmurzenie", "Opady", "Wilgotność"]
    chart_title = 'Pogoda godzinowa na najbliższe 120h'
    chart_Y_axis_name = 'Temperatura (°C)'
    mail_subject = 'Wysylam plik csv z hackathonu'


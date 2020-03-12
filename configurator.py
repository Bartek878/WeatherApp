import pathlib
from selenium import webdriver
from UserInputs import InputProvider
inputProvider = InputProvider()

class Config(object):
    selected_city = inputProvider.ask_for_city()
    user_mail = inputProvider.ask_for_login()
    user_password = inputProvider.ask_for_password()
    mail_receiver = inputProvider.ask_for_receiver_mail()
    driver = webdriver.Chrome(str(pathlib.Path().absolute()) + '\chromedriver.exe')
    file_raw = str(pathlib.Path().absolute()) + '\weather_raw.csv'
    file_ok = str(pathlib.Path().absolute()) + '\weather_ok.csv'
    file_ok2 = str(pathlib.Path().absolute()) + '\weather_ok2.csv'
    file_ok3 = str(pathlib.Path().absolute()) + '\weather_ok3.csv'
    file_excel = str(pathlib.Path().absolute()) + '\Weather.xlsx'
    file_png = str(pathlib.Path().absolute()) + '\Weather_chart.png'
    file_png2 = str(pathlib.Path().absolute()) + '\Current_weather.png'
    header_names = ["Godzina", "Temperatura", "Temp. Odczuwalna", "Prognoza", "Wiatr kier.", "Wiatr pr", "Wiatr pr max",
                    "Zachmurzenie", "Opady", "Wilgotność"]
    chart_title = 'Hourly weather for the next 120h'
    chart_Y_axis_name = 'Temperature (°C)'
    mail_subject = 'Weather data from AccuWeather.'
    mail_body = '\
    Hello,\n\
    <br>\n\
    <br>In the attachment I am sending files with the current weather forecast:\n\
    <br>1. Weather.xlsx - Excel file containing the weather for the next 120 hours in the form of a table,\n\
    <br>2. Weather_chart.png - png file with the weather for the next 120 hours in the form of a chart,\n\
    <br>3. Current_weather.png - screenshot straight from the weather service with weather forecast for the next 16h.\n\
    <br>\n\
    <br>Regards,\n\
    <br>Bartek.'
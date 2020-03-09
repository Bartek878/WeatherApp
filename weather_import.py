from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import csv
import os
from .configurator import Config
config = Config()

class weather:

    def __init__(self):
        pass

    def open_webpage(self):
        self.driver = webdriver.Chrome('D:/Bartosz/Python/webdriver/chromedriver.exe')
        self.driver.get("https://pogoda.interia.pl/lista-wojewodztw")
        delay = 3

    def choose_city(self):
        global city
        city = input('Podaj miasto, dla którego chcesz poznać pogodę: ')
        cookies_accept = self.driver.find_element_by_class_name("rodo-popup-agree")
        cookies_accept.send_keys(Keys.ENTER)
        fill_city = self.driver.find_element_by_id("weather-currently-input-text-1")
        fill_city.send_keys(city)
        delay = 2
        fill_city.send_keys(Keys.ENTER)

    def current_weather(self):
        current_temp = self.driver.find_element_by_class_name("weather-currently-temp .weather-currently-temp-strict")
        current_temp_feel = self.driver.find_element_by_class_name("feelTemperature .weather-currently-details-value")
        current_pressure = self.driver.find_element_by_class_name("pressure .weather-currently-details-value")
        current_wind = self.driver.find_element_by_class_name("wind .weather-currently-details-value")

        print('Obecnie temperatura w miescie ' + city + ' to: ' + str(current_temp.text))
        print('Obecnie odczuwalna temperatura w miescie ' + city + ' to: ' + str(current_temp_feel.text))
        print('Obecnie cisnienie w miescie ' + city + ' to: ' + str(current_pressure.text))
        print('Obecna predkosc wiatru w miescie ' + city + ' to: ' + str(current_wind.text))

        current_time = self.driver.find_element_by_class_name("weather-currently-info-item-time")
        current_sunrise = self.driver.find_element_by_class_name("weather-currently-info-sunrise")
        current_sunset = self.driver.find_element_by_class_name("weather-currently-info-sunset")
        print('Jest godzina ' + str(current_time.text) + ', słońce wzeszło dzisiaj o godz. ' + str(
            current_sunrise.text) + ' natomiast zajdzie o godz. ' + str(current_sunset.text) + '.')

        weather_provider = self.driver.find_element_by_class_name("weather-currently-poweredby-company")
        print('Informacje na temat naszej pogody otrzymujemy bezpośrednio z serwerów ' + str(weather_provider.text))

    def write_to_csv(self):
        lista_input = [el.text for el in self.driver.find_elements_by_class_name("weather-entry")]
        with open(config.file_raw, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            for wiersz in lista_input:
                writer.writerow(wiersz.split("\n"))
        #Overwrite csv without blank lines
        with open(config.file_raw) as input, open(config.file_ok, 'w') as output:
            non_blank = (line for line in input if line.strip())
            output.writelines(non_blank)
        #remove raw file
        input.close()
        os.remove(config.file_raw)
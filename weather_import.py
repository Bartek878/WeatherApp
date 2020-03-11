from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import csv
import os
import time
import pathlib
from configurator import Config
config = Config()
import io
from PIL import Image


class WeatherImporter:

    def __init__(self):
        self.driver = webdriver.Chrome(str(pathlib.Path().absolute()) + '\chromedriver.exe')

    def open_webpage(self):
        self.driver.get("https://pogoda.interia.pl/lista-wojewodztw")

    def choose_city(self):
        time.sleep(1)
        cookies_accept = self.driver.find_element_by_class_name("rodo-popup-agree")
        cookies_accept.send_keys(Keys.ENTER)
        time.sleep(1)
        fill_city = self.driver.find_element_by_id("weather-currently-input-text-1")
        fill_city.send_keys(config.selected_city)
        time.sleep(1)
        fill_city.send_keys(Keys.ENTER)

    def get_current_weather(self):
        current_temp = self.driver.find_element_by_class_name("weather-currently-temp .weather-currently-temp-strict")
        current_temp_feel = self.driver.find_element_by_class_name("feelTemperature .weather-currently-details-value")
        current_pressure = self.driver.find_element_by_class_name("pressure .weather-currently-details-value")
        current_wind = self.driver.find_element_by_class_name("wind .weather-currently-details-value")

        print('Obecnie temperatura w miescie ' + config.selected_city + ' to: ' + str(current_temp.text))
        print('Obecnie odczuwalna temperatura w miescie ' + config.selected_city + ' to: ' + str(current_temp_feel.text))
        print('Obecnie cisnienie w miescie ' + config.selected_city + ' to: ' + str(current_pressure.text))
        print('Obecna predkosc wiatru w miescie ' + config.selected_city + ' to: ' + str(current_wind.text))

        current_time = self.driver.find_element_by_class_name("weather-currently-info-item-time")
        current_sunrise = self.driver.find_element_by_class_name("weather-currently-info-sunrise")
        current_sunset = self.driver.find_element_by_class_name("weather-currently-info-sunset")
        print('Jest godzina ' + str(current_time.text) + ', słońce wzeszło dzisiaj o godz. ' + str(
            current_sunrise.text) + ' natomiast zajdzie o godz. ' + str(current_sunset.text) + '.')

        weather_provider = self.driver.find_element_by_class_name("weather-currently-poweredby-company")
        print('Informacje na temat naszej pogody otrzymujemy bezpośrednio z serwerów ' + str(weather_provider.text))

    def get_weather_screenshot1(self):
            self.driver.execute_script("window.scrollTo(0, 600);")
            image = self.driver.find_element_by_id('chart-container-hbh').screenshot_as_png
            imageStream = io.BytesIO(image)
            im = Image.open(imageStream)
            im.save('Obecna Pogoda.png')

    def get_data_to_file(self):
        lista_input = [el.text for el in self.driver.find_elements_by_class_name("weather-entry")]
        with open(config.file_raw, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            for wiersz in lista_input:
                writer.writerow(wiersz.split("\n"))

        text = open(config.file_raw, mode='r', encoding='latin-1')
        for r in (("°C", ""), ("Â", "")):
            text = ''.join([i for i in text]) \
                .replace(*r)
        x = open(config.file_ok, mode='w+', encoding='latin-1')
        x.writelines(text)
        x.close()
        #os.remove(config.file_raw)

        #Overwrite csv without blank lines
        with open(config.file_ok, mode='r', encoding='utf-8') as inp, open(config.file_ok2, mode='w', encoding='utf-8') as output:
            non_blank = (line for line in inp if line.strip())
            output.writelines(non_blank)
        #remove raw file
        inp.close()
        #os.remove(config.file_ok)

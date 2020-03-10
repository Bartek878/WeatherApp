#Selenium based app for weather forecast.

from weather_import import WeatherCreator
weatherCreator = WeatherCreator()
from send_email import MailSender
mailSender = MailSender()
from visualisation import ChartCreator
chartCreator = ChartCreator()
from transformator import FileTransformer
fileTransformer = FileTransformer()

def main():

    weatherCreator.open_webpage()
    weatherCreator.choose_city()
    weatherCreator.get_current_weather()
    weatherCreator.get_data_to_file()
    chartCreator.get_data_for_chart()
    fileTransformer.from_csv_to_xlsx()
    #mailSender.send_mail()
    chartCreator.create_chart()

main()

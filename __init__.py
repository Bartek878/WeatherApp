#Selenium based app for weather forecast.

from weather_import import WeatherCreator
weatherCreator = WeatherCreator()
from send_email import MailSender
mailSender = MailSender()
from visualisation import ChartCreator
chartCreator = ChartCreator()

def main():

    weatherCreator.open_webpage()
    weatherCreator.choose_city()
    weatherCreator.get_current_weather()
    weatherCreator.write_to_csv()
    mailSender.send_file()
    chartCreator.get_data_for_chart()
    chartCreator.create_chart()

main()

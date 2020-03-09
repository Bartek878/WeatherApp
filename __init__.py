#Selenium based app for weather forecast.

from weather_import import WeatherCreator
get_weather = WeatherCreator()
from send_email import MailSender
send_email = MailSender()
from visualisation import creating_visualisation
create_visualisation = ChartCreator()

def main():

    getting_weather.open_webpage()
    getting_weather.choose_city()
    get_weather.get_current_weather()
    get_weather.write_to_csv()
    send_email.send_file()
    create_visualisation.get_data_for_chart()
    create_visualisation.create_chart()

main()

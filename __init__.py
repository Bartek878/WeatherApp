#Selenium based app for weather forecast.

from weather_import import weather
weather = weather()
from send_email import Send_Message
email = Send_Message()
from visualisation import Visuals
visualise = Visuals()
from weather_import import weather
weather = weather()

def main():

    weather.set_files()
    weather.open_webpage()
    weather.choose_city()
    weather.current_weather()
    weather.write_to_csv()
    email.set_files()
    email.send_file()
    visualise.set_files()
    visualise.visual_prep()
    visualise.visual_create()

main()

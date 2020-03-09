#Selenium based app for weather forecast.

from weather_import import weather
get_weather = weather()
from send_email import Send_Message
send_email = Send_Message()
from visualisation import Visuals
create_visualisation = Visuals()

def main():

    get_weather.set_files()
    get_weather.open_webpage()
    get_weather.choose_city()
    weather.current_weather()
    weather.write_to_csv()
    send_email.set_files()
    send_email.send_file()
    create_visualisation.set_files()
    create_visualisation.visual_prep()
    create_visualisation.visual_create()

main()

#Selenium based app for weather forecast.

from weather_import import get_weather
get_weather = get_weather()
from send_email import Send_Message
send_email = Send_Message()
from visualisation import create_visualisation
create_visualisation = create_visualisation()

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

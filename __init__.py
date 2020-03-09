#Selenium based app for weather forecast.

from weather_import import getting_weather
get_weather = getting_weather()
from send_email import sending_message
send_email = sending_message()
from visualisation import creating_visualisation
create_visualisation = creating_visualisation()

def main():

    getting_weather.set_files()
    getting_weather.open_webpage()
    getting_weather.choose_city()
    weather.current_weather()
    weather.write_to_csv()
    send_email.set_files()
    send_email.send_file()
    create_visualisation.set_files()
    create_visualisation.visual_prep()
    create_visualisation.visual_create()

main()

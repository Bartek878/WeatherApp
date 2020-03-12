#Selenium based app for weather forecast.

from weather_import import WeatherImporter
weatherImporter = WeatherImporter()
from send_email import MailSender
mailSender = MailSender()
from visualisation import ChartCreator
chartCreator = ChartCreator()
from transformator import FileTransformer
fileTransformer = FileTransformer()
from visualisation import FileRemover
fileRemover = FileRemover()


def main():

    # weatherImporter.open_webpage()
    # weatherImporter.choose_city()
    # weatherImporter.get_current_weather()
    # weatherImporter.get_weather_screenshot1()
    # weatherImporter.get_data_to_file()
    # chartCreator.get_data_for_chart()
    # fileTransformer.change_csv_to_xlsx()
    # chartCreator.create_chart()
    mailSender.send_mail()
    fileRemover.remove_draft_files()


main()
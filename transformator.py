import pandas as pd
from configurator import Config
config = Config()

class FileTransformer:

    def __init__(self):
        pass

    def change_csv_to_xlsx(self):
        df = pd.read_csv(config.file_ok3, sep=',')
        writer = pd.ExcelWriter(config.file_excel, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Weather')
        writer.save()
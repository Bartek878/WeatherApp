import pandas as pd
from configurator import Config
config = Config()

class FileTransformer:

    def __init__(self):
        pass

    def change_csv_to_xlsx(self):
        read_file = pd.read_csv(config.file_ok3_r, sep=',')
        #read_file.to_excel("r'" + config.file_excel +"'", index=None, header=True)
        read_file.to_excel(config.file_excel, engine='xlsxwriter')
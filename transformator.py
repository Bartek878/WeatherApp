import pandas as pd
from configurator import Config
config = Config()

class FileTransformer:

    def __init__(self):
        pass

    def from_csv_to_xlsx(self):
        read_file = pd.read_csv('r' + config.file_ok3)
        read_file.to_excel('r' + config.file_excel, index=None, header=True)
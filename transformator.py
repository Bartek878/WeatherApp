import pandas as pd
from configurator import Config
config = Config()

class FileTransformer:

    def __init__(self):
        pass

    def from_csv_to_xlsx(self):
        read_file = pd.read_csv(config.file_ok3_r)
        read_file.to_excel(config.file_excel, index=None, header=True)

import csv
from matplotlib import pyplot as plt
from configurator import Config
config = Config()

class ChartCreator:

    def __init__(self):
        pass

    def get_data_for_chart(self):

        with open(config.file_ok2, mode='r', encoding='utf-8',  newline='') as file1:
            r = csv.reader(file1)
            data = [line for line in r]
        with open(config.file_ok3, mode='w+', encoding='utf-8', newline='') as file2:
            w = csv.writer(file2)
            w.writerow(config.header_names)
            w.writerows(data)
        filename = config.file_ok3
        with open(filename, mode='r', encoding='utf-8',  newline='') as f:
            reader = csv.reader(f)  #line 1
            header_row = next(reader)  #line 2

        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for index, column_header in enumerate(header_row):
                highs = []
            for row in reader:
                highs.append(row[1])  # append temperatures

            for row in reader:
                if row[1] == '':
                   continue  # if empty strings which can't be int occurs
                high = int(row[1])  # Convert to int
                highs.append(high)

    def create_chart(self):
        filename = config.file_ok3
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            values = []
            for row in reader:
                if row[1] == '':
                    continue
                value = int(row[1], 10)
                values.append(value)  # append temperatures

            # Create visualisation
            fig = plt.figure(dpi=128, figsize=(10, 6))
            plt.plot(values, c='red')  # Line 1
            # Form chart
            plt.title(config.chart_title, fontsize=22)
            plt.xlabel('', fontsize=16)
            plt.ylabel(config.chart_Y_axis_name, fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            plt.savefig(config.file_png)
            #plt.show()


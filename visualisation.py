class Visuals:

    def __init__(self):
        pass

    def set_files(self):
        self.file_ok = 'D:/Bartosz/Python/hackaton-2-grupa-8/pogoda_ok.csv'
        self.file_ok2 = 'D:/Bartosz/Python/hackaton-2-grupa-8/pogoda_ok2.csv'
        self.file_ok3 = 'D:/Bartosz/Python/hackaton-2-grupa-8/pogoda_ok3.csv'

    def visual_prep(self):

        text = open(self.file_ok, "r")
        text = ''.join([i for i in text]) \
            .replace("°C", "")
        x = open(self.file_ok2, "w")
        x.writelines(text)
        x.close()

        import csv
        with open(self.file_ok2,newline='') as f:
            r = csv.reader(f)
            data = [line for line in r]
        with open(self.file_ok3,'w',newline='') as f:
            w = csv.writer(f)
            w.writerow(["Godzina", "Temperatura", "Temp. Odczuwalna", "Prognoza", "Wiatr kier.", "Wiatr pr", "Wiatr pr max", "Zachmurzenie", "Opady", "Wilgotność"])
            w.writerows(data)
        filename = self.file_ok3
        with open(filename) as f:
            reader = csv.reader(f)  #line 1
            header_row = next(reader)  #line 2

        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for index,column_header in enumerate(header_row):
                highs = []
            for row in reader:
                highs.append(row[1])  # append temperatures

            for row in reader:
                if row[1] == '':
                   continue  # if empty strings which can't be int occurs
                high = int(row[1])  # Convert to int
                highs.append(high)

    def visual_create(self):
        import csv
        from matplotlib import pyplot as plt

        filename = self.file_ok3
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
            plt.title("Pogoda godzinowa na najbliższe 120h", fontsize=22)
            plt.xlabel('', fontsize=16)
            plt.ylabel("Temperatura (°C)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            plt.show()
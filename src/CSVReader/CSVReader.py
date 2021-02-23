import csv


class CSVReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        with open(filepath) as text_data:
            reader = csv.DictReader(text_data)
            for row in reader:
                self.data.append(row)
        pass

import csv


class CSVReader:
    data = []

    def __init__(self, filepath):
        self.data = []  # Clears the self.data variable so each call of the function starts clean
        # Receive filepath to the requested .csv file and append the data to self.data for extraction
        with open(filepath) as text_data:
            reader = csv.DictReader(text_data)
            for row in reader:
                self.data.append(row)
        pass

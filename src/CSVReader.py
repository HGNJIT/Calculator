import csv


class CSVReader:
    data = []

    def __init__(self, filepath):
        with open(filepath) as text_data:
            reader = csv.DictReader(text_data)
            for row in reader:
                self.data.append(row)
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects

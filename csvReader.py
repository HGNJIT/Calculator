import csv

with open('csv/Unit Test Addition.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        print("CSV row: {0}".format(row))
        line_count += 1

    print(f'Tested {} lines'.format(line_count))
import json
import csv

data = []
with open('aaa.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

with open('aaa.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)
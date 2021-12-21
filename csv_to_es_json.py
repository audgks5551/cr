import csv
import json
import collections

orderedDict = collections.OrderedDict()
from collections import OrderedDict


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    count = 0;
    with open(csvFilePath, 'r', encoding='utf-8-sig') as csvf:
        with open(jsonFilePath, 'w', encoding='utf-8-sig') as jsonf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                count = count + 1
                x = OrderedDict([('index', {"_index" : "article8", "_id" : f"{count}"})])
                jsonString = json.dumps(x)
                jsonf.write(jsonString)
                jsonf.write("\n")
                y = json.dumps(row, ensure_ascii = False)
                jsonf.write(y)
                jsonf.write("\n")


csvFilePath = r'./article.csv'
jsonFilePath = r'./article.json'
csv_to_json(csvFilePath, jsonFilePath)
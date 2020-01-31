# What is a CSV file
# How to create the Csv file
# How to use Reader and DictReader in Csv file

#Reader print in list format
from csv import reader
with open("new_csv.csv","r") as new:
    data = reader(new)
    for i in data:
        print(i)

#DictReader print in dictionary format
from csv import DictReader
with open("new_csv.csv","r") as new:
    data = DictReader(new)
    for i in data:
        print(i)
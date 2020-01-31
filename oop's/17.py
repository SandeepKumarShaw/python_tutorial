# How to write in csv file
# create the csv file by using writer
#  Writer and Dictwriter in python

# from csv import writer

from csv import writer
with open("new_writer_csv.csv","w") as new:
    new_data = writer(new)
    #method --> writerow, writerows
    new_data.writerow(["name","age"])
    new_data.writerow(["sandeep",30])
    new_data.writerow(["lee",50])
    new_data.writerow(["zacl",60])

    new_data.writerows([["name","age"],["sandeep",30],["lee",50],["zacl",60]])


from csv import DictWriter
with open("dict_csv.csv","w",newline = "") as new:
    new_data = DictWriter(new,fieldnames = ["name","age"])
    new_data.writeheader()
    new_data.writerow({
        "name":"sandeep",
        "age":30
    })
    new_data.writerow({
        "name":"sampt",
        "age":23
    })
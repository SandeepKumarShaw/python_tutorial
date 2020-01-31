# reader,Dictreader
# writer,Dictwriter

from csv import DictReader,DictWriter
with open("dict_csv.csv","r") as read_file:
    with open("new_writer_file.csv","w") as new_writer:
        data_read = DictReader(read_file)
        data_write = DictWriter(new_writer, fieldnames = ["name","age"])
        data_write.writeheader()
        for i in data_read:
            fname,Ages = i["name"],i["age"]
            data_write.writerow(
                {
                    "name":fname,
                    "age":Ages,

                }
            ) 
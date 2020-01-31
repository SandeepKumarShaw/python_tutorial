# How to read the emoji in file by using encoding
# How to read the number of character in in line

with open("Example.txt","r", encoding="utf-8") as rf:
    data = rf.read()
    print(data)
# With Block
# different mode in file 
# w,a,r+
# how to copy text from one file to another


# with open("Example.txt") as new_file:
#     data = new_file.read()
#     print(data)

# with open("Example.txt","w") as new_file:
#     new_file.write("Test")

# with open("File1.txt","a") as new_file:
#     new_file.write("Hello World")

# with open("File1.txt","r+") as new_file:
#     new_file.seek(len(new_file.read()))
#     print(new_file.tell())
#     new_file.write("SAndeep shaw")

with open("File1.txt","r") as textfile:
    with open("create_new.txt","w") as writefile:
        writefile.write(textfile.read())



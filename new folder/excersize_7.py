number = input("Enter any number")
total = 0
i = 0
while i<len(number):
    total = total + int(number[i])
    i = i + 1
print(total)    
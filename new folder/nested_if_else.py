winning_number = 4
user = int(input("enter any number between 1 and 10 :-"))
if user == winning_number:
    print("you selected a right number")
else:
    if user > winning_number:
        print("you enter number is too heigh")
    else:
        print("you enter number is too low")        

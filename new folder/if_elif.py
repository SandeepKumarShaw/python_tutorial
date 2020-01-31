age = int(input("Enter your age :-"))
if age == 0 or age < 0:
    print("you enter wrong age")
elif 0 < age <= 5:
    print("Ticket price : free")
elif 5<age<=15:
    print("Ticket price : 100")
elif 15<age<=50:
    print("Ticket price : 150")
else:
    print("Ticket price : 200")    

         

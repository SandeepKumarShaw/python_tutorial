# Python Object oriented programming(OOP)

# Class ,Object,Method
# class is blue print
# # list class
# number = [1,2,3,4,5,6,7,8,9,10]
# number2 = ["mahendar","2","singh"]
# number.append(11)
# print(number)

# Objective
# What is a class
# How to create an class
# What is init Method we can also call construtor
# What are Attribute ,Instance variable
# How to create our object

class mobile:
    def __init__(self,company,price,camera):
        #self here assign object
        self.company_name = company
        self.mobile_price = price
        self.camera_mp = camera

#object create
mobile1 = mobile("samsung",2000,48)
mobile2 = mobile("apple",22000,12)

print(mobile1.company_name)
print(mobile2.camera_mp)

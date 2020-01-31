# Multilevel inheritance
# More about method overiding(MRO)
class Person:#base class/ Paranet class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    @property
    def printname(self):
        print(self.firstname, self.lastname)  

class Student(Person):#child class of person parent class
    def __init__(self, fname, lname, year, Roll_number):
        # access parent class method: 1
        #Person.__init__(self, fname, lname)
        # access parent class method: 2
        super().__init__(fname, lname)

        self.graduationyear = year
        self.roll_number = Roll_number
    @property
    def welcome(self):
        return f"Welcome {self.firstname} {self.lastname} roll number is {self.roll_number}"    
    @property #decorator for without parenthessis use of class method
    #Overwriting parent class method in child class
    def printname(self):
        return f"Welcome {self.firstname} {self.lastname} roll number is {self.roll_number}"        

class Student_more(Student):#child class of student parent class
    def __init__(self, fname, lname, year, Roll_number, age, phone):
        # access parent class method: 1
        #Person.__init__(self, fname, lname)
        # access parent class method: 2
        super().__init__(fname, lname, year, Roll_number)

        self.user_age = age
        self.user_phone = phone
           

Student1 = Student("sandeep", "shaw", 2020, 615)

Student2 = Student_more("sandeep", "shaw", 2020, 615,31,9748383870)

#print(Student1.firstname)
print(Student2.firstname)
print(Student2.user_age)
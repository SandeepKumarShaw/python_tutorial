# multiple inheritance
class Person:
    #defining Constructor
    def __init__(self, personName, PersonAge):
        self.name = personName
        self.age  = PersonAge
    #defining instance methods
    def showName(self):
        print(self.name)
    
    def showAge(self):
        print(self.age)

    def hello(self):
        return f"this is a Person Class"   

# defining another class
class Student:
    def __init__(self, studentId):
        self.studentId = studentId

    def getId(self):    
        return self.studentId

    def hello(self):
        return f"this is student class"  

class Resident(Person, Student):# extends both person and student class
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)


res1 = Resident("sandeep",30,102)
print(res1.name)
print(res1.showName())
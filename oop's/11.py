# Special Magic method/Dunder method
# __str__
# __repr__
# __len__
# operator overloading
# Polymorphism - method overriding

class Person:
    #defining constructor
    def __init__(self, PersonName, PersonAge):
        self.name = PersonName
        self.age = PersonAge

    def names(self):
        return self.name

    def __str__(self):
        return f"your name is {self.name} and your age is {self.age}"   

    def __repr__(self):
        return f"your name is {self.name} and your age is {self.age}"            

    def __len__(self):
        return len(self.name)  
    # operator overloading
    def __add__(self, another_self):
        return self.age + another_self.age    

class Persons(Person):
    def __init__(self, PersonName, PersonAge):

        super().__init__(PersonName, PersonAge)
    @property
    def names(self):
        return f"your name is {self.name} and your age is {self.age}"


#person = Person("sandeep",30)
#person1 = Person("sandeep",33)
#print(person+person1)
# print(person.__str__())  
# print(person.__repr__())   
# print(person.__len__())   

persons = Persons("sandeep",30)
print(persons.names)
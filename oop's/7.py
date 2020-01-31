# more about classes 
# property,Getter and setter

class person:
    def __init__(self,name,surname,age):
        self.user_name = name
        self.user_surname = surname
        self.user_age = age
        self.user_age = max(age,0)
    @property    
    def username_age(self):
        return f"your name is {self.user_name} and your age is {self.user_age}"
    @property
    def new_age(self):
        return self.user_age
    @new_age.setter
    def new_ages(self,agess):
        self.user_age = max(agess,0)

    def full_name(self):
        return f"Your full name is {self.user_name} {self.user_surname}"


person1 = person("sandeep","shaw", 21)
#print(person1.user_name)
#print(person1.user_surname)
person1.new_ages = 1
print(person1.username_age)

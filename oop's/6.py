# Encapsulation
# Abstraction:
#    Abstraction: — Implementation hiding.
# Special naming convention
# Naming Mangling
class person:
    def __init__(self,name,surname,age):
        self.user_name = name
        self.user_surname = surname
        self.user_age = age
    def full_name(self):
        return f "Your full name is {self.user_name} {self.user_surname}"

person1 = person("sandeep","shaw", 30)
print(person1.user_name)
print(person1.user_surname)
print(person1.user_age)
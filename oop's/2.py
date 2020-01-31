# instance Variable
# Instance methode
class car:
    def __init__(self,name,color,price):
        self.car_name = name
        self.car_color = color
        self.car_price = price
        self.car_name_color = name + "" + color
        self.car_name_price = (f"the car name is {name} and the car price is {price}")
    def price_check(self):
        return self.car_price > 1000000
        # if self.car_price > 1000000:
        #     print("price is too high")
        # else:
        #     print("price is too low")    
car1 = car("Honda","red",1200000)


print(car1.car_name)  
print(car1.car_color)          
print(car1.car_price)      
print(car1.car_name_color)      
print(car1.car_name_price)  

print(car1.price_check())      
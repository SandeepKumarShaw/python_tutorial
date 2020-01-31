# Class Method

class car:
    # offer_price = 20
    total_object = 0

    def __init__(self,name,color,price):

        car.total_object +=1
        self.car_name = name
        self.car_color = color
        self.car_price = price
        self.car_name_color = name + "" + color
        self.car_name_price = (f"the car name is {name} and the car price is {price}")

    def offer(self):
        new_var = (self.offer_price*self.car_price)/100
        return f"after offer car price is {self.car_price-new_var}"

car1 = car("Honda","red",12000000)  
car2 = car("Honda","red",12000000)  
car3 = car("Honda","red",12000000)  

print(car.total_object)      

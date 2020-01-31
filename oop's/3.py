# class variable
class car:
    offer_price = 20
    def __init__(self,name,color,price):
        self.car_name = name
        self.car_color = color
        self.car_price = price
        self.car_name_color = name + "" + color
        self.car_name_price = (f"the car name is {name} and the car price is {price}")

    def offer(self):
        new_var = (car.offer_price*self.car_price)/100
        return f"after offer car price is {self.car_price-new_var}"

car1 = car("Honda","red",12000000)  
print(car1.offer())      

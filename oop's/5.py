
# static Method

class car:
    total_object = 0
    def __init__(self,name,color,price):
        car.total_object += 1
        self.car_name = name
        self.car_color = color
        self.car_price = price
    
    @classmethod
    def object_create(car,all_input):
        car_n,car_c,car_p = all_input.split(",")
        return car(car_n,car_c,car_p)
    @staticmethod
    def static_video():
        return ("this is a static tutorial video")
    @staticmethod
    def cube(a):
        return a**3 


    @classmethod
    def total(car):
        return f"you have create total {car.total_object} object of this class"
        
    def offer(self):
        new_var = (car.offer_price*self.car_price)/100
        return f"after offer car price is {self.car_price - new_var}"

print(car.static_video())
print(car.cube(2))

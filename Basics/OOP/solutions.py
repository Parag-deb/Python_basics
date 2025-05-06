# create a car c;ass with attributes like brand and model, 
# then create an instance of this class

# add method to the car class that displays the full name of the car( brand and model)
# class Car:
#     brand = None
#     model = None

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"BRAND: {self.brand} MODEL:{self.model}"
        


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand , my_new_car.model)
print(my_new_car.full_name())




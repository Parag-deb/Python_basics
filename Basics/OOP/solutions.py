# 1.create a car c;ass with attributes like brand and model, 
#   then create an instance of this class

# 2.add method to the car class that displays the full name of the car( brand and model)
# 3. Create an ElectricCar class that inherits from the car class and has an additional attributes battery_size
# 4. Encapsulation - Modify the car class to encapsulate the brand attribute, making it private and provide a getter method of it 

# class Car:
#     brand = None
#     model = None

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"BRAND: {self.brand} MODEL: {self.model}"
    


my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand , my_new_car.model)
print(my_new_car.full_name())

# Quertion 3
print()
print("-----inheritance - Question 3-----")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
print(my_tesla.full_name())






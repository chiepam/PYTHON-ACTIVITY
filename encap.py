class Car:
    def __init__(self, make, model):
        self.make = make 
        self.model = model
        self.__speed = 0 

    def accelerate(self, increment):
        if increment > 0:
            self.__speed += increment
            print(f"Speed increased to {self.__speed} km/h")

    def brake(self, decrement):
        if decrement > 0 and self.__speed - decrement >= 0:
            self.__speed -= decrement
            print(f"Speed decreased to {self.__speed} km/h")
        else:
            print("Cannot brake below 0 km/h")

    def get_speed(self):
        return self.__speed


my_car = Car("Toyota", "Corolla")
my_car.accelerate(50)
my_car.brake(20)
print(f"Current speed: {my_car.get_speed()} km/h")



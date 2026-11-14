class Vehicle:

    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def info(self):
        print(f"Brand:{self.brand}| Spped:{self.speed}")


class Car(Vehicle):

    def __init__(self, brand, speed,door):
        super().__init__(brand, speed)
        self.door=door

    def car_info(self):
        self.info()
        print(f"Door{self.door}")


class Bike(Vehicle):

    def __init__(self, brand, speed,has_gear):
        super().__init__(brand, speed)
        self.has_gear=has_gear





c = Car("Honda", 100, 4)
c.car_info()
b = Bike("Yamaha", 80, True)
b.info()
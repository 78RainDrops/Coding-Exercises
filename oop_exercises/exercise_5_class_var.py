class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"{self.color, self.name, 'Speed:', self.max_speed, 'Mileage:', self.mileage}"


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


school_bus = Bus("School Bus", 180, 12)
print(school_bus)
car = Car("Audi Q5", 240, 18)
print(car)

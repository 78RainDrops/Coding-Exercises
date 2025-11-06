class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f"Max Speed: {self.max_speed} | Mileage: {self.mileage}"


modelX = Vehicle(240, 18)
print(modelX)


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)


bus1 = Bus(250, 40)
print(bus1)

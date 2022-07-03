
class Vehicle:

    fuel_consumption = 1.25
    DEFAULT_FUEL_CONSUMPTION = fuel_consumption

    def __init__(self, fuel: float, horse_power: int, fuel_consumption=1.25):
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        if self.fuel - (kilometers * self.fuel_consumption) >= 0:
            self.fuel -= kilometers * self.fuel_consumption


vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
# print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
